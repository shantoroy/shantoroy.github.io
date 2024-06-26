---
layout: single
title: "How to Configure a Raspberry Pi as an OpenFlow Switch: Steps, Issues, and Solutions"
excerpt:  "Configuring a Raspberry Pi as an OpenFlow switch (low cost open flow switch) can be a great way to set up your own network. However, the process can be complex and come with common issues. In this guide, I will provide step-by-step instructions and solutions to help you get started with ease. Whether you're a beginner or an experienced user, you'll be able to configure your Raspberry Pi as an OpenFlow switch and set up your own software-defined (SDN) network including troubleshooting."
seo_title:  "A Step-by-Step Guide to Configuring a Raspberry Pi as an OpenFlow Switch"
seo_description:  "Learn how to configure a Raspberry Pi as an OpenFlow switch with this comprehensive guide. Build your first low cost open flow switch. It can also be a low cost SDN switch. Discover common issues, troubleshooting guides, and solutions, and set up your own software-defined (SDN) network."
header:
  image: "https://live.staticflickr.com/65535/52763084849_e3ee0ecaf0_o.png"
  teaser: "https://live.staticflickr.com/65535/52763084849_e3ee0ecaf0_o.png"
categories:
  - OpenFlow
tags:
  - Raspberry Pi
  - Tutorial
  - OpenFlow
  - Openvswitch
  - SDN
  - Switch
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Buying an open flow switch can cost you a few hundred dollars. However, we can build a low-cost open flow switch from the scratch.

To build a low-cost open flow switch, we will need a Raspberry Pi and a few (max four) USB-to-Ethernet (alternatively, known as USB-to-LAN) converter cables.

There are many tutorials that discuss how to configure a Raspberry Pi as an Open Flow Switch. However, following the same steps can make you face many issues, which I have faced earlier while working on a project.

In this blog post I will note down the entire process that works with the latest version changes and compatibility issues. I will also show how I tried to troubeshoot the issues and eventually reached to solutions.

## Version Mismatch Issues
### Download Openvswitch
Let's first download openvswitch
```bash
$ wget http://openvswitch.org/releases/openvswitch-2.5.2.tar.gz
```
and unzip
```bash
$ tar -xvzf openvswitch-2.5.2.tar.gz
```

### Install Dependencies
Now, let's install dependencies
```bash
$ apt-get install python-simplejson python-qt4 libssl-dev python-twisted-conch automake autoconf gcc uml-utilities libtool build-essential pkg-config
```
and we get the following errors:

```
E: Unable to locate package python-simplejson
E: Unable to locate package python-qt4
E: Unable to locate package python-twisted-conch
```
and let's try to install linux headers
```
$ apt-get install linux-headers-3.10-3-rpi
```
then we get this error

```
E: Unable to locate package linux-headers-3.10-3-rpi
E: Couldn't find any package by glob 'linux-headers-3.10-3-rpi'
E: Couldn't find any package by regex 'linux-headers-3.10-3-rpi'
```

## TroubleShooting
### Fix Dependency Installation
We can use the following command to find if something is available:

```bash
root@raspberrypi:~# apt-cache search simplejson
```
and we get the following:
```
golang-github-bitly-go-simplejson-dev - Golang library to interact with arbitrary JSON
python-jsonpickle-doc - Python library for serializing object graphs into JSON (documentation)
python-simplejson-doc - simple, fast, extensible JSON encoder/decoder for Python - documentation
python3-jsonpickle - Python library for serializing object graphs into JSON (Python 3)
python3-simplejson - simple, fast, extensible JSON encoder/decoder for Python 3.x
python3-simplejson-dbg - simple, fast, extensible JSON encoder/decoder for Python 3.x - debug symbols
```
so, we see, there is a package available named `python3-simplejson`. So, we need to change `python-simplejson` to `python3-simplejson`.

Since, there is `qt5` available now, let's search like the following:
```sh
root@raspberrypi:~# apt-cache search python3-pyqt5
```
Well, it has a long matching result and means it is available.

For `twisted`, I did the following at first:
```sh
root@raspberrypi:~# apt-cache search twisted-conch
```
There is nothing. So, again I shortened the name:

```sh
root@raspberrypi:~# apt-cache search twisted
```
Now, I get a long matching list and I find `python3-twisted` available out there.

**So, let's finalize the whole dependency installation line like the following**:

```sh
root@raspberrypi:~# apt-get install python3-simplejson python3-pyqt5 libssl-dev python3-twisted automake autoconf gcc uml-utilities libtool build-essential pkg-config
```


