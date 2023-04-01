---
layout: single
title: "How to Set Static IP Address in Linux/Raspbian OS"
excerpt:  "Are you tired of your IP address changing every time you restart your Linux/Raspbian OS? Setting up a static IP address can make your life much easier! In this tutorial, we'll walk you through the steps of setting up a static IP address on your Linux/Raspbian machine."
seo_title:  Your  meta  title  
seo_description:  Your  meta  description
header:
  image: "https://live.staticflickr.com/65535/51228020554_0a011cd6ca_w.jpg"
  teaser: "https://live.staticflickr.com/65535/51228020554_0a011cd6ca_w.jpg"
categories:
  - Linux
tags:
  - SysAdmin
  - Tutorial
  - Static IP
  - Computer Nework
  - Raspberry Pi
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

There are two ways of assigning IP addresses to a server or client machine. Most of the times we use DHCP to avoid additional work to assign IP addresses. 

Dynamic Host Configuration Protocol (DHCP) is a way to assign IP addresses from a range of IP addresses and usually the action is performed by a router.

However, sometimes we need to assign static IP addresses when we want to login via SSH or perform particular actions from a remote host. In case of DHCP, the IP address may change if either of the device itself or the router is restarted. However, in case of static IP, the assigned IP always remained the same.

In this tutorial, we will see how to configure static IP addresses to Linux and Raspberry Pi operating systems.

## Linux
### Ubuntu
For Ubuntu, we need to edit the `/etc/network/interfaces` configuration file where we assign the static IP to a particular network interface. 

```
auto enp0s3
iface enp0s3 inet static
        address 10.1.1.83
        netmask 255.0.0.0
        gateway 10.1.1.1
        dns-nameservers 8.8.8.8 8.8.4.4
```
In this example, `enp0s3` is the interface name. We add the static IP address, subnet mask, gateway, and DNS information in the file.

### Red Hat Linux
`Red Hat` or `Cent OS` are popular RPM-based server distributions. In case of setting static IP address, we will have to edit the interface file that resides in `/etc/sysconfig/networking-scripts/` directory. Therefore, the interface file path looks like-
`/etc/sysconfig/networking-scripts/ifcfg-_INTERFACE-NAME_`, where `_INTERFACE-NAME_` should be replaced with the interface name in your server.

Now, you will have to rewrite the configuration file as follows:

```
DEVICE=enp0s3
BOOTPROTO=static
HWADDR=aa:bb:cc:dd:ee:ff
IPADDR=192.168.1.100
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DEFROUTE=yes
ONBOOT=yes 
IPV6INIT=no
DOMAIN="server.example.net"
DNS1=128.83.185.40
DNS2=128.83.185.41
```
Here, you will have to set `BOOTPROTO` as `static`, and other information (IP address, subnet mask, gateway, and DNS information) as usual. 


## Raspbian
For `Raspbian OS`, which is the mostly used OS in Raspberry Pi devices, you need to edit the `/etc/dhcpcd.conf` file. Here, you have append the following types of information and then reboot your system.
```bash
$ nano /etc/dhcpcd.conf

# Append at the end of the file
interface wlan0
static ip_address=192.168.1.5/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```

That's all for today! Cheers!!!
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcxMDEzNDU0LDE5MTA5NjYxNzYsODIyNj
cxNDc0LC00ODE0OTQ0NCwtMTcyOTg5NjgyOSw3Mzg5MTI5NTUs
MjAyNTUwODI3NF19
-->