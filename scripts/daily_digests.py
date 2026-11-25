#!/usr/bin/env python3
"""Daily blog digests (AI, Cybersecurity, Threat Intelligence) built from data the dashboards already collect.

AI and Cybersecurity digests: one Copilot CLI call each over the AI/CyberSec Hub items.
Threat Intelligence digest: reuses the daily threat-intel report (no AI call), canonical-linked to it.
"""
import datetime as dt
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from threat_intel import ask_ai, fm, log  # noqa: E402

TODAY = dt.datetime.now(dt.timezone.utc).date()
HEADER_IMG = "https://live.staticflickr.com/65535/55672381423_3128d9aaf7_b.jpg"
MAX_STORIES = 10

DIGESTS = {
    "ai": dict(slug="ai-news-digest", path="ai-news-digest", name="AI News Digest", category="AI-Digest",
               tags=["AI", "LLM", "News", "Digest"], scope="the AI industry and research landscape (models, labs, tooling, agents, papers)"),
    "cyber": dict(slug="cybersecurity-news-digest", path="cybersecurity-digest", name="Cybersecurity News Digest",
                  category="Cybersecurity-Digest", tags=["Cybersecurity", "News", "Digest"],
                  scope="general cybersecurity (threats, breaches, vulnerabilities, research, tooling)"),
}


def hub_items(tab):
    with open("assets/data/ai-sec-hub/items.json") as f:
        items = json.load(f)
    since = str(TODAY - dt.timedelta(days=1))
    pool = [i for i in items if tab in i["tabs"] and i["date"] >= since and i["kind"] in ("news", "blog", "paper")]
    pool.sort(key=lambda i: (0 if i.get("sum") else 1, 0 if i["kind"] != "paper" else 1))
    papers = 0
    out = []
    for i in pool:
        if i["kind"] == "paper":
            papers += 1
            if papers > 4:
                continue
        out.append({"title": i["title"], "source": i["source"], "url": i["url"], "text": i.get("sum") or i.get("desc", "")[:400]})
        if len(out) >= 28:
            break
    return out


def post_path(slug):
    return f"_posts/{TODAY}-{slug}.md"


def write_post(path, front, body):
    with open(path, "w") as f:
        f.write(front + body.strip() + "\n")
    log("wrote", path)


def hub_digest(tab, cfg):
    path = post_path(cfg["slug"])
    if os.path.exists(path):
        return
    entries = hub_items(tab)
    if len(entries) < 4:
        log(f"{tab}: not enough items")
        return
    prompt = (
        f"You write a daily digest for a cybersecurity engineer's blog covering {cfg['scope']}. Using ONLY the items "
        f"below, write markdown with: a 2-3 sentence overview of the day's themes, then a section per notable story "
        f"(## heading, 2-3 sentence original-wording summary, and a line 'Source: [name](url)'). Pick at most "
        f"{MAX_STORIES} of the most significant stories and skip the rest. Do not invent facts or quote at length. "
        "End with a '## Takeaways' list of 2-3 bullets. Do not include a top-level title or front matter.\n\n"
        + json.dumps(entries, indent=1))
    body = ask_ai(prompt)
    if not body or len(body) < 300:
        log(f"{tab}: AI output missing or too short")
        return
    sources = ", ".join(sorted({e["source"] for e in entries})[:6])
    front = fm(layout="single", title=f"{cfg['name']} – {TODAY.strftime('%B %-d, %Y')}",
               excerpt=f"Daily summary of {cfg['scope'].split(' (')[0]} news from {sources} and more.",
               permalink=f"/{cfg['path']}/{TODAY}/", header={"image": HEADER_IMG, "teaser": HEADER_IMG},
               categories=[cfg["category"]], tags=cfg["tags"], toc=True, toc_label="Table of Contents", toc_icon="package")
    write_post(path, front, "*Auto-generated daily digest from the [AI/CyberSec Hub](/ai-sec-hub/). Summaries are AI-assisted; "
                            "always check the linked sources.*\n\n" + body)


def threat_digest():
    path = post_path("threat-intel-digest")
    report = f"threat-intel/reports/daily/{TODAY}.md"
    if os.path.exists(path) or not os.path.exists(report):
        return
    text = open(report).read()
    body = re.sub(r"\A---.*?---\n", "", text, count=1, flags=re.S)
    m = re.search(r'^excerpt:\s*"(.*)"', text, re.M)
    front = fm(layout="single", title=f"Vulnerability Digest – {TODAY.strftime('%B %-d, %Y')}",
               excerpt=(m.group(1) if m else "Daily CISA KEV, critical CVE and advisory summary."),
               permalink=f"/threat-intel-digest/{TODAY}/", canonical_url=f"https://shantoroy.com/threat-intel/reports/daily/{TODAY}/",
               header={"image": HEADER_IMG, "teaser": HEADER_IMG}, categories=["Threat-Intel-Digest"],
               tags=["Threat Intelligence", "CVE", "CISA KEV", "Digest"], toc=True, toc_label="Table of Contents", toc_icon="package")
    write_post(path, front, body + f"\n\n*Also published as a [report]({'/threat-intel/reports/daily/' + str(TODAY) + '/'}) on the [Threat Intelligence Dashboard](/threat-intel/).*")


def main():
    for tab, cfg in DIGESTS.items():
        try:
            hub_digest(tab, cfg)
        except Exception as exc:
            log(f"{tab} digest failed: {exc}")
    threat_digest()


if __name__ == "__main__":
    main()
