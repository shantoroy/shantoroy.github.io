---
layout: single
title: "Convert PCAP files to CSV for Network Traffic Analysis"
header:
  image: "https://live.staticflickr.com/65535/51206509290_743874dcd9_c.jpg"
  teaser: "https://live.staticflickr.com/65535/51206509290_743874dcd9_c.jpg"
categories:
  - Networking
tags:
  - Security
  - Tutorial
  - Fingerprinting
  - OS Fingerprinting
  - Computer Network
  - Traffic Analysis
  - Passive Reconnaissance
  - Wireshark
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Researchers working on Computer Network or Cyber Security often need to analyze network traffics. In that case, they use [Wireshark Packet Analyzer](https://www.wireshark.org/) or any other similar traffic analysis tools to capture and analyze packets.

However, if you want to perform data analysis, cleaning, modeling, or feature analysis and classification for the network traffic, you might want to convert the `PCAP` files into a `CSV` file.

Here, in this post we will see, how to convert PCAP files into CSV files easily.

## Collecting PCAP files
First, we need a `PCAP` file. A PCAP file usually includes a lot of network traffics. You can obtain a lot of PCAP files online. For example,

* [CIC-IDS Dataset](http://205.174.165.80/CICDataset/CIC-IDS-2017/Dataset/PCAPs/)
* [Publicly available PCAP files](https://www.netresec.com/?page=pcapfiles)

or you can capture network traffics yourself using [Wireshark Packet Analyzer](https://www.wireshark.org/) tool. 

## breaking down PCAP files
If the PCAP file is very large, you can divide that into smaller parts using the following command
```
$ tcpdump -r old_file -w new_files -C 10
```
For example:
```
python packet2df.py -file thursday-100M.pcap -o thursday-100M.csv
```

## Install `tshark`
You need to install the command-line version of wireshark named as `tshark`
	* Ubuntu: `sudo apt install -y tshark`
	* macOS: `brew install tshark`
you can find other options from their [official page](https://tshark.dev/setup/install/).

In macOS, if you have already installed wireshark, you might need to do the following if you don't find the command (check using `$ which tshark`) command.
```
$ ln -s /Applications/Wireshark.app/Contents/MacOS/tshark /usr/local/bin/tshark
```

## Convert PCAP to CSV
From the [official documentation](https://www.wireshark.org/docs/man-pages/tshark.html), we find:
```
tshark [-i <capture interface>|-][-f <capture filter>][-2][-r <infile>][-w <outfile>|-][options][<filter>]
```
Because, we are not capturing live traffic, we need to use `-r` to read a PCAP file.

Other options we need to use is `-T fields` to get the data in field format, `-E header=y` to print the header, `-E separator=,` to seperate the values using `,`, `-E quote=d` for using double quotation, `-E occurrence=f` to keep the first occurrence in case there is many (you can use `a` instead of `f` to keep all), and most importantly the required fields using `-e`.

In one of my work I used the following fields to create a CSV from a PCAP file.
```
$ tshark -r input.pcap -T fields -E header=y -E separator=, -E quote=d -E occurrence=f \
-e ip.version -e ip.hdr_len -e ip.tos -e ip.id -e ip.flags -e ip.flags.rb -e ip.flags.df \ 
-e ip.flags.mf -e ip.frag_offset -e ip.ttl -e ip.proto -e ip.checksum -e ip.src -e ip.dst \ 
-e ip.len -e ip.dsfield -e tcp.srcport -e tcp.dstport -e tcp.seq -e tcp.ack -e tcp.len \ 
-e tcp.hdr_len -e tcp.flags -e tcp.flags.fin -e tcp.flags.syn -e tcp.flags.reset \ 
-e tcp.flags.push -e tcp.flags.ack -e tcp.flags.urg -e tcp.flags.cwr -e tcp.window_size \ 
-e tcp.checksum -e tcp.urgent_pointer -e tcp.options.mss_val > output.csv
```

There are actually a lot of other fields, and which you are going to choose depends on your need.

For example, [this article](https://www.linkedin.com/pulse/build-machine-learning-model-network-flow-tao-liu/) did the following for a different purpose.

```
tshark -r thursday-100M.pcap -T fields -E header=y -E separator=, -E quote=d -E occurrence=f -e ip.src -e ip.dst -e ip.len -e ip.flags.df -e ip.flags.mf \
-e ip.fragment -e ip.fragment.count -e ip.fragments -e ip.ttl -e ip.proto -e tcp.window_size -e tcp.ack -e tcp.seq -e tcp.len -e tcp.stream -e tcp.urgent_pointer \
-e tcp.flags -e tcp.analysis.ack_rtt -e tcp.segments -e tcp.reassembled.length -e ssl.handshake -e ssl.record -e ssl.record.content_type -e ssl.handshake.cert_url.url_len \
-e ssl.handshake.certificate_length -e ssl.handshake.cert_type -e ssl.handshake.cert_type.type -e ssl.handshake.cert_type.types -e ssl.handshake.cert_type.types_len \
-e ssl.handshake.cert_types -e ssl.handshake.cert_types_count -e dtls.handshake.extension.len -e dtls.handshake.extension.type -e dtls.handshake.session_id \
-e dtls.handshake.session_id_length -e dtls.handshake.session_ticket_length -e dtls.handshake.sig_hash_alg_len -e dtls.handshake.sig_len -e dtls.handshake.version \
-e dtls.heartbeat_message.padding -e dtls.heartbeat_message.payload_length -e dtls.heartbeat_message.payload_length.invalid -e dtls.record.content_type -e dtls.record.content_type \
-e dtls.record.length -e dtls.record.sequence_number -e dtls.record.version -e dtls.change_cipher_spec -e dtls.fragment.count -e dtls.handshake.cert_type.types_len \
-e dtls.handshake.certificate_length -e dtls.handshake.certificates_length -e dtls.handshake.cipher_suites_length -e dtls.handshake.comp_methods_length -e dtls.handshake.exponent_len \
-e dtls.handshake.extension.len -e dtls.handshake.extensions_alpn_str -e dtls.handshake.extensions_alpn_str_len -e dtls.handshake.extensions_key_share_client_length \
-e http.request -e udp.port -e frame.time_relative -e frame.time_delta -e tcp.time_relative -e tcp.time_delta > thursday-100M.csv
```


If you want to filter data, for example, you only need the first packet of each network conversation, you can use a filter using the `-Y` option.

```
$ tshark -r input.pcap -Y "tcp.flags.syn eq 1" -T fields -E header=y -E separator=, -E quote=d -E occurrence=f \
-e ip.version -e ip.hdr_len -e ip.tos -e ip.id -e ip.flags -e ip.flags.rb -e ip.flags.df \ 
-e ip.flags.mf -e ip.frag_offset -e ip.ttl -e ip.proto -e ip.checksum -e ip.src -e ip.dst \ 
-e ip.len -e ip.dsfield -e tcp.srcport -e tcp.dstport -e tcp.seq -e tcp.ack -e tcp.len \ 
-e tcp.hdr_len -e tcp.flags -e tcp.flags.fin -e tcp.flags.syn -e tcp.flags.reset \ 
-e tcp.flags.push -e tcp.flags.ack -e tcp.flags.urg -e tcp.flags.cwr -e tcp.window_size \ 
-e tcp.checksum -e tcp.urgent_pointer -e tcp.options.mss_val > output.csv
```

Last Trick: If you want to split a large CSV file to smaller files using the command line, just do the following:
```
split -l 5000 <old_file> <new_file_prefixes>
``` 
and it will divide the large file into smaller ones containing 5000 records in each.

If you are interested to learn about OS fingerprinting from PCAP files, you can read this post:
[Passive Operating System Fingerprinting by Analyzing PCAP files](https://shantoroy.com/security/operating-system-fingerprinting/)

That's all Folks, cheers!

If this post helps you to solve your problem, and you want to thank/support me for that, you can  [Buy me Coffee](https://www.paypal.me/shantoroy). :smiley:

## References
1. [Wireshark Packet Analyzer Official SIte](https://www.wireshark.org/)
2. [tshark man page](https://www.wireshark.org/docs/man-pages/tshark.html)
3. [Splitting PCAP Files with tcpdump](https://support.metageek.com/hc/en-us/articles/115000910348-Splitting-PCAP-Files-with-tcpdump)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgzNzUyODE0LDE5NzcxNzc1ODcsLTk4Nz
g3MjE2NSw4OTgyMDQ2NiwtNDUzMjU5NjY3LDExNjg1NDI5NDMs
MTA3NzQ0MzI4OCwtNzI3Mzc2MDQ3LDU0MDg2MTk2NCwxMDgxMT
QwMzQzLDI2ODI0OTAwXX0=
-->