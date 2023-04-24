---
layout: single
title: "How to Enable Facebook Comments Plugin in Jekyll Blog Posts"
excerpt:  "Are you looking to integrate Facebook comments on your Jekyll blog? This blog post will guide you through the steps required to enable Facebook comments plugin in Jekyll. By following these steps, you can easily integrate the Facebook commenting system into your Jekyll blog and allow your readers to share their thoughts and feedback on your blog posts. So, let's get started!"
seo_title:  "How to Enable Facebook Comments Plugin in Jekyll Blog Posts"
seo_description:  "Learn how to easily integrate the Facebook commenting system into your Jekyll blog and allow your readers to share their thoughts and feedback on your blog posts. Follow these steps to enable Facebook comments plugin in Jekyll."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
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


## Related Posts on Jekyll/ Minimal Mistakes
* [Google Adsense in Jekyll Static Site or Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/how-I-added-google-adsense-to-my-jekyll-minimal-mistakes-blog/)
* [Google Analytics in Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/google-analytics-in-jekyll-minimal-mistakes-blog-theme/)
* [Minimal Mistakes Cheat Sheet: Code Snippets I use to Blog using Jekyll and the Minimal Mistakes Theme](https://shantoroy.com/jekyll/code-snippets-I-use-for-blogging-in-minimal-mistakes/)
* [Jekyll SEO: How to Find and Fix 404 Error on a Jekyll (Minimal Mistakes) Blog Website](https://shantoroy.com/jekyll/jekyll-seo-find-and-fix-404-error-on-jekyll-minimal-mistake-blog/)
* [Medium: How to Effectively Perform Search Engine Optimization to a Jekyll (Minimal Mistakes) Blog Post Header](https://medium.com/@shantoroy/how-to-effectively-perform-search-engine-optimization-to-a-jekyll-minimal-mistakes-blog-post-9c3a17865eca)
* [How to Add Latex Math to Jekyll-based Theme- Minimal Mistakes](https://shantoroy.com/jekyll/add-latex-math-to-jekyll-blog-minimal-mistakes/)
* [Tools and Platforms I use for Blogging](https://shantoroy.com/blog/tools-I-use-for-blogging/)
* [How to install Jekyll with the Minimal Mistakes Theme in macOS](https://shantoroy.com/blogging/install-jekyll-minimal-mistakes-in-macos/)


## References
* [Comments Moderation using Facebook Comment Plugin](https://developers.facebook.com/docs/plugins/comments)
* [Comments Plugin Moderation Tool not working](https://stackoverflow.com/questions/9120814/comments-plugin-moderation-tool-not-working)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NTk4ODIzNywxNTk0MDA0NzY4LDE4Nz
UyMjMzNjgsMTk1MTA4NTkwNSwyMDU1NDYwNjI1XX0=
-->