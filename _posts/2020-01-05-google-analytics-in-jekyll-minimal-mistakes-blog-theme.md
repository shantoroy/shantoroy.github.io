---
layout: single
title: "Google Analytics in Minimal Mistakes Blog Theme"
excerpt:  "Want to track the performance of your Minimal Mistakes blog? Google Analytics is a powerful tool that can help you to measure your website's traffic, engagement, and more. In this tutorial, you will learn how to set up Google Analytics in your Minimal Mistakes blog, track your blog's performance, and gain insights into your audience's behavior."
seo_title:  "Google Analytics in Minimal Mistakes Blog Theme"
seo_description:  "Learn how to add Google Analytics to your Minimal Mistakes blog theme and track your website's performance, traffic, and audience behavior. This tutorial will guide you through the process of setting up Google Analytics and using its features to gain insights into your blog's performance."
header:
  image: "https://live.staticflickr.com/65535/51702645308_89b0e0fe5a_o.png"
  teaser: "https://live.staticflickr.com/65535/51702645308_89b0e0fe5a_o.png"
categories:
  - jekyll
tags:
  - Blog
  - Jekyll
  - github-pages
  - Minimal Mistakes
  - Analytics
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



If you are blogging using the popular jekyll theme [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes), this post will help you adding your google analytics tracking code on your site.

First open an account in [Google Analytics](https://analytics.google.com/) and create a new stream using your website/blog URL. Google Analytics currently provides a `g-tag` for a site and you have to add the tag to your site. Therefore, you will find a tracking code like `G-1234567890` associated with the stream.

 First, make sure if you have the `google-gtag.html` file in your repository. The following script named `google-gtag` is already provided in the [official repository analytics folder](https://github.com/mmistakes/minimal-mistakes/tree/master/_includes/analytics-providers).

```markdown
<!-- Global site tag (gtag.js) - Google Analytics -->

<script async src="https://www.googletagmanager.com/gtag/js?id={{ site.analytics.google.tracking_id }}"></script>

<script>

window.dataLayer = window.dataLayer || [];

function gtag(){dataLayer.push(arguments);}

gtag('js', new Date());

gtag('config', '{{ site.analytics.google.tracking_id }}', { 'anonymize_ip': {{ site.analytics.google.anonymize_ip | default: false }}});

</script>
```



Now, add the tracking code to the `_config.yml` file under `tracking_id` option.
```yml
analytics:
  provider: "google-gtag"
  google:
    tracking_id: "G-1234567890"
    anonymize_ip: false # default
```


Or you can add the code in a `custom.html` file and select `provider: "custom"` in the `_config.yml` file.

If you want to read how to add `Google Adsense` in minimal mistakes theme, feel free to read the following post:

[Google Adsense in Jekyll Static Site or Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/how-I-added-google-adsense-to-my-jekyll-minimal-mistakes-blog/)


## Related Posts on Jekyll/ Minimal Mistakes
* [Google Adsense in Jekyll Static Site or Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/how-I-added-google-adsense-to-my-jekyll-minimal-mistakes-blog/)
* [How to Enable Facebook Comments Plugin in Jekyll Blog Posts](https://shantoroy.com/jekyll/facebook-comment-plugin-jekyll-minimal-mistakes-blog-posts/)
* [Minimal Mistakes Cheat Sheet: Code Snippets I use to Blog using Jekyll and the Minimal Mistakes Theme](https://shantoroy.com/jekyll/code-snippets-I-use-for-blogging-in-minimal-mistakes/)
* [Jekyll SEO: How to Find and Fix 404 Error on a Jekyll (Minimal Mistakes) Blog Website](https://shantoroy.com/jekyll/jekyll-seo-find-and-fix-404-error-on-jekyll-minimal-mistake-blog/)
* [Medium: How to Effectively Perform Search Engine Optimization to a Jekyll (Minimal Mistakes) Blog Post Header](https://medium.com/@shantoroy/how-to-effectively-perform-search-engine-optimization-to-a-jekyll-minimal-mistakes-blog-post-9c3a17865eca)
* [How to Add Latex Math to Jekyll-based Theme- Minimal Mistakes](https://shantoroy.com/jekyll/add-latex-math-to-jekyll-blog-minimal-mistakes/)
* [Tools and Platforms I use for Blogging](https://shantoroy.com/blog/tools-I-use-for-blogging/)
* [How to install Jekyll with the Minimal Mistakes Theme in macOS](https://shantoroy.com/blogging/install-jekyll-minimal-mistakes-in-macos/)

## References
1. [https://github.com/mmistakes/minimal-mistakes/issues/85](https://github.com/mmistakes/minimal-mistakes/issues/85)
2. [SEO Social Sharing and Analytics Settings](https://mmistakes.github.io/minimal-mistakes/docs/configuration/#seo-social-sharing-and-analytics-settings)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY4ODU5NTY2NywtODM3ODc4NjMsLTM5Mj
k4MzczMSwtMTg0NTE1MzgwNl19
-->