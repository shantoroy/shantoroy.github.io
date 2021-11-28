---
layout: single
title: "Security Solutions for Enterprise: SIEM, EDR, SOAR"
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/51711452189_ba18a4a5c2_o.png"
categories:
  - Security
tags:
  - SIEM
  - SOAR
  - EDR
  - Threat Intelligence
  - Incident Response
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post introduces the security solutions for Enterprise Systems. I discuss the basic functionalities and key differences among SIEM, EDR, and SOAR."
---

In this post, I will discuss the most popular security solution frameworks used in the large organizations. The most common and widely used security solution frameworks are:
- Security Incident and Event Management (SIEM)
- Endpoint Detection and Response (EDR) 
- Security Orchestration, Automation and Response (SOAR)

Now, let's take a look at the basic functionalities and then we will learn the key differences between these frameworks.

## Security Incident and Event Management (SIEM)
SIEM targets to provide immediate response to a security incident by correlating user-, database-, application-, and network-based activities using network device-based logs or events.

### Logging Sources (Network Resources)
The source of logs depends on the network resources an organization have:

* Network Devices
	* Routers
	* Switches
	* Servers
	* Private Cloud resources
	* Desktops
	* Wireless Access Points
* Servers
	* Database
	* Web
	* Application
* Applications
	* Web
	* Microservices
	* SaaS Applications
	* Local/Global Services
* Security Resources
	* Intrusion Detection/Prevention Systems (IDS/IPS)
	* Antivirus and Anti-malware programs
	* Firewalls
	* Honeypots/ Decoys
	* Sandboxing/ Virtual Machines


### Process
* **Data Collection:** SIEM tools collect data and event logs from all sources (servers, operating systems, applications, IDS/IPS, etc.). The collected data may be filtered and processed for correlation eligibility. Example log data can be:
	* Threat Intelligence Reports
	* Malware Scan Reports
	* User Activities
	* Vulnerability Scan Report
	* Footprinting Logs

* **Security Profile:** Different profiles are created based on the pre-defined security incidents. Policies are updated on regular basis based on new data. These policies define the rules, alerts, and notifications for the whole monitoring and management system.

* **Data Correlation:** The collected logs and events are correlated to create new rules or update an existing rule.

* **Notifications and ALerts:** Based on the collected new data, notifications and alerts are sent to the administrator if something needs to be done. These notifications and alerts help ensuring fast response after an security incident. 

### Application of SIEM
* Incident response and forensics
* Early Threat Detection
* Real-time threat monitoring and immediate Response
* Integration of Firewall, Honeypots, IDS/IPS, and other security resources
* Orchestrated threat intelligence 



## Endpoint Detection and Response (EDR) 
EDR ensures safety measures for the endpoints by early detection and response. Endpoint security is necessary to keep the Advanced Persistent Threats at bay. APTs can stay hidden inside a network for months, even years. EDR can provide safety measures against these types of APTs.

The three primary components include:
* Detection
	* Behavior Analysis
	* Scanning Results
	* Signature/Pattern Matching
* Investigation
	* Root Cause
	* Attack Visualization
	* Enriched Alert Data
* Response
	* Automated Response on Discovery
	* Immediate response during investigation
	* Notifications and Alerts


## Security Orchestration, Automation and Response (SOAR)

SOAR has four main components:
* Security Orchestration 
* Automation
* Threat Intelligence
* Security Incident Response Platform

SOAR is a orchestrated management system for incident response. An example workflow may include:
* **Early Threat Detection:** Detect a particular threat in the system
* **Case Creation and Investigation:** An online case is generated and updated based on the logs, alerts, and notifications
* **Collaboration:** Different SecOps teams collaborate by dividing responsibilities among themselves based on expertised knowledge and skills
* **Response:** Countermeasures are taken based on investigation reports


## SIEM vs EDR vs SOAR
`SIEM` primarily focus on correlating data received from different types of sources, and creating an alert system. `EDR` on the other hand helps investigating attacks by utilizing end-point data and providing automated response. `SOAR` focuses on improving security function visibility by ensuring proper collaboration between sec-ops teams. SOAR is more people-oriented and can use third-party sources for threat intelligence. Also, SOAR is capable of integrating with cross-platform security and networking products.

## References
1. [Security Information and Event Management (SIEM) Solution & it’s importance](https://layots.com/security-information-and-event-management-siem-solution-its-importance/)
2. [A Beginner's Guide to EDR Security](https://www.fool.com/the-blueprint/edr/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjI0ODEyOTE4XX0=
-->