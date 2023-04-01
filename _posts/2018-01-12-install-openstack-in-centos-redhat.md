---
layout: single
title: "How to install Open Stack cloud in Cent OS or Red Hat Linux"
excerpt:  "OpenStack is a popular cloud computing platform that allows users to manage large pools of storage, compute, and networking resources. If you're looking to install OpenStack on your CentOS or Red Hat Linux system, this guide will walk you through the process step-by-step. From preparing your system and configuring network settings to installing OpenStack packages and launching instances, you'll learn everything you need to get started with this powerful cloud computing platform."
seo_title:  How to Install OpenStack Cloud on CentOS or Red Hat Linux
seo_description:  Learn how to install and configure OpenStack on your CentOS or Red Hat Linux system in this comprehensive guide. From preparing your system to launching instances, I'll walk you through every step of the process.
header: 
  image: "https://farm5.staticflickr.com/4714/39193500724_2d5c375b4c_b.jpg"
  teaser: "https://farm5.staticflickr.com/4714/39193500724_2d5c375b4c_b.jpg"
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

OpenStack is a widely used open-source cloud computing platform that allows users to manage large pools of computing, storage, and networking resources throughout a datacenter. 

Installing OpenStack on a Linux-based operating system like CentOS or Red Hat Enterprise Linux can be a complex task for users who are new to the platform. 

In this blog post, I will guide you through the installation process of OpenStack on CentOS or Red Hat Linux step by step.

## Pre-Requisite 
To check out how to install CentOS/Red Hat in your PC you can visit following tutorials created by [Tecmint][tec] -
[How to install Cent OS][cent] or
[How to install Red Hat][red]

[tec]: https://www.tecmint.com/
[cent]: https://www.tecmint.com/centos-7-installation/
[red]: https://www.tecmint.com/redhat-enterprise-linux-7-installation/

### Pre-requisite for system

### Static IP and Hostname
First thing first, you have to set a static `IP` and `hostname`. Check carefully whether or not they are already set.

You can check the `IP` and `hostname` using the following command-

```
# ip a s eth0
# hostname
```

If the IP is a global IP or already obtained from DHCP, set static IP by editing the `/etc/sysconfig/network-scripts/ifcfg-enp0s3` file.

```
# vim /etc/sysconfig/network-scripts/ifcfg-enp0s3
```

set the `bootproto=static`, `IPADDR=192.168.1.5` and `ONBOOT=yes`. It will look like the following-

```
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

```
# vim /etc/sysconfig/network
```

Also, if the DNS is not set, edit the `/etc/resolv.conf` file.

```
# vim /etc/resolv.conf
```

Then add the DNS server address of Google or add your local nameserver address-

```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

Now, restart the `network` service-

```
# systemctl restart network
```

Then you can set the hostname using following command-

```
# hostnamectl set-hostname cloud.example.com
# hostname
```

### Configure NTP (Network Time Protocol)
NTP is generally installed by default while installing the server OS. To check if the ntp service is already running use the following command-

```
# chronyc tracking
```

If it is not running, install the `ntp` package and add to firewall rules.

```
# yum install ntp
# firewall-cmd --permanent --add-service=ntp 
# firewall-cmd --reload
```

Now start the `ntp service`-

```
# systemctl start ntpd
# systemctl enable ntpd
# systemctl status ntpd
```

You can add/modify other information by editing the `\etc\ntp.conf` file.

### Update the kernel
```
# yum upadate -y
# uname -r
# rpm -qa | grep kernel
```

## Install Open Stack
### Install Pack Stack

```
# yum -y install openstack-packstack
```

### Generate & edit an answer file
Now, generate an answer file with default configurations for `packstack`

```
# packstack --gen-answer-file = answer.txt
```

Edit the answer file using vi/m

```
# vim answer.txt
```

Now set the parameters like following-

```
CONFIG_PROVISION_DEMO=n
CONFIG_NTP_SERVERS= 172.16.31.1    # according to your configured ntp server
CONFIG_KEYSTONE_ADMIN_PW = 123456    # Admin password
CONFIG_HORIZON_SSL=y       # for SSL enabled access
```

### Install Open Stack using Packstack
It's all set up now. Install openstack using packstack answer file

```
# packstack --answer-file answer.txt
```

It may take hours to complete the installation process. 

After completion, it will provide a link for the dashboard interface. Generally, it will look like `https://192.168.1.5/dashboard`. You can access to the dashboard using that link in a browser.

Find the credentials under the home directory in `keystonerc_admin` file.

As you are using a `Self-Signed Certificate` issued by an **untrusted Certificate Authority**, your browser will show an error.
Accepting the error, login to the dashboard with the default user admin and the password set on `CONFIG_KEYSTONE_ADMIN_PW` parameter which was set while editing the packstack answer file.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY1NzgxOTEyNV19
-->