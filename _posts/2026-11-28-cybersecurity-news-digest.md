---
layout: "single"
title: "Cybersecurity News Digest \u2013 November 28, 2026"
excerpt: "Daily summary of general cybersecurity news from BleepingComputer, Dark Reading, Schneier on Security, SecurityWeek, The Hacker News, The Record and more."
permalink: "/cybersecurity-digest/2026-11-28/"
header:
  image: "https://live.staticflickr.com/65535/55672381423_3128d9aaf7_b.jpg"
  teaser: "https://live.staticflickr.com/65535/55672381423_3128d9aaf7_b.jpg"
categories:
  - "Cybersecurity-Digest"
tags:
  - "Cybersecurity"
  - "News"
  - "Digest"
toc: true
toc_label: "Table of Contents"
toc_icon: "package"
---
*Auto-generated daily digest from the [AI/CyberSec Hub](/ai-sec-hub/). Summaries are AI-assisted; always check the linked sources.*

Today's digest centers on software supply-chain compromises (SAP, Hex, trojanized installers), a wave of government and public-sector breaches, and fresh evidence that AI-driven attacks are succeeding against real targets. Several unpatched or actively exploited flaws in widely deployed infrastructure software also demand attention.

## Swiss Authorities Confirm AI-Assisted Attacks on Critical Infrastructure
Swiss cyber authorities report that intrusions driven by AI agents succeeded in four of five confirmed attacks, including against critical infrastructure operators. Agentic attacks are no longer theoretical, and defenders need to plan for them.

Source: [The Hacker News](https://thehackernews.com/2026/11/switzerland-confirms-ai-assisted.html)

## SAP Confirms Incident After Suspicious GitHub Activity
SAP says it acted urgently to protect customers after detecting suspicious activity in its environment. Reports indicate attackers used stolen employee tokens on GitHub to copy and possibly alter source code, though the full scope is unconfirmed.

Source: [SecurityWeek](https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/)

## Unpatched Cacti Zero-Day Gives Unauthenticated RCE
A zero-day in the Cacti network monitoring tool has been disclosed with a public proof-of-concept, tracked as 4HTTP2SHELL and 4HTTP2ROOT, and has no CVE yet. It allows unauthenticated attackers to run commands on vulnerable servers, reportedly via guest access in just four HTTP requests.

Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution/)

## NFS2ROOT: 12-Year-Old Linux Kernel NFS Flaw
A critical, long-lived vulnerability in the Linux kernel's NFS server, tracked as CVE-2026-99362, lets remote attackers gain root privileges. Anyone exposing NFS should check for patches.

Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-nfs2root-linux-flaw-can-let-attackers-gain-root-privileges/)

## Drupal Site-Takeover Flaw Exploited
The Drupal security team says attackers are exploiting a second critical vulnerability to breach and hijack unpatched sites. Patch promptly.

Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/drupal-warns-of-new-access-bypass-flaw-exploited-in-attacks/)

## Q-Dir and DesktopOK Downloads Trojanized
A supply-chain attack tampered with Q-Dir and DesktopOK installers distributed through the official SoftwareOK website, delivering remote access malware. Researchers indicate malicious files were generated in more than one download scenario, not only direct downloads from the official site.

Source: [The Hacker News](https://thehackernews.com/2026/11/hackers-trojanize-official-q-dir-and.html)

## Hex Package Manager Warns of Potential Breach
A vulnerability in hex.pm let attackers run commands on its web servers. No evidence of data modification was found, but database reads are not logged, so exposure can't be ruled out.

Source: [SecurityWeek](https://www.securityweek.com/hex-package-manager-warns-of-potential-data-breach/)

## Government Breaches Continue
The US Air Force's Cloud One platform was reportedly hacked, adding to recent attacks on US agencies. Japan's education ministry disclosed a procurement-system breach, and the UK's Department for Work and Pensions took services offline after a cyber incident.

Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/us-air-force-cloud-platform-reportedly-hacked-in-latest-federal-breach/)

## Vietnam-Linked Espionage Targets Southeast Asia
SOCRadar attributes a previously undocumented campaign to a suspected Vietnam-sponsored group targeting military, government, and legislative bodies in Southeast Asia. The apparent goal is intelligence on South China Sea defense matters.

Source: [The Hacker News](https://thehackernews.com/2026/11/suspected-vietnam-linked-hackers-target.html)

## Vinci RAT Delivered via Microsoft Store App
eSentire details an attack in which a Microsoft Store application delivered Vinci RAT, a remote access trojan. The chain starts with a redirect to a bogus site for a sniping tool.

Source: [The Hacker News](https://thehackernews.com/2026/11/microsoft-store-app-found-delivering.html)

## Takeaways
- Treat developer tokens and package/download channels as high-value targets; rotate and monitor them.
- Patch or mitigate exposed Cacti, Drupal, and NFS services quickly, since public PoCs and active exploitation are already in play.
- Plan detection and response for AI-agent-driven intrusions, not just human-paced attacks.
