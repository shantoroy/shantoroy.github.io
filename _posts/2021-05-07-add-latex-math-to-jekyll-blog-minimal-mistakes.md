---
layout: single
title: "How to Add Latex Math to Jekyll-based Theme- Minimal Mistakes"
excerpt:  "Learn how to add LaTeX math equations to Jekyll-based theme Minimal Mistakes with just a few easy steps! This tutorial will guide you through the process, allowing you to seamlessly integrate math equations into your blog posts."
seo_title:  "How to Add LaTeX Math Equations to Jekyll-based Theme - Minimal Mistakes"
seo_description:  "Are you struggling to add LaTeX math equations to your Jekyll-based blog posts? Look no further than this step-by-step tutorial on integrating math equations into your Minimal Mistakes theme. Discover how easy it can be to create professional-looking math formulas on your blog!"
header:
  image: "https://live.staticflickr.com/65535/51227438353_7a68113b99_w.jpg"
  teaser: "https://live.staticflickr.com/65535/49316271662_9c8b200cb6_h.jpg"
categories:
  - Jekyll
tags:
  - Jekyll
  - Latex
  - Minimal Mistakes
  - Tutorial
  - Math
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Recently, I was trying to add a few mathematical equations in the bolg posts. However, the equations were not working well. I looked for some tutorials, and found the following solutions:

1. Add the following to the `_includes/scripts.html`

	```html
		{% if page.mathjax %}
	<script type="text/javascript" async
	  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-MML-AM_CHTML">
	</script>

	<script type="text/x-mathjax-config">
	   MathJax.Hub.Config({
	     extensions: ["tex2jax.js"],
	     jax: ["input/TeX", "output/HTML-CSS"],
	     tex2jax: {
	       inlineMath: [ ['$','$'], ["\\(","\\)"] ],
	       displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
	       processEscapes: true
	     },
	     "HTML-CSS": { availableFonts: ["TeX"] }
	   });
	</script>
	{% endif %}
	```
	 it says that if the `mathjax` is enabled in the pages, it will render the equations using the package. And based on [this blog post](https://sort-care.github.io/Latex-on-Blog/), it became easier to use usual formats and notations we use in latex.

2. Add `mathjax: true` in the default post configuration section of the `_config.yml` file as follows:

	```
	# Defaults
	defaults:
	  # _posts
	  - scope:
	      path: ""
	      type: posts
	    values:
	      layout: single
	      author_profile: true
	      read_time: true
	      comments: true
	      share: true
	      related: true
	      mathjax: true
	```
	check the last line, I have enabled `mathjax` as true.

And, now you are good to go. If you need to check the configuration files, you can visit [my repository](https://github.com/shantoroy/shantoroy.github.io) to see how I configured.

A few suggestions:
* Use `\vert` as the pipe symbol rather than using `|` within the math expressions. Sometimes it does not work.
* I prefer `$ $` for inline expression (math within paragraph)
* Other than that, you can use `$$ $$` for equations that are not within the paragraphs.

That's it! Have a good day.




**References**
- [How to render math equations on your Minimal Mistakes](https://www.cross-validated.com/How-to-render-math-on-Minimal-Mistakes/)
- [Building a Personal Site with Jekyll & Minimal Mistakes](http://www.pwills.com/posts/2017/12/20/website.html)
- [Add Latex Support for Minimal Mistakes](https://sort-care.github.io/Latex-on-Blog/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MDk0Nzk0MDksLTkzMjE1Mjg2MV19
-->