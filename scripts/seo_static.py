#!/usr/bin/env python3
"""Generate crawlable static HTML (progressive enhancement) for the JS-rendered dashboards.

Search engines and LLM crawlers often don't execute JavaScript, so the latest data is rendered into
_includes/*.html at build time. The page JS removes the block once the interactive UI has loaded.
Also emits schema.org JSON-LD (ItemList) matching the visible content.
"""
import datetime as dt
import html
import json

SITE = "https://shantoroy.com"


def load(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def liquid_safe(t):
    return t.replace("{{", "{ {").replace("{%", "{ %")


def e(s):
    return liquid_safe(html.escape(str(s or ""), quote=True))


def ld(obj):
    return '<script type="application/ld+json">' + liquid_safe(json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")) + "</script>"


def threat_intel():
    items = load("assets/data/threat-intel/items.json", [])
    meta = load("assets/data/threat-intel/meta.json", {})
    advisories = load("assets/data/threat-intel/advisories.json", [])
    kev = sorted((i for i in items if i.get("kev")), key=lambda i: i.get("kev_added") or "", reverse=True)[:15]
    crit = sorted((i for i in items if not i.get("kev") and (i.get("cvss") or 0) >= 9),
                  key=lambda i: i.get("pub") or "", reverse=True)[:10]
    advs = sorted(advisories, key=lambda a: a.get("date") or "", reverse=True)[:8]

    def href(i):
        return f"/threat-intel/cve/{i['id']}/" if i.get("page") else f"https://nvd.nist.gov/vuln/detail/{i['id']}"

    def li(i):
        who = " ".join(x for x in (i.get("vendor"), i.get("product")) if x)
        text = (i.get("ai") or {}).get("summary") or i.get("desc") or ""
        cvss = f" · CVSS {i['cvss']}" if i.get("cvss") else ""
        added = f" · added to CISA KEV {i['kev_added']}" if i.get("kev_added") else ""
        return (f'<li><a href="{e(href(i))}"><strong>{e(i["id"])}</strong></a>'
                f'{" — " + e(who) if who else ""}{cvss}{added}. {e(text[:300])}</li>')

    parts = ['<div id="static-feed" class="wrap">',
             f'<h2>Latest vulnerability intelligence</h2><p>Snapshot generated {e(meta.get("updated", ""))}. '
             f'Tracking {e(meta.get("items", len(items)))} CVEs, including {e(meta.get("kev", len(kev)))} entries in the CISA Known Exploited Vulnerabilities catalog.</p>',
             "<h3>Recently added to CISA KEV</h3><ul>" + "".join(li(i) for i in kev) + "</ul>"]
    if crit:
        parts.append("<h3>Recent critical (CVSS 9.0+) vulnerabilities</h3><ul>" + "".join(li(i) for i in crit) + "</ul>")
    if advs:
        parts.append("<h3>Latest security advisories</h3><ul>" + "".join(
            f'<li><a href="{e(a["url"])}" rel="noopener">{e(a["title"])}</a> ({e(a["source"])}, {e(a["date"])})</li>' for a in advs) + "</ul>")
    parts.append("</div>")
    graph = {"@context": "https://schema.org", "@type": "ItemList", "name": "Recently added CISA KEV vulnerabilities",
             "itemListElement": [{"@type": "ListItem", "position": n + 1, "name": i["id"] + (f" — {i.get('vendor')} {i.get('product')}" if i.get("vendor") else ""),
                                  "url": href(i) if href(i).startswith("http") else SITE + href(i)} for n, i in enumerate(kev)]}
    with open("_includes/threat-intel-static.html", "w") as f:
        f.write("\n".join(parts) + "\n" + ld(graph) + "\n")


def hub():
    items = load("assets/data/ai-sec-hub/items.json", [])
    brief = load("assets/data/ai-sec-hub/briefing.json", {})
    meta = load("assets/data/ai-sec-hub/meta.json", {})
    names = {"aisec": "AI Security", "ai": "Artificial Intelligence", "cyber": "Cybersecurity"}
    parts = ['<div id="static-feed" class="wrap">', f'<h2>Today in AI and cybersecurity</h2><p>Snapshot generated {e(meta.get("updated", ""))}.</p>']
    flat = []
    for tab in ("aisec", "ai", "cyber"):
        parts.append(f"<h3>{names[tab]}</h3>")
        if brief.get(tab):
            parts.append("<ul>" + "".join(f"<li>{e(b)}</li>" for b in brief[tab]) + "</ul>")
        top = [i for i in items if tab in i["tabs"] and i["kind"] in ("news", "blog", "paper")][:8]
        parts.append("<ul>" + "".join(
            f'<li><a href="{e(i["url"])}" rel="noopener">{e(i["title"])}</a> ({e(i["source"])}, {e(i["date"])}). {e(i.get("sum") or i.get("desc", "")[:200])}</li>' for i in top) + "</ul>")
        if tab == "aisec":
            flat = top
    repos = [i for i in items if i["kind"] == "repo" and "aisec" in i["tabs"]][:8]
    if repos:
        parts.append("<h3>Trending AI-security GitHub projects</h3><ul>" + "".join(
            f'<li><a href="{e(r["url"])}" rel="noopener">{e(r["title"])}</a> ★ {e(r.get("stars"))}. {e(r.get("desc", ""))}</li>' for r in repos) + "</ul>")
    parts.append("</div>")
    graph = {"@context": "https://schema.org", "@type": "ItemList", "name": "Latest AI security news, papers and blogs",
             "itemListElement": [{"@type": "ListItem", "position": n + 1, "name": i["title"], "url": i["url"]} for n, i in enumerate(flat)]}
    with open("_includes/ai-sec-hub-static.html", "w") as f:
        f.write("\n".join(parts) + "\n" + ld(graph) + "\n")


if __name__ == "__main__":
    import sys
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("threat", "all"):
        threat_intel()
    if which in ("hub", "all"):
        hub()
    print("static includes written", dt.date.today())
