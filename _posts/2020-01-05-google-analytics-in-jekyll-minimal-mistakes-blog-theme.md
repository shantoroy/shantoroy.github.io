---
layout: single
title: "Google Analytics in Minimal Mistakes Blog Theme"
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
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
excerpt: "This post explains the way of setting up your minimal mistakes theme blog so that you can optimize your site using Google Analytics."
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


## References
1. https://github.com/mmistakes/minimal-mistakes/issues/85
2. https://mmistakes.github.io/minimal-mistakes/docs/configuration/#seo-social-sharing-and-analytics-settings
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgzNzg3ODYzLC0zOTI5ODM3MzEsLTE4ND
UxNTM4MDZdfQ==
-->