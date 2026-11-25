#!/usr/bin/env python3
"""AI & Cybersecurity hub: aggregates news, blogs, arXiv papers, community posts and GitHub repos.

Items are tagged into three tabs (ai, cyber, aisec), top items get AI summaries (Copilot CLI),
and a short daily briefing per tab is generated. Output: assets/data/ai-sec-hub/*.json
Only titles, short snippets and AI-written summaries are stored; everything links to the source.
"""
import datetime as dt
import email.utils
import html
import json
import os
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(__file__))
from threat_intel import ask_ai, http, log, parse_json_array  # noqa: E402

DATA = "assets/data/ai-sec-hub"
NOW = dt.datetime.now(dt.timezone.utc)
AI_MAX = int(os.environ.get("AI_MAX", "30"))
AI_BATCH = 8
GH_HEADERS = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {}
NS = {"a": "http://www.w3.org/2005/Atom"}

# name, url, kind, hint (tabs always applied; extra tabs come from keyword matching)
FEEDS = [
    ("The Hacker News", "https://feeds.feedburner.com/TheHackersNews", "news", "cyber"),
    ("BleepingComputer", "https://www.bleepingcomputer.com/feed/", "news", "cyber"),
    ("Dark Reading", "https://www.darkreading.com/rss.xml", "news", "cyber"),
    ("SecurityWeek", "https://www.securityweek.com/feed/", "news", "cyber"),
    ("Krebs on Security", "https://krebsonsecurity.com/feed/", "news", "cyber"),
    ("The Record", "https://therecord.media/feed", "news", "cyber"),
    ("Schneier on Security", "https://www.schneier.com/feed/atom/", "blog", "cyber"),
    ("SANS ISC", "https://isc.sans.edu/rssfeed.xml", "blog", "cyber"),
    ("Google Security Blog", "https://feeds.feedburner.com/GoogleOnlineSecurityBlog", "blog", "cyber"),
    ("Microsoft Security", "https://www.microsoft.com/en-us/security/blog/feed/", "blog", "cyber"),
    ("Unit 42", "https://feeds.feedburner.com/Unit42", "blog", "cyber"),
    ("Cisco Talos", "https://blog.talosintelligence.com/rss/", "blog", "cyber"),
    ("Project Zero", "https://googleprojectzero.blogspot.com/feeds/posts/default", "blog", "cyber"),
    ("Trail of Bits", "https://blog.trailofbits.com/feed/", "blog", "cyber"),
    ("MIT Technology Review", "https://www.technologyreview.com/topic/artificial-intelligence/feed", "news", "ai"),
    ("VentureBeat", "https://venturebeat.com/category/ai/feed/", "news", "ai"),
    ("The Verge", "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml", "news", "ai"),
    ("TechCrunch", "https://techcrunch.com/category/artificial-intelligence/feed/", "news", "ai"),
    ("OpenAI", "https://openai.com/news/rss.xml", "blog", "ai"),
    ("Google DeepMind", "https://deepmind.google/blog/rss.xml", "blog", "ai"),
    ("Hugging Face", "https://huggingface.co/blog/feed.xml", "blog", "ai"),
    ("NVIDIA Technical Blog", "https://developer.nvidia.com/blog/feed/", "blog", "ai"),
    ("Simon Willison", "https://simonwillison.net/atom/everything/", "blog", "ai"),
    ("Simon Willison (prompt injection)", "https://simonwillison.net/tags/prompt-injection.atom", "blog", "aisec"),
    ("Embrace The Red", "https://embracethered.com/blog/index.xml", "blog", "aisec"),
    ("OWASP GenAI", "https://genai.owasp.org/feed/", "blog", "aisec"),
    ("Lobsters · security", "https://lobste.rs/t/security.rss", "community", "cyber"),
    ("Lobsters · AI", "https://lobste.rs/t/ai.rss", "community", "ai"),
    ("Lobsters · ML", "https://lobste.rs/t/ml.rss", "community", "ai"),
]
# Max age in days per kind before an item is dropped
RETENTION = {"news": 7, "blog": 21, "community": 7, "paper": 10}
MAX_PER_SOURCE = 12

