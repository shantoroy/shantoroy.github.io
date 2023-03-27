---
layout: single
title: "Live Video Monitoring using a Raspberry Pi and any Webcam"
header:
  image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/51881564712_cc98a50055_o.png"
categories:
  - Raspberry Pi
tags:
  - Motion
  - Tutorial
  - Raspberry Pi
  - Security
  - Monitoring
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


We often need to monitor the outside of our home or to check activities of children inside a room.

In this post, I am going to demonstrate a simple Raspberry Pi project that uses any webcam to provide the option for live monitoring.

### Installation
First, you will have to install an OS in the Raspberry Pi. You can choose any and flush that in a MicroSD card. Check my other post where I have provided the details of doing so.

[Install Raspbian OS in Raspberry Pi without Keyboard and Monitor](https://shantoroy.com/raspberry%20pi/install-raspbian-os-raspberry-pi-without-monitor-keyboard/)


### Find IP address
Now, if you have connected your Raspberry Pi to your home network, we will have to obtain the IP address of the Pi. We can simply use the `nmap` or any other IP scanner tool to find the IP address of the Pi. 


```bash
$ sudo nmap -sP 10.0.0.0/24
```

Or if you are using a monitor, then skip it and avoid the following step (SSH) as well.

### SSH into the Pi
Now, if you have your IP address, just SSH into the system.
```bash
$ ssh -p 2222 pi@10.0.0.25
```

### Installation
Install `motion`, which provides the option for live monitoring.
```bash
$ sudo apt-get install motion
```

### Find Webcam
Connect a webcam to the raspberry pi and find the webcam using the command `lsusb`.
```bash
$ lsusb
```

### Configure Motion
Now, we will have to configure `motion`. Let's open the file in an editor.
```bash
$ sudo nano /etc/motion/motion.conf
```

Now, change the following configurations:
* Make sure 'daemon' is ON.
* framerate $\rightarrow$ 1000 to 1500.
* Stream_port $\rightarrow$ 8081.
* Stream_quality $\rightarrow$ 100.
* Stream_localhost $\rightarrow$ OFF.
* webcontrol_localhost $\rightarrow$ OFF.
* quality $\rightarrow$ 100.
* width & height $\rightarrow$ 640 & 480.
* post_capture $\rightarrow$ 5.

Press ctrl + x to exit. Type y to save and enter to conform.

Now, open the following file and configure as follows:

```bash
$ sudo nano /etc/default/motion
```

* start_motion_daemon $\rightarrow$ yes

### Running Motion
Use the following commands to run `motion`
```bash
$ sudo service motion restart
$ sudo motion
[444040:motion] [NTC] [ALL] conf_load: Processing thread 0 - config file /etc/motion/motion.conf
[444040:motion] [NTC] [ALL] motion_startup: Motion 4.1.1 Started
[444040:motion] [NTC] [ALL] motion_startup: Logging to file (/var/log/motion/motion.log)
```

### Checking Live Feed
Now, you will be able to find the live by typing the following in your browser and enter.
`localhost:8081`

If you want to see the live feed from outside, you need to configure port forwarding in your home router
`public_IP_address:forwarded_port_address`


That's all for today. Cheers!


You can also read my other posts related to `Raspberry Pi`:

* [Set Static IP Address in Linux/Raspbian OS](https://shantoroy.com/linux/set-static-hostname-linux-mac-windows-raspbian/)

* [How to Configure a Raspberry Pi as Gateways between two Private Local Area Network using Ethernet Interfaces](https://shantoroy.com/raspberry%20pi/how-to-configure-raspberry-pi-as-gateway/)

* [How to fix the Ubuntu Black Screen Issue in a Raspberry Pi after Installation](https://shantoroy.com/ubuntu/ubuntu-HDMI-black-screen-issue-in-raspberry-pi/)


* [Set Up Headless Kali Linux in a Raspberry Pi 4 without Monitor, Keyboard, and Mouse](https://shantoroy.com/security/install-kali-linux-in-raspberry-pi-4/)

* [ARM Exploitation with Raspberry Pi: Lab Setup](https://shantoroy.com/security/ARM-exploitation-Raspberry-Pi-lab-setup/)

* [ARM Exploitation with Raspberry Pi: Basic Stack Overflow](https://shantoroy.com/security/ARM-exploitation-raspberry-pi-stack-overflow/)

* [ARM Exploitation with Raspberry Pi: Return Back to Program without Crashing](https://shantoroy.com/security/avoid-segmentation-fault-return-from-shellcode/)

* [ARM Exploitation with Raspberry Pi: ARM Ret-to-Libc](https://shantoroy.com/security/ret-to-libc-arm-exploitation-raspberry-pi/)

* [Build a Balena Cloud using Raspberry Pi](https://shantoroy.com/raspberry%20pi/balenaOS-install-raspberry-pi-balenacloud/)

-   [How to Configure a Raspberry Pi as an OpenFlow Switch: Steps, Issues, and Solutions](https://shantoroy.com/openflow/how-to-configure-raspberry-pi-as-open-flow-switch/)

## References
1. [How to Make Raspberry Pi Webcam Server and Stream Live Video || Motion + Webcam + Raspberry Pi](https://www.instructables.com/How-to-Make-Raspberry-Pi-Webcam-Server-and-Stream-/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTM1MDY3OTA0LC0xMzAzNDIyMDcyLDEzOT
EzNTU5NzBdfQ==
-->