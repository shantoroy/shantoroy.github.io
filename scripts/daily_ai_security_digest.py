#!/usr/bin/env python3
"""Build a daily AI-security news digest post from RSS feeds, summarized with Copilot CLI."""
import datetime as dt
import email.utils
import html
import json
import os
import re
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET

FEEDS = {
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "BleepingComputer": "https://www.bleepingcomputer.com/feed/",
    "Dark Reading": "https://www.darkreading.com/rss.xml",
    "SecurityWeek": "https://www.securityweek.com/feed/",
    "Krebs on Security": "https://krebsonsecurity.com/feed/",
    "r/netsec": "https://www.reddit.com/r/netsec.rss",
}
KEYWORDS = re.compile(
    r"\b(AI|A\.I\.|LLMs?|GenAI|generative|agentic|agents?|MCP|model context|prompt injection|jailbreak|"
    r"copilot|chatgpt|openai|anthropic|claude|gemini|deepfake|machine learning|guardrails?|shadow AI)\b",
    re.I,
)
MAX_ITEMS = 15
UA = {"User-Agent": "Mozilla/5.0 (compatible; shantoroy.com digest bot)"}
NS = {"atom": "http://www.w3.org/2005/Atom"}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def clean(text):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", text or ""))).strip()


def parse_date(s):
    if not s:
        return None
    try:
        d = email.utils.parsedate_to_datetime(s)
    except (TypeError, ValueError):
        try:
            d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            return None
    return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)


def items(source, url):
    root = ET.fromstring(fetch(url))
    for it in root.iter("item"):
        yield source, clean(it.findtext("title")), (it.findtext("link") or "").strip(), \
            clean(it.findtext("description")), parse_date(it.findtext("pubDate"))
    for e in root.findall("atom:entry", NS):
        link = e.find("atom:link", NS)
        summary = e.findtext("atom:summary", namespaces=NS) or e.findtext("atom:content", namespaces=NS)
        yield source, clean(e.findtext("atom:title", namespaces=NS)), \
            link.get("href", "") if link is not None else "", clean(summary), \
            parse_date(e.findtext("atom:updated", namespaces=NS) or e.findtext("atom:published", namespaces=NS))


def collect(hours=30):
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=hours)
    found, seen = [], set()
    for source, url in FEEDS.items():
        try:
            for s, title, link, desc, when in items(source, url):
                if when and when >= cutoff and link not in seen and KEYWORDS.search(f"{title} {desc}"):
                    seen.add(link)
                    found.append({"source": s, "title": title, "url": link, "desc": desc[:600]})
        except Exception as exc:  # one broken feed must not kill the run
            print(f"warn: {source}: {exc}", file=sys.stderr)
    return found[:MAX_ITEMS * 2]


def summarize(entries):
    prompt = (
        "You write a daily AI-security news digest for a cybersecurity engineer's blog. "
        "Using ONLY the items below, write markdown with: a 2-3 sentence overview of the day's themes, "
        "then a section per notable story (## heading, 2-3 sentence original-wording summary, "
        "and a line 'Source: [name](url)'). Pick at most %d stories that are genuinely about AI/LLM/agent "
        "security or AI-enabled threats; skip the rest. Do not invent facts, do not quote articles at length. "
        "End with a '## Takeaways' list of 2-3 bullets. Do not include a top-level title or front matter.\n\n%s"
        % (MAX_ITEMS, json.dumps(entries, indent=1))
    )
    # Tools are disabled so feed text (untrusted) cannot trigger any actions
    out = subprocess.run(
        ["copilot", "-p", prompt, "-s", "--no-ask-user", "--available-tools="],
        capture_output=True, text=True, timeout=600, check=True,
    ).stdout.strip()
    if len(out) < 200:
        raise RuntimeError(f"unexpectedly short summary: {out!r}")
    return out


def main():
    today = dt.date.today().isoformat()
    path = f"_posts/{today}-ai-security-news-digest.md"
    if os.path.exists(path):
        print("post exists, skipping")
        return
    entries = collect()
    if len(entries) < 2:
        print("not enough AI-security items today, skipping")
        return
    body = summarize(entries)
    sources = ", ".join(sorted({e["source"] for e in entries}))
    front = f"""---
title: "AI Security News Digest – {dt.date.today().strftime('%B %-d, %Y')}"
excerpt: "Daily summary of AI and cybersecurity news from {sources}."
categories:
  - AI Security Digest
tags:
  - AI Security
  - Cybersecurity
  - News
  - Digest
comments: false
---

*Auto-generated daily digest of AI-security headlines. Summaries are AI-assisted; always check the linked sources.*

"""
    with open(path, "w") as f:
        f.write(front + body + "\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
