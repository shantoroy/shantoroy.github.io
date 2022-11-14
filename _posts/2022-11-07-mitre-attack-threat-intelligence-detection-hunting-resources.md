---
layout: single
title: "MITRE ATT&CK Resources for Threat Intelligence and Hunting"
header:
  image: "https://live.staticflickr.com/65535/52498413834_b36a34e7ae_o.png"
  teaser: "https://live.staticflickr.com/65535/52498413834_b36a34e7ae_o.png"
categories:
  - ATT&CK
tags:
  - ATT&CK
  - MITRE
  - Threat Intelligence
  - Threat Hunting
  - STIX
  - TAXII
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
---


MITRE ATT&CK has been widely used for threat intelligence, threat detection and hunting, risk mitigation, and security product development.

The MITRE ATT&CK framework includes matrix for enterprise, ICS, and Mobile, etc. The matrices are organized and divided initially by $14$ tactics used by adversaries. Then each tactics list a number of techniques and sub-techniques.

The $14$ tactics are: Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control (C2), Exfiltration, and Impact.

In this post, I will list important resources related to the ATT&CK framework.

1. [ATT&CK Matrices](https://attack.mitre.org/matrices/enterprise/) is the official knowledge base of adverasial Tactics, Techniques, and Procedures (TTPs).
2. [Threat Intelligence Repository on GitHub](https://github.com/mitre/cti) contains the ATT&CK and CAPEC datasets expressed in STIX 2.0. Here, Structured Threat Information Expression (STIX) is a language that is used for sharing and exchanging threat intelligence information.
3. A python module named [mitreattack-python](https://pypi.org/project/mitreattack-python/1.2.0/) is available for using python-based tools for working with ATT&CK. You can also locate it on [this GitHub Repository](https://github.com/mitre-attack/mitreattack-python).
4. Another python module named [pyattck](https://pypi.org/project/pyattck/) can be used to interact with the ATT&CK framework. Interestingly, this module can pull latest data from the following locations:
	-   enterprise_attck_json="[https://swimlane-pyattck.s3.us-west-2.amazonaws.com/merged_enterprise_attck_v1.json](https://swimlane-pyattck.s3.us-west-2.amazonaws.com/merged_enterprise_attck_v1.json)"
	-   pre_attck_json="[https://swimlane-pyattck.s3.us-west-2.amazonaws.com/merged_pre_attck_v1.json](https://swimlane-pyattck.s3.us-west-2.amazonaws.com/merged_pre_attck_v1.json)"
	-   mobile_attck_json="[https://swimlane-pyattck.s3.us-west-2.amazonaws.com/merged_mobile_attck_v1.json](https://swimlane-pyattck.s3.us-west-2.amazonaws.com/merged_mobile_attck_v1.json)"
	-   ics_attck_json="[https://swimlane-pyattck.s3.us-west-2.amazonaws.com/merged_ics_attck_v1.json](https://swimlane-pyattck.s3.us-west-2.amazonaws.com/merged_ics_attck_v1.json)"
	-   nist_controls_json="[https://swimlane-pyattck.s3.us-west-2.amazonaws.com/merged_nist_controls_v1.json](https://swimlane-pyattck.s3.us-west-2.amazonaws.com/merged_nist_controls_v1.json)"
	-   generated_nist_json="[https://swimlane-pyattck.s3.us-west-2.amazonaws.com/attck_to_nist_controls.json](https://swimlane-pyattck.s3.us-west-2.amazonaws.com/attck_to_nist_controls.json)"
5. Python scripts and utilities for working with ATT&CK, are available on [this `attack-scripts` repository](https://github.com/mitre-attack/attack-scripts).
6. Another Python module [attackcti](https://github.com/mitre-attack/mitreattack-python) provides options for classes and functions from [cti-python-stix2](https://github.com/oasis-open/cti-python-stix2) and [cti-taxii-client](https://github.com/oasis-open/cti-taxii-client) libraries.
7. Awesome Resources
	- [Awesome Mitre ATT&CK framework](https://github.com/infosecn1nja/awesome-mitre-attack) 
	- [Awesome Threat Detection and Hunting](https://github.com/0x4D31/awesome-threat-detection)
	- [Awesome Threat Intelligence](https://github.com/hslatman/awesome-threat-intelligence)
	- [Awesome IOCs](https://github.com/sroberts/awesome-iocs), IOC stands for Indicator of Compromise
8. The [Mitre Visualizer on Github](https://github.com/qeeqbox/mitre-visualizer) provides visualization of the ATT&CK TTPs.
9. The [Threat Hunter Playbook](https://github.com/OTRF/ThreatHunter-Playbook) shares detection logics and resources for detection-based developments. The objective is to help running detection logic against [security datasets](https://securitydatasets.com/) locally or remotely through [BinderHub](https://mybinder.readthedocs.io/en/latest/index.html). Details are available on the [Official Site](https://threathunterplaybook.com/intro.html).
10. A Info-Sec writer named [Roberto Rodriguez](https://medium.com/@cyb3rward0g) on Medium.com has good number of blog posts related to ATT&CK for threat hunting. You can follow his writings and work procedurs.
11. Talking about medium.com, you can follow a particular channel named [Open Threat Research](https://medium.com/threat-hunters-forge) for more posts related to ATT&CK. 
12. A new framework named [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT) has been developed to detect tactics, techniques; and combat threats.
13. A knowledge graph of security countermeasures, named [D3FEND](https://d3fend.mitre.org/) is developed for providing guidelined to the organizations about hardening, detection, isolation, deception, and eviction. D3FEND can be called the defender's version of ATT&CK knowledge base.


So far, these are the most important resources I have found so far. I will keep updating the list of resources. 

The `awesome` repositories are pretty good place to start since these curated lists present all varieties of resources available out there.

That's all for today. Until next time, cheers! :sunglasses: 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE4OTc2MjY4NF19
-->