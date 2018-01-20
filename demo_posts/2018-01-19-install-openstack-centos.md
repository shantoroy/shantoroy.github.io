---
layout: single
title: How to install Open Stack cloud in Cent OS or Red Hat Linux
header: 
  image: "https://farm6.staticflickr.com/5705/21779044556_6406c39c32_b.jpg"
  teaser: "https://farm6.staticflickr.com/5705/21779044556_6406c39c32_b.jpg"
categories: 
  - Cloud
tags:
  - Open Stack
  - Linux
  - Cent OS
  - Red Hat
  - tutorial
toc: true
toc_label: "Table of Contents"
toc_icon: "heart" 
---

## Pre-Requisite
To check out how to install CentOS/Red Hat in your PC you can visit following tutorials created by [Tecmint][tec]-
[How to install Cent OS][cent]
[How to install Red Hat][red]

[tec]: https://www.tecmint.com/
[cent]: https://www.tecmint.com/centos-7-installation/
[red]: https://www.tecmint.com/redhat-enterprise-linux-7-installation/

### Pre-requisite for system
### Pre-requisite configuration
* Static IP
* Static Hostname
* NTP
* yum update

## Initial Configuration
First thing first, you have to set a static `IP` and `hostname`. Check carefully whether or not they are already set.

You can check the `IP` and `hostname` using the following command-
```bash
# ip a s eth0
# hostname
```

If the IP is a global IP or already obtained from DHCP, set static IP by editing the `/etc/sysconfig/network-scripts/ifcfg-enp0s3` file.
```bash
# vim /etc/sysconfig/network-scripts/ifcfg-enp0s3
```
set the `bootproto=static`, `IPADDR=192.168.1.5` and `ONBOOT=yes`. It will look like the following-
```bash
HWADDR=08:00:17:5C:FF:53
TYPE=Ethernet
BOOTPROTO=static
DEFROUTE=yes
PEERDNS=yes
PEERROUTES=yes
IPV4_FAILURE_FATAL=no
IPADDR=192.168.1.5
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_PEERDNS=yes
IPV6_PEERROUTES=yes
IPV6_FAILURE_FATAL=no
NAME=enp0s3
UUID=eb49ea7e-253b-653c-c9b4-gfdb6f1b4ac5
ONBOOT=yes
```
If the gateway is not set, you can set that by editing the `/etc/sysconfig/network` file.
```bash
# vim /etc/sysconfig/network
```
Also, if the DNS is not set, edit the `/etc/resolv.conf` file.
```bash
# vim /etc/resolv.conf
```
Then add the DNS server address of Google or add your local nameserver address-
```bash
nameserver 8.8.8.8
nameserver 8.8.4.4
```
Then you can set the hostname using following command-
```bash
# hostnamectl set-hostname cloud.example.com
```


## Install Open Stack

## Network Configuration
