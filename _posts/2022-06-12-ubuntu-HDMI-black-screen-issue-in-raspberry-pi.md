---
layout: single
title: "How to fix the Ubuntu Black Screen Issue in a Raspberry Pi after Installation"
excerpt: "If you've recently installed Ubuntu on your Raspberry Pi, you might have encountered the black screen issue when booting up. This is a common problem with a simple fix. In this post, I will show you how to troubleshoot and fix the Ubuntu black screen issue on your Raspberry Pi."
seo_title: "How to Fix the Ubuntu Black Screen Issue in a Raspberry Pi after Installation"
seo_description: "Are you facing a black screen issue on your Raspberry Pi after installing Ubuntu? Don't worry, this post will guide you through the troubleshooting steps to fix the Ubuntu black screen issue on your Raspberry Pi."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - Ubuntu
tags:
  - Ubuntu
  - Tutorial
  - Raspberry Pi
  - HDMI
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Recently, I was facing some issues after installing Ubuntu in a Raspberry Pi. What I did was flashed a microSD using Balena Etcher, put back the card in the Pi, and turned the board on.

### The Issue
However, I was not being able to see anything on the monitor after I connected a HDMI cable to the board.

I restarted the device several times and the screen goes dark immediately after starting to boot.

### The Fix
I looked at several forums, however, almost all of the solutions did not work.

One solution did work. I had to turn the Raspberry Pi off again. I took the microSD out of it and inserted back to my card reader of my laptop.

I accessed the `system-boot` volume and did the following two things to the `config.txt` file:

1. Added the following lines
	```
	hdmi_group=1
	hdmi_mode=16
	```
2. Changed `dtoverlay=vc4-kms-v3d` to `dtoverlay=vc4-fkms-v3d`.

Even though there is a solution exist, I wrote this blog post because I had to look at so many links to find one right way to fix.

I hope this helps. I also have added the reference for your convenience.

Have a good day! 

You can also read my other posts related to `Raspberry Pi`:

* [Set Static IP Address in Linux/Raspbian OS](https://shantoroy.com/linux/set-static-hostname-linux-mac-windows-raspbian/)

* [How to Configure a Raspberry Pi as Gateways between two Private Local Area Network using Ethernet Interfaces](https://shantoroy.com/raspberry%20pi/how-to-configure-raspberry-pi-as-gateway/)

* [Live Video Monitoring using a Raspberry Pi and any Webcam](https://shantoroy.com/raspberry%20pi/live-monitoring-using-raspberry-pi-and-any-webcam/)

* [Set Up Headless Kali Linux in a Raspberry Pi 4 without Monitor, Keyboard, and Mouse](https://shantoroy.com/security/install-kali-linux-in-raspberry-pi-4/)

* [ARM Exploitation with Raspberry Pi: Lab Setup](https://shantoroy.com/security/ARM-exploitation-Raspberry-Pi-lab-setup/)

* [ARM Exploitation with Raspberry Pi: Basic Stack Overflow](https://shantoroy.com/security/ARM-exploitation-raspberry-pi-stack-overflow/)

* [ARM Exploitation with Raspberry Pi: Return Back to Program without Crashing](https://shantoroy.com/security/avoid-segmentation-fault-return-from-shellcode/)

* [ARM Exploitation with Raspberry Pi: ARM Ret-to-Libc](https://shantoroy.com/security/ret-to-libc-arm-exploitation-raspberry-pi/)

* [Build a Balena Cloud using Raspberry Pi](https://shantoroy.com/raspberry%20pi/balenaOS-install-raspberry-pi-balenacloud/)

-   [How to Configure a Raspberry Pi as an OpenFlow Switch: Steps, Issues, and Solutions](https://shantoroy.com/openflow/how-to-configure-raspberry-pi-as-open-flow-switch/)

## References
*   [Black screen after update today](https://forums.raspberrypi.com/viewtopic.php?t=347128)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcwNTUzNjYxNSw4MjEzMTk5ODJdfQ==
-->