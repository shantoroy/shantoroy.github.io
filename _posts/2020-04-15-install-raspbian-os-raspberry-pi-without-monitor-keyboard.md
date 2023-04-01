---
layout: single
title: "Install Raspbian OS in Raspberry Pi without Keyboard and Monitor"
excerpt:  "In this tutorial, I'll show you how to install Raspbian OS in Raspberry Pi without using a keyboard and monitor. This method is useful when you don't have access to a keyboard and monitor, or when you want to do a headless installation. By following the steps in this guide, you'll be able to install Raspbian OS on your Raspberry Pi using your laptop or desktop computer."
seo_title:  Your  meta  title  
seo_description:  Your  meta  description
header:
  image: "https://live.staticflickr.com/65535/49799517663_f7285ba01d_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49799517663_f7285ba01d_h.jpg"
categories:
  - Raspberry Pi
tags:
  - Tutorial
  - ARM
  - Installation
  - Raspberry Pi
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Raspberry Pi is widely used to build IoT projects and it is continuously gaining more attention and popularity. After buying a Raspberry Pi, we can install an OS within a few minutes.

We usually need a monitor and a keyboard to install operating system in a physical machine. However, in this tutorial we will learn how to install `Raspbian OS` without a keyboard and a monitor. Also, how we can have access to the device using SSH via WiFi.

## Download Raspbian OS
Let's first download the latest version of **`Raspbian OS`** from the [Raspberry Pi official site](https://www.raspberrypi.org/downloads/raspbian/). The latest version is the `Raspbian Buster`.

## Download BalenaEtcher
We can flash the OS in a microSD is using different system and third-party tools. The easiest way to do it is using **`balenaEtcher`**, which is a cross platform tool and it can flash an OS in a microSD within minutes. It can be downloaded from the [balena official site](https://www.balena.io/etcher/)

## Flash the MicroSD
Insert the memory card in a card reader and attach to your working computer. Then, launch `balenaEtcher`; and flash in three steps:

1. Select the downloaded Image file from your downloaded location
2. Select the flash drive from the options
3. Click `Flash` and wait for the success notification.

## Add Configuration Files
When you are done with flashing, you need to add two files. Go to the **boot** drive and add following files.

### Enable `SSH`
To enable `ssh`, simply add a file named **`SSH`** in the `boot` directory. Note that, the file should not have any extension. 

Now, you will be able to ssh to your machine via a **`LAN Cable`**. You can simply login via a terminal from Linux or macOS. If you are using Windows, download [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/) and login from there.

The default hostname, usename and password are as follows:
```
hostname: raspberrypi.local
username: pi
password: raspberry
```
You can change the password later using the command **`sudo raspi-config`**.

### Connect to WiFi Network
To enable ssh via WiFi, you have to create another file that holds network information. Create a file named **`wpa_supplicant.conf`** and add the following lines:
```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="Your SSID 1"
psk="Your Password"
key_mgmt=WPA-PSK
}

network={
ssid="Your SSID 2"
psk="Your Password"
key_mgmt=WPA-PSK
}
```

Here, I have added two different WiFi networks. You can add as many as you want. Just edit the `SSID` and the `password` in your file. 

Now, after inserting the microSD in the Raspberry Pi and powering on the device, you can ssh via WiFi, no need of any Ethernet cable.


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

-   [How to Configure a Raspberry Pi as an OpenFlow Switch: Steps, Issues, and Solutions](https://shantoroy.com/openflow/how-to-configure-raspberry-pi-as-open-flow-switch/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzc0NDY3MzUzLDE4NTAxNzc0MTQsLTEyNz
YwMDUzODgsLTEzNjY2MDcwMTJdfQ==
-->