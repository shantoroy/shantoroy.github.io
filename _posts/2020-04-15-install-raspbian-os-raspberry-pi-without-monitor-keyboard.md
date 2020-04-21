
---
layout: single
title: "Install Raspbian OS in Raspberry Pi without Keyboard and Monitor"
header:
  image: "https://live.staticflickr.com/65535/49799517663_f7285ba01d_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49799517663_f7285ba01d_h.jpg"
categories:
  - Raspberry-Pi
tags:
  - Tutorial
  - ARM
  - Installation
  - Raspberry-Pi
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg1MDE3NzQxNCwtMTI3NjAwNTM4OCwtMT
M2NjYwNzAxMl19
-->
