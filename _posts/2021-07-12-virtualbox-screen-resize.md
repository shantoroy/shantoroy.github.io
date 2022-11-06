---
layout: single
title: "How to Fix Ubuntu Automatic Screen Scaling Issue on Virtualbox"
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
eyJoaXN0b3J5IjpbLTczNjQyMjE1OF19
-->