#!/usr/bin/env python3
"""Automated threat-intelligence pipeline.

Collects CISA KEV, NVD CVEs, CISA and GitHub security advisories, adds AI summaries
(Copilot CLI), and writes JSON data, CVE pages and daily/weekly report pages.
"""
import argparse
import collections
import datetime as dt
import email.utils
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

DATA = "assets/data/threat-intel"
REPORTS = "threat-intel/reports"
CVE_PAGES = "threat-intel/cve"
KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
CISA_RSS = "https://www.cisa.gov/cybersecurity-advisories/all.xml"
GHSA_URL = "https://api.github.com/advisories?per_page=100&type=reviewed"
HEADER_IMG = "https://live.staticflickr.com/65535/55672381423_3128d9aaf7_b.jpg"

RETENTION_DAYS = 30        # critical (9.0+) non-KEV CVEs kept this long
HIGH_RETENTION_DAYS = 7    # 7.0-8.9 non-KEV CVEs kept this long
ADVISORY_DAYS = 45
MIN_CVSS = 7.0             # non-KEV CVEs below this are not stored
KEV_PAGE_DAYS = 90         # KEV entries added within this window get a detail page
AI_MAX = int(os.environ.get("AI_MAX", "30"))
AI_BATCH = 8
UA = {"User-Agent": "Mozilla/5.0 (compatible; shantoroy.com threat-intel bot)"}
TODAY = dt.datetime.now(dt.timezone.utc).date()


def log(*a):
    print(*a, file=sys.stderr)


def http(url, headers=None, retries=3, timeout=60):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={**UA, **(headers or {})})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as exc:
            if i == retries - 1:
                raise
            log(f"retry {url[:80]}: {exc}")
            time.sleep(8 * (i + 1))


def curl(url):
    """CISA's CDN rejects Python's TLS fingerprint but accepts curl."""
    return subprocess.run(["curl", "-fsSL", "--max-time", "60", "-A", "Mozilla/5.0", url],
                          capture_output=True, check=True).stdout


def jget(url, headers=None):
    return json.loads(http(url, headers))


def clean(text):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", text or ""))).strip()


def load(name, default):
    try:
        with open(f"{DATA}/{name}") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def dump_list(name, rows):
    """One record per line keeps daily git diffs small."""
    os.makedirs(DATA, exist_ok=True)
    with open(f"{DATA}/{name}", "w") as f:
        f.write("[\n" + ",\n".join(json.dumps(r, separators=(",", ":"), ensure_ascii=False) for r in rows) + "\n]\n")


def d(s):
    try:
        return dt.date.fromisoformat((s or "")[:10])
    except ValueError:
        return None


# ---------------------------------------------------------------- collectors
def sev_from_score(score):
    if score is None:
        return ""
    return "CRITICAL" if score >= 9 else "HIGH" if score >= 7 else "MEDIUM" if score >= 4 else "LOW"


def pretty(s):
    return s.replace("_", " ").strip()


