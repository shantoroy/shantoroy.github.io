---
layout: single
title: "How to Fix Ubuntu Automatic Screen Scaling Issue on Virtualbox"
excerpt:  "Are you struggling with Ubuntu's automatic screen scaling issue while using VirtualBox? This can be a frustrating experience, but luckily, there's a solution! In this article, we'll guide you through the steps to fix Ubuntu's automatic screen scaling issue on VirtualBox so you can have a seamless virtualization experience."
seo_title:  "How to Fix Ubuntu Automatic Screen Scaling Issue on VirtualBox"
seo_description:  "Are you tired of dealing with Ubuntu's automatic screen scaling issue on VirtualBox? In this guide, I'll show you how to fix the problem with easy-to-follow steps, so you can enjoy a smooth virtualization experience. Learn how to adjust Ubuntu's screen scaling and resolution settings to match your VirtualBox display settings effortlessly."
header:
  image: "https://live.staticflickr.com/65535/52480457238_8ed90410c1_o.png"
  teaser: "https://live.staticflickr.com/65535/52480457238_8ed90410c1_o.png"
categories:
  - Linux
tags:
  - Linux
  - Ubuntu
  - Virtualbox
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
---


After installing Ubuntu on Virtualbox, sometimes the automatic screen resize option does not work. The screen looks freezed and small.

There is a way to fix this. Just we need to perform the following steps:

1.  Start the VM
2. Click in Devices > Insert Guest Additions CD image...
3.  You'll see a CD icon in your Favorites (left side). Double click on it
4. In the top right there's a button saying "Run Software". Click on it.
5. If not works:
		* right-click anywhere on the folder and click "open with terminal"
		* run `./autorun.sh`
6. Restart the VM

That's all! Cheers!!! :sunglasses:
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjU5NDI5ODcyLC03MzY0MjIxNThdfQ==
-->