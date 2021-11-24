---
layout: single
title: "Google Adsense in Jekyll Static Site or Minimal Mistakes Blog Theme"
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/51703105884_43aa3f4b4d_o.png"
categories:
  - jekyll
tags:
  - Blog
  - Jekyll
  - github-pages
  - Minimal Mistakes
  - Adsense
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post explains the way of setting up your minimal mistakes theme blog so that you can optimize your site using Google Adsense."
---




If you are blogging using the popular jekyll theme [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes), this post will help you adding your google adsense on your site.


## Google Adsense Account

First open an account in [Google Adsense](https://www.google.com/adsense/start/) and create codes for your ads. Google adsense provides different custom size ad codes (horizontal/vertical advertisements units). You can follow the steps:

1. Click on `New ad unit` under `Ad Units` from `my ads`
2. Select `text and display ads`
3. Name the unit after previewing how the ad will appear on your site
4. Click on `Get Code` visible on your unit. The code looks like as follows
```js
<script async  src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>  
<!-- Single post - 1 (yourwebsite.com) -->  
<ins  class="adsbygoogle"  
		style="display:block"  
		data-ad-client="0123456789012345"  
		data-ad-slot="01234567"  
		data-ad-format="auto"></ins>  
<script>  
	(adsbygoogle  =  window.adsbygoogle  ||  []).push({});  
</script>
```

## Add Ad Code to Site
 
I have included codes of two ad units under the `_includes` directory. Simply add the code you got earlier in a `<filename>.html` file and put that under `_includes` directory. If you go to my [site repository directory](https://github.com/shantoroy/shantoroy.github.io/tree/master/_includes), you will find two files named `advertisements.html` and `vertical_advertisement.html`.

Now, since I use the `single.html` layout for my posts, I have included these ad pages in different locations under class `page__content`. The code now looks like as follows

```html
<section class="page__content" itemprop="text">
{% if page.toc %}
<aside class="sidebar__right">
<nav class="toc">
<header><h4 class="nav__title"><i class="fas fa-{{ page.toc_icon | default: 'file-text' }}"></i> {{ page.toc_label | default: site.data.ui-text[site.locale].toc_label }}</h4></header>
{% include toc.html sanitize=true html=content h_min=2 h_max=3 class="toc__menu" %}
</nav>
{% include vertical_advertisement.html %}
</aside>
{% endif %}
{{ content }}
{% include advertisements.html %}
{% if page.link %}<div><a href="{{ page.link }}" class="btn btn--primary">{{ site.data.ui-text[site.locale].ext_link_label | default: "Direct Link" }}</a></div>{% endif %}
</section>
```

So, you see, I have added the `vertical ad unit` after the `table of contents` and added another (`horizontal ad unit`) after the content. You can place ads in different places based on where you exactly want this ads to show up. You just need to add this code

```markdown
{% include advertisements.html %}
```

If you want to know how to track your website or blog using `Google Analytics`, feel free to read my other post:
[Google Analytics in Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/google-analytics-in-jekyll-minimal-mistakes-blog-theme/)

Keep growing your audience and earning some passive money. 
Happy blogging!!! :sunglasses:
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY0NzAwODA3XX0=
-->