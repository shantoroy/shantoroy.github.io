---
layout: single
title: "Minimal Mistakes Cheat Sheet: Code Snippets I use to Blog using Jekyll and the Minimal Mistakes Theme"
excerpt:  "Looking for a cheat sheet to improve your Jekyll-based blog using the Minimal Mistakes theme? In this blog post, I share some code snippets that I use to enhance my blogging experience, from adding posts from social medias and text formatting to adding syntax highlighting to code snippets."
seo_title:  "Minimal Mistakes Cheat Sheet: Code Snippets I use to Blog using Jekyll and the Minimal Mistakes Theme"
seo_description:  "Looking to enhance your Jekyll-based blog using the Minimal Mistakes theme? Check out this cheat sheet, which features code snippets for adding posts from social medias, text formatting, adding syntax highlighting to code snippets, and more!"
header:
  image: "https://live.staticflickr.com/65535/52099493299_0bbdfc4b68_o.png"
  teaser: "https://live.staticflickr.com/65535/52099493299_0bbdfc4b68_o.png"
categories:
  - Jekyll
tags:
  - Minimal Mistakes
  - Tutorial
  - Cheatsheet
  - Blogging
  - Snippets
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---
In this post, I will include the small snippets I use most while writing a blog post in my blog. 

I assume you have already found out that I have been using a jekyll theme for blogging which requires `markdown` commands to write a post. The theme I have been using from the beginning is [minimal mistakes](https://mmistakes.github.io/minimal-mistakes/) which is actively maintained in this [Github repository](https://github.com/mmistakes/minimal-mistakes).

The reasons I prefer a static blog template over [Wordpress](https://wordpress.com/) is:
* It is very lightweight
* Has no cost for hosting (if you are using [github-pages](https://pages.github.com/)). And in github, you can have up to 100GB for your repository.
* You can easily perform SEO, add adsense, and comment platforms here as well

Now, let's jump to the main topic. Here, I list some most common snippet templates in my blog posts:

## Header
This is how I add the header of a blog post. You can see the title, header image, teaser, category, tags, and whether I enable the table of contents or not. I modify each based on the post I am writing.
```
---
layout: single
title: "A Basic Keylogger in Python"
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/51211036232_6916bf5c10_c.jpg"
categories:
  - Security
tags:
  - Python
  - Tutorial
  - Keylogging
  - Keylogger
  - Trojan Horse
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post explains the basic syntax of matplotlib module for data visualization."
---
```


## Figures
Here is the code for adding a figure. You can keep images in the same repository under `/assets/images` subdirectory. However, I prefer keeping images in [flickr](https://www.flickr.com/) and then I just use the image source here under the `figure` block.
### Basic Code
```
<figure>
  <a href="https://live.staticflickr.com/65535/51226516036_e486b2a319_w.jpg"><img src="https://live.staticflickr.com/65535/51226516036_e486b2a319_w.jpg"></a>
</figure>
<br/>
```

#### Output
<figure>
  <a href="https://live.staticflickr.com/65535/51226516036_e486b2a319_w.jpg"><img src="https://live.staticflickr.com/65535/51226516036_e486b2a319_w.jpg"></a>
</figure>
<br/>

### More Configurations
```
<figure style="width: 90%" class="align-center">
  <a href="https://live.staticflickr.com/65535/51226516036_e486b2a319_w.jpg" title="The Pixel Tracker logo" alt="The Pixel Tracker logo">
  <img src="https://live.staticflickr.com/65535/51226516036_e486b2a319_w.jpg" alt=""></a>
  <figcaption>Image caption.</figcaption>
</figure>
```

#### Output
<figure style="width: 80px" class="align-center">
  <a href="https://live.staticflickr.com/65535/51226516036_e486b2a319_w.jpg" title="The Pixel Tracker logo" alt="The Pixel Tracker logo">
  <img src="https://live.staticflickr.com/65535/51226516036_e486b2a319_w.jpg" alt=""></a>
  <figcaption>Image caption.</figcaption>
</figure>




## Embedding
Sometime, I need to embed a youtube video or instagram image. Here's the example codes for embedding video or image from other platforms.
### Youtube Embedding Snippet
```
<iframe src="https://www.youtube.com/embed/rbdtSpc_NyE" width="560" height="315" frameborder="0"> </iframe>
<br/>
```

#### Output
<iframe src="https://www.youtube.com/embed/rbdtSpc_NyE" width="560" height="315" frameborder="0"> </iframe>
<br/>

### Instagram Embedding Snippet
```
<iframe src="https://www.instagram.com/p/CUtm-wTANz2/embed" width="560" height="580" frameborder="0"> </iframe>
```
#### Output
<iframe src="https://www.instagram.com/p/CUtm-wTANz2/embed" width="560" height="580" frameborder="0"> </iframe>


### Giphy Gifs
```
<img src="https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif" width="40%" height="40%" />
```

#### Output
<img src="https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif" width="40%" height="40%" />


### Github Gist
```
<script src="https://gist.github.com/shantoroy/9bb4da0b2a281e3c91cc836045b6c74d.js"></script>
```
#### output
<script src="https://gist.github.com/shantoroy/9bb4da0b2a281e3c91cc836045b6c74d.js"></script>




## Other Minimal Mistakes Blogs
Here are a few other blogs that are using the `Minimal Mistakes` theme. You can get inspiration by looking at how people are prefering this template for publishing their blogs.
1. [https://www.gurucharan.in/blog/blogging-as-a-developer/](https://www.gurucharan.in/blog/blogging-as-a-developer/)
2. [https://www.cross-validated.com/Personal-website-with-Minimal-Mistakes-Jekyll-Theme-HOWTO-Part-IV/](https://www.cross-validated.com/Personal-website-with-Minimal-Mistakes-Jekyll-Theme-HOWTO-Part-IV/)
([Github](https://github.com/k-bosko/k-bosko.github.io))






## Troubleshooting

* If there is an error (tag not ended properly), most probably it's because there is `%` in the code snippet.




## CheatSheet/Help
If you are looking for more snippets, just go visit this page:
* [https://www.fabriziomusacchio.com/blog/2021-08-11-Minimal_Mistakes_Cheat_Sheet/#via-html](https://www.fabriziomusacchio.com/blog/2021-08-11-Minimal_Mistakes_Cheat_Sheet/#via-html)


## Related Posts on Jekyll/ Minimal Mistakes
* [Google Adsense in Jekyll Static Site or Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/how-I-added-google-adsense-to-my-jekyll-minimal-mistakes-blog/)
* [Google Analytics in Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/google-analytics-in-jekyll-minimal-mistakes-blog-theme/)
* [How to Enable Facebook Comments Plugin in Jekyll Blog Posts](https://shantoroy.com/jekyll/facebook-comment-plugin-jekyll-minimal-mistakes-blog-posts/)
* [Jekyll SEO: How to Find and Fix 404 Error on a Jekyll (Minimal Mistakes) Blog Website](https://shantoroy.com/jekyll/jekyll-seo-find-and-fix-404-error-on-jekyll-minimal-mistake-blog/)
* [Medium: How to Effectively Perform Search Engine Optimization to a Jekyll (Minimal Mistakes) Blog Post Header](https://medium.com/@shantoroy/how-to-effectively-perform-search-engine-optimization-to-a-jekyll-minimal-mistakes-blog-post-9c3a17865eca)
* [How to Add Latex Math to Jekyll-based Theme- Minimal Mistakes](https://shantoroy.com/jekyll/add-latex-math-to-jekyll-blog-minimal-mistakes/)
* [Tools and Platforms I use for Blogging](https://shantoroy.com/blog/tools-I-use-for-blogging/)
* [How to install Jekyll with the Minimal Mistakes Theme in macOS](https://shantoroy.com/blogging/install-jekyll-minimal-mistakes-in-macos/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY3ODQzMDMzNSwxNTQ2NjkyNjEwLC02MD
U5NDA4NDMsNTM4MDQ2NjAxLC04OTE2NTQ4MywtNTIwNDgyMjE2
LDU1NDk1MjM2OSwtNTY1NDcwODY3LC0xMTcxMDgwMjY0XX0=
-->