### Fix Linux Headers
If the right compatible linux header is not there, we may run into issues when configuring the `openvswitch`.

```bash
$ cd openvswitch-2.5.2
$ ./configure --with-linux=/lib/modules/3.10-3-rpi/build
```
And we get error as this version does not exist today.
### Updated Linux Header Version Issues
If we have issues, let's first check the installed versions
```bash
$ ls /lib/modules/
5.15.76+  5.15.76-v7+  5.15.76-v7l+  5.15.76-v8+
```

These are recent versions available after we installed linux headers.

However, we get the following error:

```
configure: error: source dir /lib/modules/5.15.84+/build doesn't exist
```
as there is no `build` directory within any of these folders.

Now, let's check with one of these:
```bash
$ ./configure --with-linux=/lib/modules/5.15.76+/build

configure: error: Linux kernel in /lib/modules/5.15.76+/build is version 5.15.76, but version newer than 4.3.x is not supported (please refer to the FAQ for advice)
```
Now, we get errors again.

**update:** Later I tried installing a generic updated version using the following command:

```bash
$ sudo apt install raspberrypi-kernel-headers
```
and it installed 6.1.19.

Now, while configuring, it gave me the following error message:

```
configure: error: Linux kernel in /lib/modules/6.1.19+/build is version 6.1.19, but version newer than 5.8.x is not supported (please refer to the FAQ for advice)
```

### Check for available linux headers
We can check for the available linux headers using the following command:
```bash
$ apt search linux-headers
```
And we see, there is nothing less than `5.10+` version. But, that's an issue as from [the official source](https://docs.openvswitch.org/en/latest/faq/releases/), the maximum support version is $5.8$.

