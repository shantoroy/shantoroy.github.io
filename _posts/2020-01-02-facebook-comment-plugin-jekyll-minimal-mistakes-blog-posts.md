---
layout: single
title: "How to Enable Facebook Comments Plugin in Jekyll Blog Posts"
header:
  image: "https://live.staticflickr.com/65535/49316271662_9c8b200cb6_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49316271662_9c8b200cb6_h.jpg"
categories:
  - Jekyll
tags:
  - Jekyll
  - Facebook-Comments-Plugin
  - Minimal Mistakes
  - Tutorial
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

I enabled the `Facebook-Comments-Plugin` in my blog as a comment provider. Here is how, I enabled it and now managing it.

## Create a Facebook Developer App ID
Go to [Facebook Developer](https://developers.facebook.com/) page and register a web app to receive an App ID. It will take only a minute or two.

## Configure Jekyll in Webpage
Include the following code at the end of the `<body>...</body>` tag. In a simple Jekyll site, put this in the `_layout/default.html`. In case if you are using you will find a different script file in `_includes/comment-providers/facebook.html`; remove previous code and add the following code. Remember to **replace your app ID with mine** at the end of line number 6. Here, `466840033890778` is my App ID.
```html
<div  id="fb-root"></div>
<script>(function(d, s, id) {
var  js, fjs = d.getElementsByTagName(s)[0];
if (d.getElementById(id)) return;
js = d.createElement(s); js.id = id;
js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=466840033890778";
fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
```

## Set Up Comment Moderation
### Include Meta Property in Page
In most of the tutorials, authors included only the following code within the `<head>...</head>` section of the `_layout/default.html` file.
```html
<meta  property="fb:admins"  content="{https://www.facebook.com/shanto.roy.9}"/>
```
However, it did not work. Therefore, I found a new thread in Stack Overflow thread [Comments Plugin Moderation Tool not working] that solves the issue finally. Add all these within the `<head>...</head>` section of the `_layout/default.html` file-
```html
<meta  property="fb:app_id"  content="466840033890778"  />
<meta  property="fb:admins"  content="466840033890778"/>
<meta  property="og:url"  content="URL"  />
<meta  property="og:title"  content="TITLE"  />
<meta  property="og:description"  content="DESC"  />
<meta  property="og:image"  content="IMG"  />
```

### Admin Setup
Go to [https://developers.facebook.com/tools/comments/466840033890778](https://developers.facebook.com/tools/comments/466840033890778) and this is your dashboard. From settings add as many admins as you want who will be able to moderate the comments if logged in their facebook account. Do not forget to **replace my App ID with yours**.

## Configure the YAML front matter
Enable the facebook comments plugin in `_config.yml` file by following instructions provided in the file. In `Minimal Mistakes` theme, it looks like the following:
```yml
comments:
	provider : "facebook"
	facebook:
		appid : 466840033890778
		num_posts : # 5 (default)
		colorscheme : # "light" (default), "dark"
```

Now, you are good to go. Cheers!!!

## References
* [Comments Moderation using Facebook Comment Plugin](https://developers.facebook.com/docs/plugins/comments)
* [Comments Plugin Moderation Tool not working](https://stackoverflow.com/questions/9120814/comments-plugin-moderation-tool-not-working)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk1MTA4NTkwNSwyMDU1NDYwNjI1XX0=
-->