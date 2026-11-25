---
layout: "single"
title: "Cybersecurity News Digest \u2013 November 25, 2026"
excerpt: "Daily summary of general cybersecurity news from BleepingComputer, Cisco Talos, Dark Reading, SANS ISC, Schneier on Security, SecurityWeek and more."
permalink: "/cybersecurity-digest/2026-11-25/"
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

Today's digest is dominated by AI-assisted offensive activity hitting core security infrastructure, alongside critical virtualization patches and a wave of vendor and government breaches. Vishing-driven extortion and exposed admin interfaces also featured heavily.

## AI-Driven Attacks Hit Check Point Management Servers
GreyNoise, which tracks the actor as GT13, says an unidentified group used AI-driven offensive tooling against Check Point Security Management servers at 22 organizations. The campaign shows that automated exploitation of core security infrastructure is now something defenders should plan for.

Source: [The Hacker News](https://thehackernews.com/2026/11/hackers-compromise-24-check-point.html)

## Palo Alto Patches Fragnesia Flaw Used to Root Firewalls
Palo Alto Networks fixed Fragnesia, which a China-linked group chained with PHP2Shell in AI-assisted attacks on 25 servers. Firewall administrators should apply the patch promptly.

Source: [SecurityWeek](https://www.securityweek.com/palo-alto-networks-patches-fragnesia-flaw-used-to-root-firewalls/)

## Agentic AI Attack Tradecraft Comes Into Focus
Unit 42 documents campaigns where autonomous AI agents automated intrusions across platforms using ordinary tools, yet left distinctive traces defenders can hunt for. Cisco Talos separately compares publicly traceable 2026 OpenAI-linked swarm activity with early agentic attacks seen in the wild.

Source: [Unit 42](https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/)

## Drupal Flaw Found by Anthropic Scanner Is Exploited
A Drupal vulnerability discovered by an Anthropic scanner is now being exploited. CISA added it to the KEV catalog with a three-day federal patch deadline, signaling real urgency for Drupal operators.

Source: [SecurityWeek](https://www.securityweek.com/drupal-flaw-found-by-anthropic-scanner-exploited-in-attacks/)

## VMware Patches Critical vCenter and ESX Flaws
Broadcom fixed 23 flaws across VMware products, including CVE-2026-123903, a 9.8-rated vCenter authentication bypass that followed zero-day exploitation. Other bugs allow code execution on ESX hosts, so virtualization admins should prioritize updates.

Source: [The Hacker News](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html)

## Inception Vishing Gang Linked to ShinyHunters
Okta assesses that a ShinyHunters-associated voice-phishing cluster has rebranded as INCEPTION with a new leak site. BleepingComputer reports a large campaign aimed at stealing single sign-on credentials from global companies. ShinyHunters itself also claims to be back after arrests.

Source: [The Hacker News](https://thehackernews.com/2026/11/okta-links-shinyhunters-associated.html)

## Radware Breach Exposes Customer Cloud Keys
Attackers reached customer account details and cloud access keys through an internet-exposed internal Cloud WAF management API. Customers should rotate keys, and teams should audit their own exposed administrative interfaces.

Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)

## Rackspace Shuts Down Spot After Breach
Rackspace is closing its Spot cloud service after a breach exposed customer Kubernetes clusters and secrets. Users must migrate by December 8 and should rotate any credentials stored there.

Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/rackspace-shuts-down-spot-cloud-platform-after-security-breach/)

## Volant Manticore Uses IPFS-Based KuboShell Backdoor
A newly documented Iran-aligned espionage group targets Cyprus telecoms, airlines and infrastructure with KuboShell, a backdoor that uses IPFS for command-and-control. Defenders may want to monitor for decentralized-network C2 traffic.

Source: [The Hacker News](https://thehackernews.com/2026/11/iran-aligned-volant-manticore-uses-ipfs.html)

## Webworm Compiles Customized SoftEther VPN
The China-aligned Webworm group built SoftEther VPN from source with telltale artifacts removed, complicating detection. It's a reminder that signatures of known open source tools aren't enough.

Source: [Dark Reading](https://www.darkreading.com/perimeter/webworm-slithers-customized-softether-vpn)

## Takeaways
- Expect automated, AI-assisted exploitation of security appliances and management planes; patch Check Point, Palo Alto, VMware and Drupal exposures quickly.
- Audit internet-exposed admin APIs and rotate cloud keys and secrets held by affected vendors.
- Use phishing-resistant authentication and staff training to counter vishing-driven SSO theft.
