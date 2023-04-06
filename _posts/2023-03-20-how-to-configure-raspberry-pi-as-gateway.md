---
layout: single
title: "How to Configure a Raspberry Pi as Gateways between two Private Local Area Network using Ethernet Interfaces"
excerpt: "In research/development testbeds, there is often a need to connect multiple local area networks together. One way to achieve this is by using a Raspberry Pi as a gateway between two private LANs. In this blog post, I will guide you through the process of setting up your Raspberry Pi and configuring it as a gateway between two LANs using Ethernet interfaces."
seo_title: "Step-by-Step Guide: Configure Raspberry Pi as a Gateway for Two Private LANs using Ethernet Interfaces"
seo_description: "Learn how to configure your Raspberry Pi as a gateway between two private local area networks using Ethernet interfaces. My easy-to-follow guide provides step-by-step instructions for setting up a testbed and configuring the necessary settings to get two LANs communicating with each other."
header:
  image: "https://live.staticflickr.com/65535/52762763609_cc0b7cecb9_o.png"
  teaser: "https://live.staticflickr.com/65535/52762763609_cc0b7cecb9_o.png"
categories:
  - Raspberry Pi
tags:
  - System
  - Raspberry Pi
  - Gateway
  - Configuration
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



If we want to create a physical testbed to experiment different scenarios, Raspberry Pi's are the best options out there. We can create private networks and connect the networks through routers or gateways.

And we don't have to buy a router to connect two different networks. We can configure one of our raspberry Pi's to act as gateways for two different private networks and connect these networks as well.

In this post, we will learn how to configure a Raspberry Pi to act as two gateways for two different networks and route traffics between these two networks through Ethernet interfaces.

## Hardware Requirements
We will need the following hardware:
- Three Raspberry Pi Devices with power adapter/cables and memory cards
- Three Ethernet Cables
- One USB-to-LAN Converter

If you need to check how to install a Raspbian OS to a Raspberry Pi, check out my [other blog post](https://shantoroy.com/raspberry%20pi/install-raspbian-os-raspberry-pi-without-monitor-keyboard/).

[Install Raspbian OS in Raspberry Pi without Keyboard and Monitor](https://shantoroy.com/raspberry%20pi/install-raspbian-os-raspberry-pi-without-monitor-keyboard/)

## Setting Static IP
First, we need to set static IP addresses to the ethernet interfaces. We can do that by adding the following configuration:

### The End Devices
Let's create a file for interface `eth0`
```bash
$ sudo nano /etc/network/interfaces.d/eth0
```

And add the following to the one of the Raspberry Pi devices:
```
# Static IP configuration for eth0
auto eth0
iface eth0 inet static
address 192.168.5.10
netmask 255.255.255.0
network 192.168.5.0
broadcast 192.168.5.255
gateway 192.168.5.1
```

and the following to the second one:
```
# Static IP configuration for eth0
auto eth0
iface eth0 inet static
address 192.168.6.10
netmask 255.255.255.0
network 192.168.6.0
broadcast 192.168.6.255
gateway 192.168.6.1
```

### The Gateway
For the Gateway Raspberry Pi, we have two ethernet interfaces: `eth0` and `eth1` after we added the USB-to-ethernet cable to one of the USB ports.

So, we will create two files. Let say, `eth0` is connected to `192.168.5.10`, then we will do the following

```bash
$ sudo nano /etc/network/interfaces.d/eth0
``` 
```
# Static IP configuration for eth0
auto eth0
iface eth0 inet static
address 192.168.5.1
netmask 255.255.255.0
network 192.168.5.0
broadcast 192.168.5.255
gateway 192.168.5.1
```

And, then `eth1` is connected to `192.168.6.10`
```bash
$ sudo nano /etc/network/interfaces.d/eth1
``` 
```
# Static IP configuration for eth1
auto eth1
iface eth1 inet static
address 192.168.6.1
netmask 255.255.255.0
network 192.168.6.0
broadcast 192.168.6.255
gateway 192.168.6.1
```

Or, there is a good alternative way to do all in a single file. In the `/etc/network/interfaces` file, instead of the following, 
```
auto lo
iface lo inet loopback

source /etc/network/interfaces.d/*

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp
```

we can have everything in that file:

```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
address 192.168.5.1
netmask 255.255.255.0
network 192.168.5.0
broadcast 192.168.5.255
gateway 192.168.5.1

auto eth1
iface eth1 inet static
address 192.168.6.1
netmask 255.255.255.0
network 192.168.6.0
broadcast 192.168.6.255
gateway 192.168.6.1

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp
```

Now, whatever change we made, we will have to run the following command

```bash
$ sudo systemctl restart networking
```
Or, if not working, reboot the devices.

## Routing
We can ping both `192.168.5.10` and `192.168.6.10` from the gateway raspberry pi. However, the devices cannot ping to each other for now.

To make routing happen between both end devices, we will have to run the following command in the gateway raspberry pi:

```bash
$ sudo sysctl net.ipv4.ip_forward=1
```

also, set up NAT (Network Address Translation) on the Raspberry Pi to allow traffic from the honeypot network to access the Internet via the real network.
```bash
$ sudo mkdir /etc/iptables
$ sudo touch /etc/iptables/rules.v4
$ sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
$ sudo iptables-save | sudo tee /etc/iptables/rules.v4
```

Now, you should be able to ping each devices. 

Note that, if the gateways are not properly set up and ping does not work, you can additionally do the following:

Add static routes on each of the two Raspberry Pis to enable them to communicate with each other. On the Raspberry Pi with IP address 192.168.5.10, add a static route for the 192.168.6.0/24 subnet by running the following command:

```bash
$ sudo ip route add 192.168.6.0/24 via 192.168.5.1
```
Similarly, on the Raspberry Pi with IP address 192.168.6.10, add a static route for the 192.168.5.0/24 subnet by running the following command:

```bash
$ sudo ip route add 192.168.5.0/24 via 192.168.6.1
```




## Concluding Remarks
That's all for today. I hope this tutorial can help you set up testbeds according to your needs if there are multiple networks you are dealing with.

I have made this tutorial to do the routing through Ethernet interfaces since the WiFi interface I use for SSH (for configuration change and troubleshooting from remote location) and internet access only. When I will no longer need outside connection, I can simply disconnect these devices from WiFi and work around a perfect testbed.


You can also read my other posts related to `Raspberry Pi`:

* [Set Static IP Address in Linux/Raspbian OS](https://shantoroy.com/linux/set-static-hostname-linux-mac-windows-raspbian/)


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
eyJoaXN0b3J5IjpbLTEwMTY2NzEyNTcsLTE3MzgwNDk1MF19
-->