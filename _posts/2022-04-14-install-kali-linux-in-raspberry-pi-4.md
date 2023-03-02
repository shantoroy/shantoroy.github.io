---
layout: single
title: "Set Up Headless Kali Linux in a Raspberry Pi 4 without Monitor, Keyboard, and Mouse"
excerpt:  Your  blog  post  excerpt  
seo_title:  Your  meta  title  
seo_description:  Your  meta  description
header:
  image: "https://live.staticflickr.com/65535/51881085549_dd32d6eb18_o.png"
  teaser: "https://live.staticflickr.com/65535/51881085549_dd32d6eb18_o.png"
categories:
  - Security
tags:
  - Kali Linux
  - Tutorial
  - Raspberry Pi
  - Pentesting
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post explains the procedure of Setting up a Kali Linux OS in a Raspberry Pi 4 without any Monitor, Keyboard, and Mouse"
---

If you want to install a Kali Linux machine in your Raspberry pi, it is quite easy to do. You basically flush the image in a microSD and then run it from the raspberry pi.

However, the main concern of this post is to enable SSH without the requirement of monitor, keyboard, or mouse. Here, you basically add your home Wi-Fi information in the Kali Linux, let it have an IP via DHCP, and let you access via SSH without needing an additional monitor for the raspberry pi.


## Requirements
1.  A Raspberry Pi 4
2.  A Power adapter for Raspberry Pi 4
3.  A  microSD card (32GB or higher)
4.  A card reader

Download Kali for ARM from the [Official Kali Linux Download Page](https://www.kali.org/get-kali/). It is around 2 GB of size.

After downloading, you can verify the hash by comparing the generated hash with the original provided in the website.

```
$ sha256sum kali-linux-2021.1-rpi4-nexmon-64.img.xz
```



## Install image in Raspberry Pi
### Download BalenaEtcher
We can flash the OS in a microSD is using different system and third-party tools. The easiest way to do it is using **`balenaEtcher`**, which is a cross platform tool and it can flash an OS in a microSD within minutes. It can be downloaded from the [balena official site](https://www.balena.io/etcher/)

### Flash the MicroSD
Insert the memory card in a card reader and attach to your working computer. Then, launch `balenaEtcher`; and flash in three steps:

1. Select the downloaded Image file from your downloaded location
2. Select the flash drive from the options
3. Click `Flash` and wait for the success notification.

**Note**, you can flash multiple Raspberry Pi device with the same image file.


## Steps
### Enable Kali Linux Raspberry Pi auto login
First, we will have to enable autologin in the Kali Linux system. The Kali Linux Raspberry Pi default username and password is `kali:kali`

Now, we will have to edit the `ligthdm.conf` configuration file.
```bash
$ sudo nano /etc/lightdm/lightdm.conf
```

Here, we will uncomment the lines `83-84` and `126-127`, where, we set values as follows:
```
autologin-user =kali
autologin-user-timeout =0
```
also uncomment the `pam-autologin-service=lightdm-autologin` line under `[Seat:*]`.

Now, open the following file
```
$ sudo nano /etc/pam.d/lightdm-autologin
```
and comment out the following line:
```
# auth required pam_succeed_if.so user != root quiet_success
```

### Add Home Wi-Fi Connection Settings 
Create a file named `<example>.nmconnection` under the `/etc/NetworkManager/system-connections/` directory and paste the following with your own SSID and Password.
```
[connection]
id=ARRIS-0D45
uuid=78f5168f-a717-324d-90b7-2d9496d52d7a
type=wifi
interface-name=wlan0
permissions=user:kali:;

[wifi]
mac-address-blacklist=
mode=infrastructure
ssid=<SSID>

[wifi-security]
auth-alg=open
key-mgmt=wpa-psk
psk=<PASSWORD>

[ipv4]
dns-search=
method=auto

[ipv6]
addr-gen-mode=stable-privacy
dns-search=
method=auto

[proxy]
```

Now, change permission of the file as follows:
```bash
$ sudo chmod 600 <example>.nmconnection
```

Then update the `NetworkManager.conf` file:
```bash
$ sudo  nano  /etc/NetworkManager/NetworkManager.conf
```

change `managed=false` to `managed=true` on the last line
```
[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=true
```

Now, add `wlan0` interface to the `/etc/network/interfaces` file
```bash
$ sudo nano /etc/network/interfaces
```
The file should have the following contents:
```
auto lo
iface lo inet loopback

auto eth0
allow-hotplug eth0
iface eth0 inet dhcp

auto wlan0
iface wlan0 inet dhcp
```

### Final Tasks
1. Start the Raspberry Pi 4
2. Wait 2/3 minutes and try finding the IP address using `Nmap` or other IP scanners, for example, using nmap, you can use the following host discovery command
	```bash
	$ sudo nmap -sP 192.168.0.0/24
	```
3. Now, ssh to the kali linux (for example, mine had the following IP: 192.168.0.6)
	```bash
	$ ssh kali@192.168.0.6
	```

That's all! Now, you can actually carry a mini Kali Linux Machine in your pocket. If something goes wrong, just connect to a monitor via a `HDMI to mini-HDMI` cable to check things out.

Cheers! Happy Pentesting!!!


## References
1. [How to Install Kali Linux on Raspberry Pi 4](https://bughacking.com/how-to-install-kali-linux-on-raspberry-pi-4/)
2. [Kali Linux Installation on Headless Raspberry Pi](https://medium.com/@defsecone/kali-linux-installation-on-headless-raspberry-pi-1856d9c61983)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MzQyMDIyNjddfQ==
-->