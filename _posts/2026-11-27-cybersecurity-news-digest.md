---
layout: "single"
title: "Cybersecurity News Digest \u2013 November 27, 2026"
excerpt: "Daily summary of general cybersecurity news from BleepingComputer, Dark Reading, SecurityWeek, Simon Willison, The Hacker News, The Record and more."
permalink: "/cybersecurity-digest/2026-11-27/"
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

The day's themes: actively exploited flaws in edge and enterprise software (Mitel, Juniper, Drupal), supply-chain and developer-targeted attacks, and browser-extension abuse for stealing email and credentials.

## Mitel MiCollab Zero-Days Exploited, Possibly With AI Help
Accenture reports attackers abused MiCollab vulnerabilities before Mitel published its advisory, in what looks like an extortion campaign. The activity may have been AI-assisted, which could shorten exploitation timelines. CISA has since added five MiCollab flaws to its KEV catalog, as part of a batch of 10 that also covers Juniper, Vates and Danfoss products.

Source: [SecurityWeek](https://www.securityweek.com/mitel-micollab-zero-days-exploited-in-suspected-ai-assisted-attacks/)

## CISA Adds 10 Exploited Flaws to KEV
CISA added 10 vulnerabilities to its Known Exploited Vulnerabilities catalog, spanning Mitel, Juniper, Vates and Danfoss products. Five of them are the recently disclosed MiCollab bugs.

Source: [The Hacker News](https://thehackernews.com/2026/11/hackers-exploit-10-vulnerabilities.html)

## Critical Juniper Session Smart Conductor Flaw Exploited
Tracked as CVE-2026-103406, the vulnerability lets remote attackers execute arbitrary commands as root on Session Smart Conductor. It is being exploited in attacks, so patching should be prioritized.

Source: [SecurityWeek](https://www.securityweek.com/critical-juniper-session-smart-conductor-flaw-exploited-in-attacks/)

## Drupal Core Takeover Flaw Under Active Exploitation
Drupal warned of a "highly critical" core flaw, CVE-2026-136716, caused by improper checking of unusual or exceptional conditions. It is exploited in the wild. A related report says a previous installer patch left a gap that lets attackers take over some sites.

Source: [The Hacker News](https://thehackernews.com/2026/11/drupal-warns-of-new-highly-critical.html)

## 1Password Breach Exposes Customer Data and Source Code
1Password disclosed an incident in its backend systems. An attacker used a compromised employee GitHub account to push malicious code and steal customer records and internal source code. The company says customer vaults and other secrets were not accessed.

Source: [SecurityWeek](https://www.securityweek.com/1password-breach-exposes-customer-data-internal-source-code/)

## PolinRider Poisons 7,600+ GitHub Repositories
The North Korea-linked PolinRider campaign plants a Python loader in GitHub repositories, hidden in a small utils package or in conftest.py. SafeDep's report suggests the activity may date back to February 2025.

Source: [The Hacker News](https://thehackernews.com/2026/11/north-korea-linked-polinrider-poisons.html)

## 13 Malicious NuGet Packages Target .NET Developers
Researchers found 13 NuGet packages that pose as WinUI 3 and WPF button controls and are tied to fake take-home job assessments. Socket's researcher describes them as malware delivery traps aimed at Windows .NET developers.

Source: [The Hacker News](https://thehackernews.com/2026/11/13-malicious-nuget-packages-turn-fake.html)

## Extension-Based Email Theft: Remus and SYS010
The Remus infostealer uses a malicious Chrome extension posing as a Google Sheets add-on to steal Gmail messages. Its operators marketed this as a Gmail zero-day. Separately, a new SYS01 variant spread via Meta ads enrolls browsers into enterprise-style management to force-install a data-stealing extension targeting Gmail and Outlook.

Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/remus-malware-steals-gmail-messages-via-fake-google-sheets-extension/)

## "GoodGuys" Phishing Impersonates Brands for Paid Interviews
An ongoing campaign impersonates companies such as Google, Nvidia, Accenture and SpaceX. It uses fake paid expert interview and webinar invitations to steal corporate Google and Okta credentials.

Source: [BleepingComputer](https://www.bleepingcomputer.com/news/apple/fake-paid-expert-interviews-impersonate-brands-to-steal-google-logins/)

## Iranian "Volant Manticore" Targets Cyprus
A previously undocumented Iranian threat group is targeting Cypriot organizations in an intelligence-gathering effort for Tehran.

Source: [Dark Reading](https://www.darkreading.com/cyberattacks-data-breaches/cyprus-espionage-target-iranian-hackers)

## Takeaways
- Prioritize patching for KEV-listed edge and collaboration products (Mitel, Juniper, Drupal); exploitation is already underway.
- Treat developer ecosystems (GitHub, NuGet, job-assessment lures) and employee accounts as primary attack surface.
- Audit browser extensions and browser-management enrollment, and train staff on fake interview and webinar lures.
