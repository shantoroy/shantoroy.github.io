---
layout: single
title: "Passive Operating System Fingerprinting by Analyzing PCAP files"
header:
  image: "https://live.staticflickr.com/65535/51205416268_12b5776516_c.jpg"
  teaser: "https://live.staticflickr.com/65535/51205416268_12b5776516_c.jpg"
categories:
  - Security
tags:
  - Security
  - Tutorial
  - Fingerprinting
  - OS Fingerprinting
  - p0f
  - Wireshark
  - Passive Reconnaissance
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Attackers can perform active or passive reconnaissance once they compromise an asset within an internal network. Active reconnaissance (active scanning) provides better accuracy while performing reconnaissance although with a higher chance of being exposed to the Intrusion Detection Systems (IDS).

Therefore, most of the times, the attacker chooses to perform passive reconnaissance and `passive OS fingerprinting` is one of the most popular techniques. This is how an attacker can understand the underlying operating system of other network nodes that eventually may lead to vulnerability exposure.

In this post, we will see how to fingerprint OS using a passive fingerprinting tool named `p0f`.

First, we need a `PCAP` file. A PCAP file usually includes a lot of network traffics. You can obtain a lot of PCAP files online. For example,

* [CIC-IDS Dataset](http://205.174.165.80/CICDataset/CIC-IDS-2017/Dataset/PCAPs/)
* [Publicly available PCAP files](https://www.netresec.com/?page=pcapfiles)

or you can capture network traffics yourself using [Wireshark Packet Analyzer](https://www.wireshark.org/) tool. 

## Wireshark
You might be able to fingerprint OS using wireshark if captured http traffics. If not, you can do it manually using following steps:

1. First install the command-line version of wireshark named as `tshark`
	* Ubuntu: `sudo apt install -y tshark`
	* macOS: `brew install tshark`
you can find other options from their [official page](https://tshark.dev/setup/install/).
2. Capture only the first packet of a flow, which can be filtered using the `tcp.flags.syn eq 1` filter. Here, we will be capturing only `TTL` and `Window Size`. You can look for a few other features as well.
	```
	$ tshark -r <pcap_filename> -Y "tcp.flags.syn eq 1" -T fields -e ip.src -e ip.ttl -e tcp.window_size > <output_filename_with_path>
	```
	for example,
	```
	$ tshark -r thursday-100M.pcap -Y "tcp.flags.syn eq 1" -T fields -e ip.src -e ip.ttl -e tcp.window_size > /Users/roy/github/github_mrx/python_learn_teach/traffic_analysis/my_packet_analysis/dataset/tshark-log-thursday-100M.txt
	```
	See other options of `tshark` in the [official man page](https://www.wireshark.org/docs/man-pages/tshark.html).
3. open the `txt`/output file and match with existing databases. I'm adding an example database I found online.

|                OS                | TTL | Win Size |
|:--------------------------------:|:---:|:--------:|
|    Linux (kernel 2.4 and 2.6)    |  64 |   5840   |
|            Windows XP            | 128 |   65535  |
| Windows 7, Vista and Server 2008 | 128 |   8192   |
|      Cisco Router (IOS 12.4)     | 255 |   4128   |




## p0f
Well, if you want to use a better tool which won't cost you time for manual checking and incomplete information, you can use `p0f` which is my most favorite and recommended tool to use for fingerprinting.

It's quite easy to do so with only a single command and you can find all necessary information about a source node.

You can install `p0f` using the following commands:

* Ubuntu: `sudo apt-get install -y p0f`
* macOS: `brew install p0f`

Now run the following command and you will find your output in the output file.
```
$ sudo p0f -r <pcap_filename> -o <output_filename_with_path>
```
For example,
```
$ sudo p0f -r thursday-100M.pcap -o /Users/mrx/fop-log-thursday-100M.txt
```

That's it, have fun, cheers!







<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzOTk2NTMzNTBdfQ==
-->