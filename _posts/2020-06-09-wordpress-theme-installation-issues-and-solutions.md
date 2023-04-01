---
layout: single
title: "Fixing Wordpress Theme Installation Issue in macOS: Writing Content Permission Issue"
excerpt: "If you are a Wordpress user and have faced issues while installing a new theme on your macOS, you are not alone. The process can be complicated, especially if you are not familiar with the software's requirements. However, there are some easy steps you can follow to fix the problem quickly. In this blog post, I will guide you through the process of fixing Wordpress theme installation issues in macOS." 
seo_title:  "Fixing Wordpress Theme Installation Issue in macOS - A Step-by-Step Guide"
seo_description: "Are you struggling to install a new theme on your Wordpress site using a macOS device? This blog post provides a step-by-step guide to help you fix the issue quickly and easily. Whether you are new to the software or an experienced user, our guide will provide you with everything you need to know to get your Wordpress theme installed and running smoothly on your macOS device."
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/52010965276_faf5ae76ef_o.png"
categories:
  - Wordpress
tags:
  - Wordpress
  - Tutorial
  - macOS
  - XAMPP
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post explains the way of fixing the issue of being unable to install Wordpress themes"
---



If you have installed wordpress in macOS and now are being unable to install wordpress themes, this post is for you.

The reason behind this issue is quite simple. macOS does not permit to write contents from Wordpress unless changes the default permission.

### GUI
First, check the permission by going to the 
`/Applications/xampp/xamppfiles/` and then finding the **htdocs** folder. Right click on this folder. Then select **Get Info** and find the permissions at the bottom of the dialogue box. Then select everyone and permit **Read & Write**.

### Terminal
Alternatively, you can do the same thing from terminal using the following commands
```
$ cd /Applications/XAMPP/xamppfiles/
$ sudo chown -R daemon htdocs
$ sudo chmod -R g+w htdocs
```

Once you allow `write` permission for the folder, you are good to go. Try installing themes now and that should work properly.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMxOTc2NTMxNiwtMTYxMjMxNjU1Ml19
-->