AI_RE = re.compile(
    r"\b(AI|A\.I\.|LLMs?|GenAI|generative AI|gpt-?\d*|chatgpt|openai|anthropic|claude|gemini|copilot|"
    r"agentic|AI agents?|MCP|model context protocol|machine learning|deep learning|neural networks?|"
    r"foundation models?|retrieval[- ]augmented|deepfakes?|language models?|fine-?tuning)\b", re.I)
SEC_RE = re.compile(
    r"\b(security|secure|vulnerabilit\w+|exploit\w*|CVE-\d+|malware|ransomware|phishing|attack\w*|"
    r"threats?|breach\w*|hack\w*|adversar\w+|jailbreak\w*|backdoor\w*|poison\w*|zero-?day|"
    r"red[- ]team\w*|cyber\w*|infosec|botnet|spyware|malicious|trojan)\b", re.I)
AISEC_RE = re.compile(
    r"(prompt injection|jailbreak|LLM (?:security|safety|attack|vulnerab)|AI (?:security|safety|red[- ]team)|"
    r"red[- ]team\w* (?:of )?(?:LLM|AI|language model)|adversarial (?:attack|example|robustness|prompt)|"
    r"model (?:poisoning|extraction|inversion|stealing)|data poisoning|backdoor\w* (?:in )?(?:LLM|model|neural)|"
    r"agent(?:ic)? (?:security|attack|safety)|MCP (?:security|server|attack|vulnerab)|guardrails?|"
    r"membership inference|trojan\w* (?:model|neural)|safety alignment|OWASP.*LLM|shadow AI|AI-powered (?:attack|malware|phishing)|"
    r"deepfake|AI agents? .{0,40}(?:exploit|hijack|vulnerab))", re.I)


def clean(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t or ""))).strip()


def parse_date(s):
    if not s:
        return None
    try:
        d = email.utils.parsedate_to_datetime(s)
    except (TypeError, ValueError):
        try:
            d = dt.datetime.fromisoformat(s.strip().replace("Z", "+00:00"))
        except ValueError:
            return None
    return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)


def classify(title, desc, hint):
    """Return the tabs an item belongs to: ai, cyber and/or aisec (AI x security)."""
    text = f"{title} {desc}"
    ai, sec = bool(AI_RE.search(text)), bool(SEC_RE.search(text))
    tabs = set()
    if hint == "ai" or ai:
        tabs.add("ai")
    if hint == "cyber" or sec:
        tabs.add("cyber")
    if hint == "aisec" or AISEC_RE.search(text) or (ai and sec):
        tabs.update({"aisec", "ai", "cyber"})
    # AI-only sources shouldn't land in cyber just because of one generic word
    if hint == "ai" and "aisec" not in tabs and not sec:
        tabs.discard("cyber")
    if hint == "cyber" and "aisec" not in tabs and not ai:
        tabs.discard("ai")
    return sorted(tabs)


def mk(title, url, source, kind, date, desc, hint, **extra):
    tabs = classify(title, desc, hint)
    if not tabs or not url or not title:
        return None
    return {"id": url, "title": title[:220], "url": url, "source": source, "kind": kind,
            "date": date.date().isoformat() if date else NOW.date().isoformat(),
            "desc": desc[:320], "tabs": tabs, **extra}


# ---------------------------------------------------------------- collectors
def feed_items(name, url, kind, hint):
    root = ET.fromstring(http(url, retries=2, timeout=30))
    out = []
    for it in root.iter("item"):
        link = (it.findtext("link") or "").strip()
        out.append(mk(clean(it.findtext("title")), link, name, kind, parse_date(it.findtext("pubDate")),
                      clean(it.findtext("description")), hint))
    for e in root.findall("a:entry", NS):
        ln = next((x.get("href") for x in e.findall("a:link", NS) if x.get("rel") in (None, "alternate")), "")
        summary = e.findtext("a:summary", namespaces=NS) or e.findtext("a:content", namespaces=NS)
        out.append(mk(clean(e.findtext("a:title", namespaces=NS)), ln, name, kind,
                      parse_date(e.findtext("a:published", namespaces=NS) or e.findtext("a:updated", namespaces=NS)),
                      clean(summary), hint))
    return [o for o in out if o][:MAX_PER_SOURCE]


