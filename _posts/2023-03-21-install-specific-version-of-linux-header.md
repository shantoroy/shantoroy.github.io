---
layout: single
title: "How to Install Specific Version of Linux Header in a Raspberry Pi"
excerpt: "Installing a specific version of Linux header in a Raspberry Pi can be crucial for certain applications to work. However, it can be a tricky process if you are not familiar with the commands. In this blog post, we will guide you through the steps to install a specific version of Linux header in a Raspberry Pi."
seo_title: "How to Install Specific Version of Linux Header in a Raspberry Pi"
seo_description: "Need to install a specific version of Linux header in your Raspberry Pi? This blog post will guide you through the steps to get it done quickly and easily. Learn how to install Linux headers and avoid any issues with your applications on your Raspberry Pi. Includes solution for multiple definition of yylloc error"
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - Raspberry Pi
tags:
  - Raspberry Pi
  - Tutorial
  - Linux
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Hi, this post is a follow-up to [another post](https://shantoroy.com/openflow/how-to-configure-raspberry-pi-as-open-flow-switch/), where I needed a specific version of Linux header.

Read that post here,
[How to Configure a Raspberry Pi as an OpenFlow Switch: Steps, Issues, and Solutions](https://shantoroy.com/openflow/how-to-configure-raspberry-pi-as-open-flow-switch/)

If we search for linux headers using the following command:
```bash
$ apt search linux-headers
```
we see, there is nothing less than `5.10+` version. However, I wanted to install version 4.9. 

In this post, I will go through the steps to install a specific linux header in a Raspberry Pi.

1. Download the source code for the kernel version you want to install. You can find the source code at [https://github.com/raspberrypi/linux](https://github.com/raspberrypi/linux). You need to select `4.9` from the branch and then download zip file.
2. Extract the source code to the `/usr/src` directory

	```bash
	$ sudo cp linux-4.9.y-stable.zip /usr/src/
	$ cd /usr/src/
	```
	```bash
	$ sudo unzip linux-rpi-4.9.y-stable.zip
	```
3. Change to the extracted source code directory
	```bash
	$ cd linux-rpi-4.9.y-stable/
	```
4. Check `bcmxxxx_deconfig` version, check the `xxxx` part
	```bash
	$ ls arch/arm/configs/
	```
	I got `2709`
	```bash
	$ sudo make bcm2709_defconfig
	```
5. Next we need to create `zImage`
	```bash
	$ sudo make clean
	$ sudo make mrproper
	$ sudo make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcm2709_defconfig
	$ sudo make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage
	```
	After executing the last command we can get a error like 

	```
	usr/bin/ld: scripts/dtc/dtc-parser.tab.o:(.bss+0x10): multiple definition of 'yylloc'; scripts/dtc/dtc-lexer.lex.o:(.bss+0x0): first defined here
	```
	we need to edit the `scripts/dtc/dtc-lexer-lex.c` file in that case, find the line 'YYLTYPE yylloc' and change it to 'extern YYLTYPE yylloc'. I found the solution [here](https://github.com/BPI-SINOVOIP/BPI-M4-bsp/issues/4).
	
	Now, let's run the command again. This will take a while (hours!). You can do other things in the meantime.
6. If the build process completes successfully this time, the `zImage` file should be in the `arch/arm/boot` folder. Copy the "zImage" file to the "/boot" directory on your Raspberry Pi's SD card.
	```bash
	$ sudo cp arch/arm/boot/zImage /boot
	```
7. Configure the kernel using the existing configuration file (`.config`)

	```bash
	$ sudo make oldconfig
	```
8. Compile the kernel
	```bash
	$ sudo make -j$(nproc)
	```
	This also takes some time.
9. Install the kernel modules
	```bash
	$ sudo make modules_install
	```
10. Install the kernel
	```bash
	$ sudo make install
	```
11. Reboot the system to start using the new kernel.

That's all! 

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

*  [How to Configure a Raspberry Pi as an OpenFlow Switch: Steps, Issues, and Solutions](https://shantoroy.com/openflow/how-to-configure-raspberry-pi-as-open-flow-switch/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA1NTIxNjUyOV19
-->