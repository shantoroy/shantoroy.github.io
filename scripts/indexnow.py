#!/usr/bin/env python3
"""Notify IndexNow (Bing, Yandex, etc.) about the main pages and content changed in the last commit."""
import json
import re
import subprocess
import urllib.request

HOST = "shantoroy.com"
KEY = "54ec44d1dc96d163247e5847bd732fde"
MAIN = ["/", "/threat-intel/", "/threat-intel/reports/", "/ai-sec-hub/", "/blog/", "/llms.txt"]


def changed_urls():
    try:
        files = subprocess.run(["git", "diff", "--name-only", "HEAD~1", "HEAD"], capture_output=True, text=True).stdout.split()
    except OSError:
        return []
    out = []
    for f in files:
        if f.endswith((".md", ".html")) and (f.startswith(("threat-intel/", "_posts/"))):
            m = re.search(r'^permalink:\s*"?([^"\n]+)"?', open(f).read(4000), re.M) if _exists(f) else None
            if m:
                out.append(m.group(1).strip())
    return out


def _exists(f):
    try:
        open(f).close()
        return True
    except OSError:
        return False


def main():
    urls = [f"https://{HOST}{p}" for p in dict.fromkeys(MAIN + changed_urls())][:200]
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print("IndexNow", r.status, len(urls), "urls")
    except Exception as exc:  # never fail the workflow over a ping
        print("IndexNow skipped:", exc)


if __name__ == "__main__":
    main()