def collect_feeds():
    out = []
    for name, url, kind, hint in FEEDS:
        try:
            got = feed_items(name, url, kind, hint)
            log(f"feed {name}: {len(got)}")
            out += got
        except Exception as exc:
            log(f"warn: feed {name}: {exc}")
    return out


def collect_hn():
    out, seen = [], set()
    since = int((NOW - dt.timedelta(days=7)).timestamp())
    for q, hint in [("LLM security", "aisec"), ("prompt injection", "aisec"), ("AI agents security", "aisec"),
                    ("cybersecurity", "cyber"), ("vulnerability", "cyber"), ("ransomware", "cyber"),
                    ("LLM", "ai"), ("AI model", "ai"), ("OpenAI", "ai")]:
        url = ("https://hn.algolia.com/api/v1/search?tags=story&hitsPerPage=12&query=" + urllib.parse.quote(q)
               + f"&numericFilters=created_at_i>{since},points>=10")
        try:
            for h in json.loads(http(url, retries=2, timeout=30))["hits"]:
                link = h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}"
                if link in seen:
                    continue
                seen.add(link)
                o = mk(h["title"], link, "Hacker News", "community", parse_date(h["created_at"]), "", hint,
                       points=h.get("points"), discuss=f"https://news.ycombinator.com/item?id={h['objectID']}")
                if o:
                    out.append(o)
        except Exception as exc:
            log(f"warn: hn {q}: {exc}")
    log(f"hn: {len(out)}")
    return out


ARXIV_QUERIES = [
    ("cyber", "cat:cs.CR", 40),
    ("ai", "(cat:cs.AI OR cat:cs.CL) AND (abs:LLM OR abs:agents OR abs:reasoning)", 40),
    ("", '(cat:cs.CR OR cat:cs.LG OR cat:cs.AI OR cat:cs.CL) AND (abs:"prompt injection" OR abs:jailbreak '
              'OR abs:"adversarial attack" OR abs:"red teaming" OR abs:"LLM security" OR abs:backdoor '
              'OR abs:"agent security" OR abs:"data poisoning")', 40),
]


def collect_arxiv():
    out, seen = [], set()
    for hint, q, n in ARXIV_QUERIES:
        url = ("https://export.arxiv.org/api/query?sortBy=submittedDate&sortOrder=descending&max_results=%d&search_query=%s"
               % (n, urllib.parse.quote(q)))
        try:
            root = ET.fromstring(http(url, retries=3, timeout=60))
            for e in root.findall("a:entry", NS):
                link = e.findtext("a:id", namespaces=NS).strip().replace("http://", "https://")
                if link in seen:
                    continue
                seen.add(link)
                authors = [a.findtext("a:name", namespaces=NS) for a in e.findall("a:author", NS)]
                who = ", ".join(authors[:3]) + (" et al." if len(authors) > 3 else "")
                cat = e.find("{http://arxiv.org/schemas/atom}primary_category")
                o = mk(clean(e.findtext("a:title", namespaces=NS)), link, "arXiv", "paper",
                       parse_date(e.findtext("a:published", namespaces=NS)),
                       clean(e.findtext("a:summary", namespaces=NS)), hint,
                       authors=who, cat=cat.get("term") if cat is not None else "")
                if o:
                    o["desc"] = o["desc"][:320]
                    out.append(o)
        except Exception as exc:
            log(f"warn: arxiv {q[:30]}: {exc}")
        time.sleep(4)  # arXiv asks for one request every 3 seconds
    log(f"arxiv: {len(out)}")
    return out


