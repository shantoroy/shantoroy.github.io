---
layout: single
title: "Code Snippets I use to Blog using Jekyll and the Minimal Mistakes Theme"
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
<figure style="width: 180px" class="align-center">
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
<iframe src="https://www.instagram.com/p/CUtm-wTANz2/?utm_source=ig_embed" width="560" height="580" frameborder="0"> </iframe>
```
#### Output
<iframe src="https://www.instagram.com/p/CUtm-wTANz2/?utm_source=ig_embed" width="560" height="580" frameborder="0"> </iframe>


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


## Smileys
Sometimes, I like to use smileys in my sentences and here's how you can add in your posts.
```
:sunglasses: 
:wink:
:smiley:
```

#### Output
:sunglasses: 
:wink:
:smiley:

## Other Minimal Mistakes Blogs
Here are a few other blogs that are using the `Minimal Mistakes` theme. You can get inspiration by looking at how people are prefering this template for publishing their blogs.
1. https://www.gurucharan.in/blog/blogging-as-a-developer/
2. https://www.cross-validated.com/Personal-website-with-Minimal-Mistakes-Jekyll-Theme-HOWTO-Part-IV/
([Github](https://github.com/k-bosko/k-bosko.github.io))






## Troubleshooting

* If there is an error (tag not ended properly), most probably it's because there is `%` in the code snippet.




## CheatSheet/Help
If you are looking for more snippets, just go visit this page:
* https://www.fabriziomusacchio.com/blog/2021-08-11-Minimal_Mistakes_Cheat_Sheet/#via-html

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUyMDQ4MjIxNiw1NTQ5NTIzNjksLTU2NT
Q3MDg2NywtMTE3MTA4MDI2NF19
-->