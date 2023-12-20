---
layout: single
title: "Google Adsense in Jekyll Static Site or Minimal Mistakes Blog Theme"
excerpt:  "If you're running a Jekyll static site or a blog using the Minimal Mistakes theme, you may be wondering how to incorporate Google Adsense to monetize your site. In this tutorial, I'll walk you through the process of setting up Google Adsense on your Jekyll or Minimal Mistakes site, and show you how to add ad units to your posts."
seo_title:  "How to Add Google Adsense to Jekyll Static Site or Minimal Mistakes Blog Theme"
seo_description:  "Learn how to monetize your Jekyll static site or blog built with the Minimal Mistakes theme by adding Google Adsense. This tutorial will guide you through the steps to set up and add ad units to your posts."
header:
  image: "https://live.staticflickr.com/65535/51703105884_43aa3f4b4d_o.png"
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
Happy blogging!!!

If you find this post helpful, and want to support this blog, you can
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="shantoroy" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script> or

<div style="width: 300px; height: 200px;">
<form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="business" value="Q9F45GULUSYMY" />
<input type="hidden" name="no_recurring" value="0" />
<input type="hidden" name="item_name" value="I appreciate your support! 😊" />
<input type="hidden" name="currency_code" value="USD" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
</form></div>


## Related Posts on Jekyll/ Minimal Mistakes

* [Google Analytics in Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/google-analytics-in-jekyll-minimal-mistakes-blog-theme/)
* [How to Enable Facebook Comments Plugin in Jekyll Blog Posts](https://shantoroy.com/jekyll/facebook-comment-plugin-jekyll-minimal-mistakes-blog-posts/)
* [Minimal Mistakes Cheat Sheet: Code Snippets I use to Blog using Jekyll and the Minimal Mistakes Theme](https://shantoroy.com/jekyll/code-snippets-I-use-for-blogging-in-minimal-mistakes/)
* [Jekyll SEO: How to Find and Fix 404 Error on a Jekyll (Minimal Mistakes) Blog Website](https://shantoroy.com/jekyll/jekyll-seo-find-and-fix-404-error-on-jekyll-minimal-mistake-blog/)
* [Medium: How to Effectively Perform Search Engine Optimization to a Jekyll (Minimal Mistakes) Blog Post Header](https://medium.com/@shantoroy/how-to-effectively-perform-search-engine-optimization-to-a-jekyll-minimal-mistakes-blog-post-9c3a17865eca)
* [How to Add Latex Math to Jekyll-based Theme- Minimal Mistakes](https://shantoroy.com/jekyll/add-latex-math-to-jekyll-blog-minimal-mistakes/)
* [Tools and Platforms I use for Blogging](https://shantoroy.com/blog/tools-I-use-for-blogging/)
* [How to install Jekyll with the Minimal Mistakes Theme in macOS](https://shantoroy.com/blogging/install-jekyll-minimal-mistakes-in-macos/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU2MjQ0NDQ0OCwtMTcxNTI3ODM3Ml19
-->