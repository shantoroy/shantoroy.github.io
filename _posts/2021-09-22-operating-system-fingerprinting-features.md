---
layout: single
title: "Operating System Fingerprinting Features in Captured Network Packets"
excerpt:  "Operating System Fingerprinting is a process of identifying the type of operating system running on a remote machine by analyzing the packets captured on the network. It can be useful for network administrators, security researchers, and attackers. In this blog post, we will explore the different features used for operating system fingerprinting in captured network packets."
seo_title:  "Operating System Fingerprinting Features in Captured Network Packets"
seo_description:  "Learn how to identify the type of operating system running on a remote machine by analyzing the packets captured on the network in this blog post. Explore the different features used for operating system fingerprinting and how it can be useful for network administrators, security researchers, and attackers."
header:
  image: "https://live.staticflickr.com/65535/52009031863_eb80d101d5_o.png"
  teaser: "https://live.staticflickr.com/65535/52009031863_eb80d101d5_o.png"
categories:
  - Security
tags:
  - Operating System
  - Tutorial
  - Fingerprinting
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



Different tools use different parameters for operating system fingerprinting. Even researchers also look for these features to identify certain operating systems.

The most common features are `TTL` and `Window_Size` that are implemented with different values across different operating systems. However, there are other features that are used to fingerprint an operating system.

Here, I listed these features from [this paper](https://ieeexplore.ieee.org/document/7346842).

1) ver: IP protocol version.
2) ittl: Initial TTL used by the OS.
3) olen: Length of IPv4 options or IPv6 extension headers.
4)  Maximum Segment Size (MSS): sometimes specified in TCP
Options for segmentation.
5) wsize: Window Size, a fixed random value or a
multiple of MSS, of MTU.
6) scale: Window Scaling factor, if specified in TCP Options.
7) olayout: Comma-delimited layout and ordering of TCP
Options. For example,
no-op option, maximum segment size, window scaling,
selective ACK permitted, timestamp.
8) quirks: Comma-delimited properties in IP or
TCP headers.
9) pclass: Payload size.

If you want to learn more about fingerprinting tools and processes, go through the following posts of mine:

[Passive Operating System Fingerprinting by Analyzing PCAP files](https://shantoroy.com/security/operating-system-fingerprinting/)

[Convert PCAP files to CSV for Network Traffic Analysis](https://shantoroy.com/networking/convert-pcap-to-csv-using-tshark/)

## References
1. [A Deception Based Approach for Defeating OS and Service Fingerprinting](https://ieeexplore.ieee.org/document/7346842)
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTIzOTIyNDQ0LC05Njk0Njk4MTddfQ==
-->