def nvd_item(v):
    c = v["cve"]
    desc = re.sub(r"\s+", " ", next((x["value"] for x in c.get("descriptions", []) if x["lang"] == "en"), "")).strip()
    if c.get("vulnStatus") == "Rejected" or desc.startswith("** REJECT"):
        return None
    score = vec = None
    for key in ("cvssMetricV40", "cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
        ms = c.get("metrics", {}).get(key)
        if ms:
            m = next((x for x in ms if x.get("type") == "Primary"), ms[0])
            score, vec = m["cvssData"]["baseScore"], m["cvssData"].get("vectorString")
            break
    techs, vendor, product = [], "", ""
    for cfg in c.get("configurations", []):
        for node in cfg.get("nodes", []):
            for m in node.get("cpeMatch", []):
                if not m.get("vulnerable"):
                    continue
                p = m["criteria"].split(":")
                if len(p) > 4:
                    vendor = vendor or pretty(p[3]).title()
                    product = product or pretty(p[4])
                    t = f"{pretty(p[3])} {pretty(p[4])}"
                    if t not in techs:
                        techs.append(t)
    if not vendor:
        for aff in c.get("affected", []):
            for ad in aff.get("affectedData", []):
                if ad.get("vendor", "n/a").lower() not in ("n/a", "") and ad.get("product", "n/a").lower() != "n/a":
                    vendor, product = vendor or ad["vendor"], product or ad["product"]
                    t = f"{ad['vendor']} {ad['product']}"
                    if t not in techs:
                        techs.append(t)
    cwes = sorted({x["value"] for w in c.get("weaknesses", []) for x in w.get("description", [])
                   if x["value"].startswith("CWE-")})
    return {
        "id": c["id"], "pub": c["published"][:10], "mod": c["lastModified"][:10],
        "cvss": score, "sev": sev_from_score(score), "vec": vec, "vendor": vendor, "product": product,
        "desc": desc[:500], "cwe": cwes, "tech": techs[:6],
        "refs": [r["url"] for r in c.get("references", [])[:5]],
    }


def collect_nvd(days):
    key = os.environ.get("NVD_API_KEY")
    pause = 0.8 if key else 6.5
    end = dt.datetime.now(dt.timezone.utc)
    start = end - dt.timedelta(days=days)
    out, idx = [], 0
    while True:
        q = {"lastModStartDate": start.strftime("%Y-%m-%dT%H:%M:%S.000"),
             "lastModEndDate": end.strftime("%Y-%m-%dT%H:%M:%S.000"),
             "resultsPerPage": 2000, "startIndex": idx}
        data = jget(NVD_URL + "?" + urllib.parse.urlencode(q), {"apiKey": key} if key else None)
        out += data["vulnerabilities"]
        idx += data["resultsPerPage"]
        if idx >= data["totalResults"]:
            break
        time.sleep(pause)
    cutoff = TODAY - dt.timedelta(days=RETENTION_DAYS)
    items = []
    for v in out:
        it = nvd_item(v)
        if it and d(it["pub"]) >= cutoff and it["cvss"] is not None and it["cvss"] >= MIN_CVSS:
            items.append(it)
    log(f"nvd: {len(out)} modified, {len(items)} kept")
    return items


def collect_kev():
    data = jget(KEV_URL)
    items = []
    for k in data["vulnerabilities"]:
        items.append({
            "id": k["cveID"], "kev": 1, "kev_added": k["dateAdded"], "due": k.get("dueDate"),
            "ransom": 1 if k.get("knownRansomwareCampaignUse") == "Known" else 0,
            "vendor": k["vendorProject"], "product": k["product"], "title": k["vulnerabilityName"],
            "desc": k["shortDescription"][:500], "action": k.get("requiredAction", "")[:400],
            "cwe": k.get("cwes", []),
        })
    log(f"kev: {len(items)} entries")
    return items


def enrich_kev(store, limit):
    """Fill CVSS for KEV entries from NVD, newest first."""
    key = os.environ.get("NVD_API_KEY")
    todo = sorted((i for i in store.values() if i.get("kev") and i.get("cvss") is None and not i.get("nvd_miss")),
                  key=lambda i: i["kev_added"], reverse=True)[:limit]
    for it in todo:
        try:
            data = jget(f"{NVD_URL}?cveId={it['id']}", {"apiKey": key} if key else None)
            n = nvd_item(data["vulnerabilities"][0]) if data["vulnerabilities"] else None
        except Exception as exc:
            log(f"enrich {it['id']}: {exc}")
            n = None
        if n:
            for f in ("pub", "mod", "cvss", "sev", "vec", "tech", "refs"):
                it[f] = n[f]
            it["cwe"] = it.get("cwe") or n["cwe"]
        else:
            it["nvd_miss"] = 1
        time.sleep(0.8 if key else 6.5)


def collect_advisories():
    out = []
    try:
        root = ET.fromstring(curl(CISA_RSS))
        for it in root.iter("item"):
            try:
                date = email.utils.parsedate_to_datetime(it.findtext("pubDate") or "").date().isoformat()
            except (TypeError, ValueError):
                continue
            title, desc = clean(it.findtext("title")), clean(it.findtext("description"))
            out.append({"id": (it.findtext("link") or "").strip(), "title": title, "url": (it.findtext("link") or "").strip(),
                        "source": "CISA", "date": date, "sev": "", "summary": desc[:400],
                        "cves": sorted(set(re.findall(r"CVE-\d{4}-\d{4,7}", f"{title} {desc}")))[:8], "tech": []})
    except Exception as exc:
        log(f"warn: cisa advisories: {exc}")
    try:
        hdr = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else None
        for a in jget(GHSA_URL, hdr):
            if a["severity"] not in ("high", "critical"):
                continue
            techs = [f"{v['package']['name']} ({v['package']['ecosystem']})" for v in a.get("vulnerabilities", [])
                     if v.get("package")]
            out.append({"id": a["html_url"], "title": a["summary"], "url": a["html_url"], "source": "GitHub",
                        "date": a["published_at"][:10], "sev": a["severity"].upper(), "summary": clean(a["description"])[:400],
                        "cves": [a["cve_id"]] if a.get("cve_id") else [], "tech": techs[:5]})
    except Exception as exc:
        log(f"warn: ghsa: {exc}")
    log(f"advisories: {len(out)}")
    return out


# ---------------------------------------------------------------- AI
def ask_ai(prompt, retries=2):
    if os.environ.get("NO_AI"):
        return None
    for i in range(retries):
        try:
            # Tools are disabled so untrusted feed text cannot trigger any actions
            r = subprocess.run(["copilot", "-p", prompt, "-s", "--no-ask-user", "--available-tools="],
                               capture_output=True, text=True, timeout=600, check=True)
            return r.stdout.strip()
        except Exception as exc:
            log(f"ai attempt {i + 1} failed: {exc}")
    return None


def parse_json_array(text):
    if not text:
        return []
    a, b = text.find("["), text.rfind("]")
    try:
        return json.loads(text[a:b + 1])
    except ValueError:
        return []


def summarize(store, touched):
    recent = TODAY - dt.timedelta(days=14)

    def eligible(i):
        if "ai" in i:
            return False
        return (i.get("kev") and (d(i["kev_added"]) or dt.date.min) >= recent) or (i.get("cvss") or 0) >= 9

    def priority(i):
        return (0 if i.get("kev") else 1, -(i.get("cvss") or 0))

    todo = sorted((store[t] for t in touched if eligible(store[t])), key=priority)[:AI_MAX]
    log(f"ai: summarizing {len(todo)} items")
    for n in range(0, len(todo), AI_BATCH):
        batch = todo[n:n + AI_BATCH]
        payload = [{"id": i["id"], "vendor": i.get("vendor"), "product": i.get("product"), "title": i.get("title"),
                    "description": i["desc"][:500], "cvss": i.get("cvss"), "cpe_products": i.get("tech", []),
                    "known_exploited": bool(i.get("kev"))} for i in batch]
        prompt = (
            "You are a vulnerability analyst writing for security engineers. For EACH vulnerability below, "
            "using ONLY the provided data, return a JSON array (no prose, no code fences) of objects with keys: "
            '"id", "summary" (1-2 plain-English sentences on what the flaw is and why it matters), '
            '"affected" (array of up to 5 affected products/technologies, with versions only if given), '
            '"impact" (one short phrase such as "remote code execution"), '
            '"action" (one sentence of defensive remediation advice). '
            "Do not invent facts and do not include exploit instructions.\n\n" + json.dumps(payload, indent=1))
        for r in parse_json_array(ask_ai(prompt)):
            if isinstance(r, dict) and r.get("id") in store and r.get("summary"):
                store[r["id"]]["ai"] = {k: r.get(k) for k in ("summary", "affected", "impact", "action")}


# ---------------------------------------------------------------- pages
def notable(i):
    if i.get("kev"):
        return (d(i["kev_added"]) or dt.date.min) >= TODAY - dt.timedelta(days=KEV_PAGE_DAYS)
    return (i.get("cvss") or 0) >= 9 and "ai" in i


def fm(**kw):
    lines = ["---"]
    for k, v in kw.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            lines += [f"  - {json.dumps(x)}" if isinstance(x, str) else f"  - {x}" for x in v]
        elif isinstance(v, dict):
            lines.append(f"{k}:")
            lines += [f"  {a}: {json.dumps(b)}" for a, b in v.items()]
        elif isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        else:
            lines.append(f"{k}: {json.dumps(v) if isinstance(v, str) else v}")
    lines.append("---\n")
    return "\n".join(lines)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def label(i):
    v, p = i.get("vendor") or "", i.get("product") or ""
    return (p if v.lower() == p.lower() else f"{v} {p}".strip()) or "Vendor not specified"


def cve_page(i):
    ai = i.get("ai") or {}
    rows = [("CVSS", f"{i['cvss']} ({i['sev'].title()})" if i.get("cvss") is not None else "Not yet scored"),
            ("Vendor / product", label(i))]
    if i.get("kev"):
        rows += [("CISA KEV", f"Added {i['kev_added']}, remediation due {i.get('due') or 'n/a'}"),
                 ("Ransomware use", "Known" if i.get("ransom") else "Unknown")]
    if i.get("pub"):
        rows.append(("Published", i["pub"]))
    if i.get("cwe"):
        rows.append(("Weakness", ", ".join(i["cwe"])))
    if i.get("vec"):
        rows.append(("Vector", f"`{i['vec']}`"))
    body = [fm(layout="single", title=f"{i['id']}: {i.get('title') or label(i)}",
               excerpt=(ai.get("summary") or i["desc"])[:200], permalink=f"/threat-intel/cve/{i['id']}/",
               header={"image": HEADER_IMG, "teaser": HEADER_IMG},
               tags=["Threat Intelligence", "CVE"] + (["CISA KEV"] if i.get("kev") else []),
               toc=False, sitemap=True)]
    body.append("*AI-assisted summary built from NVD and CISA data. Verify against the linked sources before acting.*\n")
    body.append(f"## Summary\n\n{ai.get('summary') or i['desc']}\n")
    if ai.get("impact"):
        body.append(f"**Impact:** {ai['impact']}\n")
    aff = ai.get("affected") or i.get("tech") or []
    if aff:
        body.append("## Affected technologies\n\n" + "\n".join(f"- {a}" for a in aff) + "\n")
    action = ai.get("action") or i.get("action")
    if action:
        body.append(f"## Recommended action\n\n{action}\n")
    body.append("## Details\n\n| | |\n|---|---|\n" + "\n".join(f"| {a} | {b} |" for a, b in rows) + "\n")
    body.append(f"## Original description\n\n> {i['desc']}\n")
    refs = [f"- [NVD record](https://nvd.nist.gov/vuln/detail/{i['id']})"]
    if i.get("kev"):
        refs.append("- [CISA Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)")
    refs += [f"- <{r}>" for r in i.get("refs", [])]
    body.append("## References\n\n" + "\n".join(refs) + "\n")
    body.append("[← Threat intelligence dashboard](/threat-intel/)\n")
    write(f"{CVE_PAGES}/{i['id']}.md", "\n".join(body))


def link(i):
    return f"[{i['id']}](/threat-intel/cve/{i['id']}/)" if i.get("page") else f"[{i['id']}](https://nvd.nist.gov/vuln/detail/{i['id']})"


def line(i):
    s = (i.get("ai") or {}).get("summary") or (i["desc"][:220] + ("…" if len(i["desc"]) > 220 else ""))
    score = f" · CVSS {i['cvss']}" if i.get("cvss") is not None else ""
    flag = " · 🔥 ransomware use" if i.get("ransom") else ""
    return f"- **{link(i)}** — {label(i)}{score}{flag}\n  {s}"


def overview(kind, facts):
    prompt = (f"Write the opening of a {kind} cybersecurity threat-intelligence report for security engineers. "
              "Using ONLY the data below, output markdown: a 3-4 sentence overview of the main themes, then a "
              "'### Defender priorities' heading with 3 short bullet points of defensive actions. "
              "No title, no front matter, no invented facts.\n\n" + json.dumps(facts, indent=1))
    return ask_ai(prompt)


def brief(i):
    return {"id": i["id"], "who": label(i), "cvss": i.get("cvss"), "kev": bool(i.get("kev")),
            "summary": ((i.get("ai") or {}).get("summary") or i["desc"])[:200]}


def daily_report(store, advisories, force):
    path = f"{REPORTS}/daily/{TODAY}.md"
    if os.path.exists(path) and not force:
        return
    since = TODAY - dt.timedelta(days=1)
    kev = sorted((i for i in store.values() if i.get("kev") and (d(i["kev_added"]) or dt.date.min) >= since),
                 key=lambda i: i["kev_added"], reverse=True)
    crit = sorted((i for i in store.values() if not i.get("kev") and (i.get("cvss") or 0) >= 9 and
                   (d(i.get("pub")) or dt.date.min) >= since), key=lambda i: -i["cvss"])[:15]
    advs = [a for a in advisories if (d(a["date"]) or dt.date.min) >= since][:12]
    if not (kev or crit or advs):
        log("daily: nothing to report")
        return
    ov = overview("daily", {"kev_additions": [brief(i) for i in kev[:10]], "critical_cves": [brief(i) for i in crit[:10]],
                            "advisories": [a["title"] for a in advs]}) or \
        f"Today's snapshot: {len(kev)} CISA KEV additions, {len(crit)} new critical CVEs and {len(advs)} security advisories."
    out = [fm(layout="single", title=f"Daily Threat Intelligence Report – {TODAY.strftime('%B %-d, %Y')}",
              excerpt=f"{len(kev)} KEV additions, {len(crit)} critical CVEs and {len(advs)} advisories.",
              permalink=f"/threat-intel/reports/daily/{TODAY}/", report_type="daily", report_date=str(TODAY),
              header={"image": HEADER_IMG, "teaser": HEADER_IMG}, tags=["Threat Intelligence", "Daily Report"],
              toc=True, toc_label="Table of Contents", toc_icon="package", sitemap=True),
           "*Auto-generated from CISA KEV, NVD and public advisories; summaries are AI-assisted.*\n", ov + "\n"]
    out.append(f"## CISA KEV additions ({len(kev)})\n\n" + ("\n".join(line(i) for i in kev) or "None in this window.") + "\n")
    out.append(f"## New critical CVEs ({len(crit)})\n\n" + ("\n".join(line(i) for i in crit) or "None in this window.") + "\n")
    out.append(f"## Security advisories ({len(advs)})\n\n" + ("\n".join(
        f"- [{a['title']}]({a['url']}) — {a['source']}" + (f" ({', '.join(a['cves'][:3])})" if a["cves"] else "")
        for a in advs) or "None in this window.") + "\n")
    out.append("[← Threat intelligence dashboard](/threat-intel/) · [All reports](/threat-intel/reports/)\n")
    write(path, "\n".join(out))
    log("wrote", path)


def weekly_report(store, advisories, force):
    year, week, _ = TODAY.isocalendar()
    path = f"{REPORTS}/weekly/{year}-W{week:02d}.md"
    if os.path.exists(path) and not force:
        return
    since = TODAY - dt.timedelta(days=7)
    kev = sorted((i for i in store.values() if i.get("kev") and (d(i["kev_added"]) or dt.date.min) >= since),
                 key=lambda i: i["kev_added"], reverse=True)
    crit = sorted((i for i in store.values() if not i.get("kev") and (i.get("cvss") or 0) >= 9 and
                   (d(i.get("pub")) or dt.date.min) >= since), key=lambda i: -i["cvss"])
    high = [i for i in store.values() if not i.get("kev") and 7 <= (i.get("cvss") or 0) < 9 and
            (d(i.get("pub")) or dt.date.min) >= since]
    advs = [a for a in advisories if (d(a["date"]) or dt.date.min) >= since]
    if not (kev or crit or high):
        return
    vendors = collections.Counter(label(i) for i in kev + crit + high)
    techs = collections.Counter(t for i in crit + kev for t in ((i.get("ai") or {}).get("affected") or i.get("tech") or []))
    ransom = sum(i.get("ransom", 0) for i in kev)
    ov = overview("weekly", {"kev_additions": len(kev), "ransomware_linked": ransom, "critical": len(crit), "high": len(high),
                             "top_vendors": vendors.most_common(8), "top_technologies": techs.most_common(8),
                             "top_kev": [brief(i) for i in kev[:8]], "top_critical": [brief(i) for i in crit[:8]]}) or \
        f"This week: {len(kev)} KEV additions, {len(crit)} critical and {len(high)} high-severity new CVEs."
    out = [fm(layout="single", title=f"Weekly Threat Intelligence Report – Week {week}, {year}",
              excerpt=f"{len(kev)} KEV additions, {len(crit)} critical and {len(high)} high-severity CVEs ({since} to {TODAY}).",
              permalink=f"/threat-intel/reports/weekly/{year}-W{week:02d}/", report_type="weekly", report_date=str(TODAY),
              header={"image": HEADER_IMG, "teaser": HEADER_IMG}, tags=["Threat Intelligence", "Weekly Report"],
              toc=True, toc_label="Table of Contents", toc_icon="package", sitemap=True),
           f"*Coverage: {since} to {TODAY}. Auto-generated; summaries are AI-assisted.*\n", ov + "\n",
           "## By the numbers\n\n| Metric | Count |\n|---|---|\n"
           f"| CISA KEV additions | {len(kev)} |\n| Ransomware-linked KEV additions | {ransom} |\n"
           f"| New critical CVEs (9.0+) | {len(crit)} |\n| New high CVEs (7.0–8.9) | {len(high)} |\n"
           f"| Advisories published | {len(advs)} |\n",
           "## Most affected vendors\n\n" + "\n".join(f"- {v} — {n}" for v, n in vendors.most_common(10)) + "\n"]
    if techs:
        out.append("## Most affected technologies\n\n" + "\n".join(f"- {t} — {n}" for t, n in techs.most_common(10)) + "\n")
    out.append(f"## CISA KEV additions ({len(kev)})\n\n" + ("\n".join(line(i) for i in kev[:40]) or "None.") + "\n")
    out.append(f"## Top critical CVEs ({len(crit)})\n\n" + ("\n".join(line(i) for i in crit[:20]) or "None.") + "\n")
    out.append("[← Threat intelligence dashboard](/threat-intel/) · [All reports](/threat-intel/reports/)\n")
    write(path, "\n".join(out))
    log("wrote", path)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=2, help="NVD modification window (use ~14 for first backfill)")
    ap.add_argument("--weekly", action="store_true", help="force a weekly report (otherwise Mondays only)")
    ap.add_argument("--force", action="store_true", help="regenerate existing reports")
    ap.add_argument("--enrich", type=int, default=40, help="max KEV entries to enrich with NVD CVSS")
    args = ap.parse_args()

    store = {i["id"]: i for i in load("items.json", [])}
    touched = set()

    for n in collect_nvd(args.days):
        cur = store.setdefault(n["id"], {})
        if cur.get("mod") != n["mod"] or cur.get("cvss") != n["cvss"]:
            touched.add(n["id"])
        cur.update(n)
    for k in collect_kev():
        cur = store.setdefault(k["id"], {})
        if not cur.get("kev"):
            touched.add(k["id"])
        cur.update(k)
    enrich_kev(store, args.enrich)

    def keep(v):
        if v.get("kev"):
            return True
        days = RETENTION_DAYS if (v.get("cvss") or 0) >= 9 else HIGH_RETENTION_DAYS
        return (d(v.get("pub")) or TODAY) >= TODAY - dt.timedelta(days=days)

    store = {k: v for k, v in store.items() if keep(v)}
    for i in store.values():
        i["date"] = (i.get("kev_added") if i.get("kev") else i.get("pub")) or ""
    touched &= set(store)

    summarize(store, touched)
    for tid in touched:
        if notable(store[tid]):
            store[tid]["page"] = 1
    for i in store.values():
        if i.get("page") and (i["id"] in touched or not os.path.exists(f"{CVE_PAGES}/{i['id']}.md")):
            cve_page(i)

    advisories = {a["id"]: a for a in load("advisories.json", [])}
    for a in collect_advisories():
        advisories[a["id"]] = a
    adv_cut = TODAY - dt.timedelta(days=ADVISORY_DAYS)
    advisories = {k: v for k, v in advisories.items() if (d(v["date"]) or TODAY) >= adv_cut}

    daily_report(store, list(advisories.values()), args.force)
    if args.weekly or TODAY.weekday() == 0:
        weekly_report(store, list(advisories.values()), args.force)

    # bulky fields are only needed while generating pages
    slim = ("refs", "vec", "action")
    rows = sorted(({k: v for k, v in i.items() if k not in slim} for i in store.values()), key=lambda i: i["id"])
    dump_list("items.json", rows)
    dump_list("advisories.json", sorted(advisories.values(), key=lambda a: a["id"]))
    with open(f"{DATA}/meta.json", "w") as f:
        json.dump({"updated": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), "items": len(rows),
                   "kev": sum(1 for i in rows if i.get("kev")), "advisories": len(advisories)}, f)
    log(f"done: {len(rows)} items, {len(touched)} touched, {len(advisories)} advisories")


if __name__ == "__main__":
    main()
