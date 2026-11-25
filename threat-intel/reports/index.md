---
layout: single
title: "Threat Intelligence Reports"
permalink: /threat-intel/reports/
excerpt: "Automatically generated daily and weekly vulnerability intelligence reports."
header:
  image: "https://live.staticflickr.com/65535/55672381423_3128d9aaf7_b.jpg"
  teaser: "https://live.staticflickr.com/65535/55672381423_3128d9aaf7_b.jpg"
---

Daily and weekly reports generated from CISA KEV, NVD and public security advisories, with AI-assisted summaries. [← Back to the dashboard](/threat-intel/)

{% assign weekly = site.pages | where_exp: "p", "p.report_type == 'weekly'" | sort: "report_date" | reverse %}
{% assign daily = site.pages | where_exp: "p", "p.report_type == 'daily'" | sort: "report_date" | reverse %}

## Weekly reports

{% for p in weekly %}- [{{ p.title }}]({{ p.url | relative_url }}) — {{ p.excerpt | strip_html | strip }}
{% else %}Weekly reports are published on Mondays.
{% endfor %}

## Daily reports

{% for p in daily %}- [{{ p.title }}]({{ p.url | relative_url }}) — {{ p.excerpt | strip_html | strip }}
{% else %}No reports yet.
{% endfor %}
