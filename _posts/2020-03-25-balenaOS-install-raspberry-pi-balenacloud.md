---
layout: single
title: "Build a Balena Cloud using Raspberry Pi"
header:
  image: "https://live.staticflickr.com/65535/49803481683_3b7c3e3447_b.jpg"
  teaser: "https://live.staticflickr.com/65535/49803481683_3b7c3e3447_b.jpg"
categories:
  - Raspberry Pi
tags:
  - Tutorial
  - ARM
  - Installation
  - Raspberry Pi
  - Balena Cloud
  - Balena OS
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---
We can simply work on microservice and different other projects in Balena Cloud which is nothing but a collection of Raspberry Pi devices.

Here, in this post we will learn how to install BalenaOS in Raspberry Pi and connect to the Balena Cloud. Anyone can access the devices from anywhere given the username and password for the dashboard.

## Requirements
-   [Raspberry Pi 4 Model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) 
-   microSD card (4GB Minimum, class 10)
-   Power supply
-   [balena account](https://dashboard.balena-cloud.com/signup)
-   WiFi Connection

## Download Balena OS
1. Create an account in [balena](https://dashboard.balena-cloud.com/signup)
2. Click -> `Create Application`
	- Put any name for your application
	- Set Device type -> `Raspberry Pi 4`
	- Set Application type -> `Starter`
	- Click -> `Create new application`
3. Click -> `Add device`
	- Set Device type -> `Raspberry Pi 4`
	- Set OS type -> `balenaOS`
	- Select the recommended version
	- Set edition -> `Production`
4. Edit Network Connection
	- Set Connection -> `Wifi+Ethernet`
	- Set your Wifi SSID
	- Set your Wifi Password

Now, download your image file. You should have a zipped image file.

## Install image in Raspberry Pi
### Download BalenaEtcher
We can flash the OS in a microSD is using different system and third-party tools. The easiest way to do it is using **`balenaEtcher`**, which is a cross platform tool and it can flash an OS in a microSD within minutes. It can be downloaded from the [balena official site](https://www.balena.io/etcher/)

### Flash the MicroSD
Insert the memory card in a card reader and attach to your working computer. Then, launch `balenaEtcher`; and flash in three steps:

1. Select the downloaded Image file from your downloaded location
2. Select the flash drive from the options
3. Click `Flash` and wait for the success notification.

**Note**, you can flash multiple Raspberry Pi device with the same image file.


## Find device in Dashboard
After powering up the device(s), the devices will connect to the Wifi automatically. Now, check your dashboard and wait for the device(s) to show up.

I added three devices and the dashboard looks like as follows:


<figure>
	<a href="https://live.staticflickr.com/65535/49803482718_713ee46128_b.jpg"><img src="https://live.staticflickr.com/65535/49803482718_713ee46128_b.jpg"></a></figure>



## Reference:
1. [Get started with Raspberry Pi 4 and Python](https://www.balena.io/docs/learn/getting-started/raspberrypi4-64/python/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzk0MzIxMzYxLDY4NTUyNTE0NF19
-->