However, I find build error for anything greater than version 5. The error is similar to the one reported in [this stackoverflow thread](https://stackoverflow.com/questions/71918528/compile-openvswitch-in-odroid-xu4-has-error). We must install a version **4.9 or less**. 

Now, let's look at the following link to find updated versions. And voila! It also states supporting linux kernel associated with each version.

https://docs.openvswitch.org/en/latest/faq/releases/

## Another Try
The following is what I tried later. 
```bash
$ wget http://openvswitch.org/releases/openvswitch-3.0.0.tar.gz
$ tar -xvzf openvswitch-3.0.0.tar.gz
```
and then
```bash
$ cd openvswitch-3.0.0/
$ ./configure --with-linux=/lib/modules/5.15.76+/build
$ make
$ make install
```

Well, it didn't work for me either. Somehow, there was a missing `datapath` directory inside.

## Finally Worked for Following Versions
Here, I am sharing for the versions that worked for me fine. Let's first get the openvswitch.
```bash
$ wget https://www.openvswitch.org/releases/openvswitch-2.17.1.tar.gz
$ tar -xvzf openvswitch-2.17.1.tar.gz
```



and then do the rest.
```bash
$ cd openvswitch-2.17.1
$ ./configure --with-linux=/lib/modules/4.9.0-6-rpi/build
$ make
$ sudo make install
```

Note that, I had to install linux header version `<5.8` to support openvswitch `2.17.1` version. The installation of earlier version is manual and I will add a seperate post for that. In practice, it supports any version of **4.9 or less**.

I have written another blog post on how to manually install an earlier version. Here's the link:
[How to Install Specific Version of Linux Header in a Raspberry Pi](https://shantoroy.com/raspberry%20pi/install-specific-version-of-linux-header/)


Now, to make `modprobe` work, we need to **restart** the raspberry pi. When rebooted, let's do the following:
```bash
$ su
$ cd openvswitch-2.17.1/datapath/linux/
$ modprobe openvswitch
```

Then we need to create a file named `ovs_script.sh` with the following code:
```
#!/bin/bash
ovsdb-server --remote=punix:/usr/local/var/run/openvswitch/db.sock \
    --remote=db:Open_vSwitch,Open_vSwitch,manager_options \
    --private-key=db:Open_vSwitch,SSL,private_key \
    --certificate=db:Open_vSwitch,SSL,certificate \
    --bootstrap-ca-cert=db:Open_vSwitch,SSL,ca_cert \
    --pidfile --detach
ovs-vsctl --no-wait init
ovs-vswitchd --pidfile --detach
ovs-vsctl show
```

Then we need to create a file named `ovs-vswitchd.conf` in the configuration directory to track the details of the switch.
```bash
$ touch /usr/local/etc/ovs-vswitchd.conf
```
and a directory
```bash
$ mkdir -p /usr/local/etc/openvswitch
```
Then we need to populate the database. Here I used relative paths.
```bash
$ cd ../..
$ ovsdb-tool create /usr/local/etc/openvswitch/conf.db vswitchd/vswitch.ovsschema
```


Need to go back to the previous directory (datapath/linux), where we created the script. Then we need to run the script.
```bash
$ cd -
$ chmod +x ovs_script.sh
$ ./ovs_script.sh
```


```bash
$ /usr/local/share/openvswitch/scripts/ovs-ctl --system-id start
$ sudo ./ovs_script.sh
```
And we just configured a Raspberry Pi to act as an Open Flow Switch.

## Concluding Remarks
The existing tutorials I found online does not have the fix for the Linux Header compatibility. While following those steps I faced the issues and eventually could solve it.

I hope, now, you can configure a Raspberry Pi to act as an Open Flow Switch without any issue. In a later tutorial, I will show how to work around the switch.

Until then, have a great time!

You can also read my other posts related to `Raspberry Pi`:
* [Set Static IP Address in Linux/Raspbian OS](https://shantoroy.com/linux/set-static-hostname-linux-mac-windows-raspbian/)
* [How to Configure a Raspberry Pi as Gateways between two Private Local Area Network using Ethernet Interfaces](https://shantoroy.com/raspberry%20pi/how-to-configure-raspberry-pi-as-gateway/)
* [How to fix the Ubuntu Black Screen Issue in a Raspberry Pi after Installation](https://shantoroy.com/ubuntu/ubuntu-HDMI-black-screen-issue-in-raspberry-pi/)
* [Live Video Monitoring using a Raspberry Pi and any Webcam](https://shantoroy.com/raspberry%20pi/live-monitoring-using-raspberry-pi-and-any-webcam/)
* [Set Up Headless Kali Linux in a Raspberry Pi 4 without Monitor, Keyboard, and Mouse](https://shantoroy.com/security/install-kali-linux-in-raspberry-pi-4/)
* [ARM Exploitation with Raspberry Pi: Lab Setup](https://shantoroy.com/security/ARM-exploitation-Raspberry-Pi-lab-setup/)
* [ARM Exploitation with Raspberry Pi: Basic Stack Overflow](https://shantoroy.com/security/ARM-exploitation-raspberry-pi-stack-overflow/)
* [ARM Exploitation with Raspberry Pi: Return Back to Program without Crashing](https://shantoroy.com/security/avoid-segmentation-fault-return-from-shellcode/)
* [ARM Exploitation with Raspberry Pi: ARM Ret-to-Libc](https://shantoroy.com/security/ret-to-libc-arm-exploitation-raspberry-pi/)
* [Build a Balena Cloud using Raspberry Pi](https://shantoroy.com/raspberry%20pi/balenaOS-install-raspberry-pi-balenacloud/)

## References
1. [Configuring Raspberry PI as an OpenFlow switch](https://praveennotes.com/2019/02/01/Configuring-Raspberry-PI-as-an-OpenFlow-switch.html)
2. [Converting a Raspberry Pi to a OpenFlow Switch](https://sumitrokgp.wordpress.com/2017/05/18/converting-a-raspberry-pi-to-a-openflow-switch/)
3. [Install OVS (Openvswitch) in Raspberry-Pi](https://techflow360.com/install-ovs-openvswitch-in-raspberry-pi/)
4. [PiOVS: Raspberry Pi Open vSwitch](https://www.telematika.org/post/piovs-raspberry-pi-open-vswitch/)
5. [Open vSwitch database connection failure after rebooting](https://stackoverflow.com/questions/28506053/open-vswitch-database-connection-failure-after-rebooting)
6. [[Official] Open vSwitch Releases](https://docs.openvswitch.org/en/latest/faq/releases/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU5MTQ5NTc4OSwxMzQ0MTYwNDU4LDgxNT
gwMTYxMCw5NDU1NDA0NzgsLTQzNjEwMjM3Nyw0MjM4NTQ5Mzgs
LTEzMjI1NDgyNzMsLTE5MTQyMjc1MTAsLTE4MjE1NzMyNDksND
U4NTYxOTIyLDE0MzU4NDQzNDksLTIxMTQ3OTkxODksMTEyNjQ2
MDkzLDExMzQ2MTcwNTBdfQ==
-->