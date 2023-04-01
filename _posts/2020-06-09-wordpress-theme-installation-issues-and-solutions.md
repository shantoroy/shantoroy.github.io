---
layout: single
title: "Fixing Wordpress Theme Installation Issue in macOS"
excerpt: "" 
seo_title:  Your  meta  title  
seo_description:  Your  meta  description
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
eyJoaXN0b3J5IjpbLTE3NjExODAxNzUsLTE2MTIzMTY1NTJdfQ
==
-->