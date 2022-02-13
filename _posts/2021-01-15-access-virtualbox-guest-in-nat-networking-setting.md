---
layout: single
title: "Enable Access to VirtualBox Guest Machine via SSH in a NAT Network Settings"
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/51878165271_d341fbc248_o.png"
categories:
  - Security
tags:
  - virtualbox
  - ssh
  - NAT
  - bridge
  - Tutorial
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post provides a solution to enable SSH to a VirtualBox VM in a NAT Network Settings"
---


Virtualbox and VMWare are the most popular environments that allow us to run different operating systems within a virtual environment. As a developer or security analyst, we use these guest machines and often set up a network.

The most preferred way of putting all of these virtual machines within a local area network is to set up a `bridge adapter` in each guest and allow those virtual machines to receive IP addresses from the same router.

However, in many situations, we might not need to set up LAN or the bridge settings does not work well (e.g., updated macOS has issues with allowing to share internet via WLAN adapter). 

In that case, we can simply continue using the NAT settings and if needed, we can have some settings so that we can ssh the guest OS.

Here, is the step-by-step procedure to do so:

1. Click on `Settings -> Network -> Advanced`
2. Click on `Port Forwarding`
3. Edit the dialog box settings as follows:
		* Name: SSH
		* Protocol: TCP
		* Host IP: 127.0.0.1
		* Host Port: 5500
		* Guest IP: 10.0.2.15
		* Guest Port: 22

Now, if you have set exactly the same way described above, you should be able to `ssh` using the following command from the Linux/macOS terminal.
```bash
$ ssh -p 5500 kali@127.0.0.1
```

Or, you can use GUI-based tools (e.g., putty) to do that.

That's all. Thanks and Cheers!!!
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MTMyOTYyNDJdfQ==
-->