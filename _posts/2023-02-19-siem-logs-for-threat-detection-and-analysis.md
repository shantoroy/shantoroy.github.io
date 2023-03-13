---
layout: single
title: "The Importance of SIEM Logs for Threat Intelligence, Detection, and Modeling"
excerpt:  "A Security Information and Event Management (SIEM) system collects log data from various sources within an organization's IT infrastructure. This data is used to provide actionable insights into potential security incidents. By analyzing SIEM logs, organizations can detect potential security threats, improve intrusion/threat detection, and enhance their threat modeling efforts. Read on to learn more about the importance of SIEM logs for threat intelligence, detection, and modeling."
seo_title:  "What Logs are Logged by the SIEM and How those logs are essential for Threat Intelligence/Modeling, Intrusion/Threat Detection"
seo_description:  "Learn how Security Information and Event Management (SIEM) system logs can help organizations detect and respond to security incidents, identify potential threats, and improve threat modeling efforts."
header:
  image: "https://live.staticflickr.com/65535/52711346998_b4c0a18047_o.png"
  teaser: "https://live.staticflickr.com/65535/52711346998_b4c0a18047_o.png"
categories:
  - Security
tags:
  - Security
  - SIEM
  - Threat Intelligence
  - Threat Modeling
  - Logging
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
---


In today's digital landscape, cyber threats are becoming more sophisticated, and organizations must keep up with the evolving security landscape to protect their assets. 

One of the most effective ways to detect and respond to security incidents is through a Security Information and Event Management (SIEM) system. 

A SIEM system collects and aggregates log data from various sources within an organization's IT infrastructure, and this data is used to provide actionable insights into potential security incidents. 

In this blog post, I will go through what logs are collected by the SIEM, and why they matter for threat intelligence, intrusion/threat detection, and threat modeling.

## Type of Logs collected by SIEM
A SIEM system collects logs from various sources, including network devices, servers, applications, and endpoints. 

These logs contain valuable information about the activity occurring within an organization's IT infrastructure, including user activity, system events, and network traffic. 

Here are the types of log data mentioned by [ManageEngine Log360](https://www.manageengine.com/log-management/siem/collecting-and-analysing-different-log-types.html)

* Perimeter device logs
* Windows event logs
* Endpoint logs
* Application logs
* Proxy logs
* IoT logs

Ther is also an order of which logs to give priority over another.  Order of priority mentioned by a [blog post](https://www.networksgroup.com/blog/threat-detection-logs-log-sources-and-analysis-make-all-the-difference) from `Networks Group`:


1.  IDS/IPS Alert Detections (Blocked & Allowed), Access, & Configuration Changes
2.  Advanced Endpoint Protection logs
3.  Firewall Logs/Connections, Access, Health, & Configuration Changes
4.  Domain Controller Authentication, User Creation and Modification
5.  Windows Event Application, Security, Powershell, & System
6.  DNS Requests
7.  Web Proxy Access/Errors
8.  Remote Access/VPN Authentication & Connections
9.  DHCP Lease Details
10.  Two-Factor Authentication Access Attempts
11.  Switching Logs & Netflow
12.  SNMP Audit Where Relevant


## Why these Logs matter
### Threat Intelligence
The logs collected by a SIEM system provide valuable information that can be used to identify potential threats to an organization's IT infrastructure. 

By analyzing authentication logs, for example, a SIEM system can detect brute force attacks, which can be a precursor to a more significant security incident. 

Firewall logs can be used to detect unauthorized access attempts and network traffic that may indicate a compromise.

Most importantly, these logs can effectively lead to Advanced Persistent Threat (APT) behaviors and overlapping of used tactics and techniques. Organizations often use the MITRE ATT&CK framework for further threat intelligence.
 

### Intrusion/Threat Detection
The logs collected by a SIEM system are also used to detect security incidents as they occur. For example, if a SIEM system detects a sudden increase in failed login attempts from a particular IP address, it may indicate that an attacker is attempting to gain unauthorized access to the network. 

By analyzing network traffic logs, a SIEM system can also detect suspicious patterns of traffic that may indicate a potential intrusion.

The traffic logs are quite important. Once, I analyzed some packets of ICIDS-2017 intrusion detection dataset. If you are interested in how to analyze packets, you can visit my [Github Repo](https://github.com/shantoroy/OS_fingerprinting_using-ML).

Different logs are also used for particular threat or procedure detection. The logs lead to certain use of techniques and tools and can reveal the behavioral match of an APT.

### Threat Modeling
The logs collected by a SIEM system can be used to improve an organization's threat modeling efforts. Threat modeling is the process of identifying potential threats to an organization's IT infrastructure and developing countermeasures to mitigate those threats. 

By analyzing the logs collected by a SIEM system, organizations can identify potential vulnerabilities and weaknesses in their IT infrastructure that may be exploited by attackers.

Threat modeling is more related to threat intelligence and often used for the same purposes. However, modeling requires further actions of behavior analysis, prediction, and pattern matching of these APTs.

## Concluding Remarks
SIEMs have become an essential part of the security analysts and engineers. Logs are meant to refer potential events and anomaly within the common pattern.

Through collecting the logs, a SIEM can potentially identify and model existing and new threats. Some of the actions can be taken instantly by a SIEM tool itself, and some requires the security analysts's attention.

By the way, currently, I am researching the MITRE ATT&CK framework, which is widely used as a recognized knowledge base of TTPs. I will update on my research soon. You can also read my other post on MITRE ATT&CK.

[MITRE ATT&CK Resources for Threat Intelligence and Hunting](https://shantoroy.com/att&ck/mitre-attack-threat-intelligence-detection-hunting-resources/)

That's all for today! Cheers!!! 😎
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk2OTY5NDMxLDU3NDk2NzA2NF19
-->