def date_ago(days):
    return (NOW - dt.timedelta(days=days)).date().isoformat()


REPO_QUERIES = [
    ("aisec", "topic:llm-security", f"pushed:>{date_ago(30)} stars:>30"),
    ("aisec", "topic:prompt-injection", f"pushed:>{date_ago(30)} stars:>20"),
    ("aisec", "topic:ai-security", f"pushed:>{date_ago(30)} stars:>30"),
    ("aisec", "topic:ai-red-teaming", f"pushed:>{date_ago(60)} stars:>20"),
    ("aisec", "topic:mcp-security", f"pushed:>{date_ago(60)} stars:>10"),
    ("aisec", "topic:llm-security", f"created:>{date_ago(45)} stars:>5"),
    ("cyber", "topic:cybersecurity", f"pushed:>{date_ago(14)} stars:>500"),
    ("cyber", "topic:pentesting", f"pushed:>{date_ago(14)} stars:>300"),
    ("cyber", "topic:threat-hunting", f"pushed:>{date_ago(30)} stars:>100"),
    ("cyber", "topic:security", f"created:>{date_ago(30)} stars:>50"),
    ("ai", "topic:ai-agents", f"created:>{date_ago(21)} stars:>100"),
    ("ai", "topic:llm", f"created:>{date_ago(14)} stars:>150"),
    ("ai", "topic:generative-ai", f"created:>{date_ago(21)} stars:>100"),
]


def collect_repos():
    repos = {}
    for hint, topic, extra in REPO_QUERIES:
        q = urllib.parse.quote(f"{topic} {extra}")
        try:
            data = json.loads(http(f"https://api.github.com/search/repositories?q={q}&sort=stars&order=desc&per_page=10",
                                   GH_HEADERS, retries=2, timeout=30))
            for r in data.get("items", []):
                o = repos.setdefault(r["html_url"], {
                    "id": r["html_url"], "title": r["full_name"], "url": r["html_url"], "source": "GitHub",
                    "kind": "repo", "date": (r.get("pushed_at") or "")[:10] or NOW.date().isoformat(),
                    "desc": clean(r.get("description"))[:240], "tabs": [], "stars": r["stargazers_count"],
                    "lang": r.get("language") or ""})
                if hint not in o["tabs"]:
                    o["tabs"].append(hint)
                if hint == "aisec":
                    for t in ("ai", "cyber"):
                        if t not in o["tabs"]:
                            o["tabs"].append(t)
        except Exception as exc:
            log(f"warn: repos {topic}: {exc}")
        time.sleep(2.2)
    out = sorted(repos.values(), key=lambda r: -r["stars"])
    for r in out:
        r["tabs"] = sorted(set(r["tabs"]) | set(classify(r["title"], r["desc"], "")))
    log(f"repos: {len(out)}")
    return out


# ---------------------------------------------------------------- AI
def summarize(store):
    cutoff = date_ago(3)
    kind_rank = {"blog": 0, "news": 0, "paper": 1, "community": 2}
    todo = [i for i in store.values()
            if i["kind"] in kind_rank and "sum" not in i and i["date"] >= cutoff and (i["desc"] or i["kind"] == "paper")]
    todo.sort(key=lambda i: (0 if "aisec" in i["tabs"] else 1, kind_rank[i["kind"]], i["date"]), reverse=False)
    papers = 0
    picked = []
    for i in todo:
        if i["kind"] == "paper":
            if papers >= 10:
                continue
            papers += 1
        picked.append(i)
        if len(picked) >= AI_MAX:
            break
    log(f"ai: summarizing {len(picked)} items")
    for n in range(0, len(picked), AI_BATCH):
        batch = picked[n:n + AI_BATCH]
        payload = [{"id": i["id"], "title": i["title"], "source": i["source"], "text": i["desc"]} for i in batch]
        prompt = (
            "You curate an AI and cybersecurity news hub. For EACH item below, using ONLY the given title and text, "
            "return a JSON array (no prose, no code fences) of objects with keys \"id\" (unchanged) and "
            "\"sum\" (one original-wording sentence, max 35 words, saying what it is and why a security or AI "
            "practitioner should care). Do not copy sentences verbatim, do not invent facts.\n\n"
            + json.dumps(payload, indent=1))
        for r in parse_json_array(ask_ai(prompt)):
            if isinstance(r, dict) and r.get("id") in store and r.get("sum"):
                store[r["id"]]["sum"] = str(r["sum"]).strip()[:300]


def briefing(store, old):
    recent = [i for i in store.values() if i["date"] >= date_ago(2) and i["kind"] != "repo"]
    payload = {}
    for tab in ("aisec", "ai", "cyber"):
        top = sorted((i for i in recent if tab in i["tabs"]),
                     key=lambda i: (0 if "sum" in i else 1, i["kind"] == "community", i["date"]), reverse=False)[:18]
        payload[tab] = [{"title": i["title"], "source": i["source"], "note": i.get("sum", "")} for i in top]
    if not any(payload.values()):
        return old
    prompt = (
        "Write a short daily briefing for an AI and cybersecurity news hub using ONLY the headlines below. "
        "Return a single JSON object (no prose, no code fences) with keys \"aisec\", \"ai\", \"cyber\"; each value is "
        "an array of 3 concise bullet strings (max 28 words each, original wording, no invented facts) capturing the "
        "main themes today. \"aisec\" = security of AI/LLMs/agents, \"ai\" = AI industry and research, "
        "\"cyber\" = general cybersecurity.\n\n" + json.dumps(payload, indent=1))
    out = ask_ai(prompt)
    try:
        a, b = out.find("{"), out.rfind("}")
        data = json.loads(out[a:b + 1])
        clean_data = {k: [str(x)[:260] for x in data[k]][:4] for k in ("aisec", "ai", "cyber") if isinstance(data.get(k), list)}
        if clean_data:
            return {"date": NOW.date().isoformat(), **clean_data}
    except Exception as exc:
        log(f"briefing failed: {exc}")
    return old


# ---------------------------------------------------------------- main
def load(name, default):
    try:
        with open(f"{DATA}/{name}") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def main():
    os.makedirs(DATA, exist_ok=True)
    old = {i["id"]: i for i in load("items.json", [])}
    fresh = collect_feeds() + collect_hn() + collect_arxiv()
    repos = collect_repos()

    store = {}
    for i in list(old.values()) + fresh:
        if i["kind"] == "repo":
            continue
        prev = store.get(i["id"], {})
        store[i["id"]] = {**prev, **i, **({"sum": prev["sum"]} if "sum" in prev and "sum" not in i else {})}
    for i in list(store.values()):
        if i["date"] < date_ago(RETENTION.get(i["kind"], 7)):
            del store[i["id"]]
    if not store and not repos:
        log("nothing collected; keeping existing data")
        return 1

    summarize(store)
    brief = briefing(store, load("briefing.json", {}))
    for r in repos:
        store[r["id"]] = r

    rows = sorted(store.values(), key=lambda i: (i["date"], i.get("stars", 0)), reverse=True)
    with open(f"{DATA}/items.json", "w") as f:
        f.write("[\n" + ",\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows) + "\n]\n")
    with open(f"{DATA}/briefing.json", "w") as f:
        json.dump(brief, f, ensure_ascii=False, indent=1)
    counts = {k: sum(1 for r in rows if r["kind"] == k) for k in ("news", "blog", "paper", "community", "repo")}
    with open(f"{DATA}/meta.json", "w") as f:
        json.dump({"updated": NOW.strftime("%Y-%m-%d %H:%M UTC"), "counts": counts,
                   "tabs": {t: sum(1 for r in rows if t in r["tabs"]) for t in ("aisec", "ai", "cyber")}}, f, indent=1)
    log(f"done: {len(rows)} items {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
