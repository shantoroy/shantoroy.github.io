---
layout: single
title: "Why you should use Latex Plots in your Reports instead of Matplotlib Plots"
header:
  image: "https://live.staticflickr.com/65535/52104342559_4543d284e9_o.png"
  teaser: "https://live.staticflickr.com/65535/52104342559_4543d284e9_o.png"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Overleaf
  - Tikz
  - matplotlib
  - pgfplot
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
---



When I joined my lab (RNS Lab at UH) and was working for my first publication, I did not know much about latex plots. I have always used matplotlib plots before that paperwork. Even when we submitted in a conference for the first time, we submitted the matplotlib plots as those were in `png` or `pdf` format.

Later, when the paper was not accepted and we had to submit the revides version in the associated workshop of the conference, professor motivated us to try latex plots.

Why! It's because using latex plots have several benifits. 
1. If you have prepared your plots for one column article template, and get rejected from a conference or journal that uses the same template, you may have to modify the figure again to make the figures appear well in a new template (e.g., two-column templates). If you are using latex plots, the work is minimal and you are still getting the best quality graph without thinking much about the size of the figure and ratio of the texts.

2. Font sizes are always a major concern when saved the image from matplotlib. Here, using latex plots you don't have to work much. Most cases, it just matches the document font size itself.

3. Using matplotlib image, you have to generate an image, save it, upload it to the overleaf project, and so on. Using latex plot, you don't need to go through these extra processes for each image.

4. In many digital libraries, specially in the IEEE Xplorer, they want to match the font-family of the figures with the document font-family. If that doesn't match, you get an error when preparing the camera-ready submission. using latex plots, you don't have these issues since it directly uses the document font-family.

Most of all the `pgfplot` and `tikz` libraries provide excellent graphs that you can use in your report or article. there are numerous templates that you can directly use with your own data. 

Now, when writing a new report, I always look for latex plots. And there is a new python module I have found that makes it a lot easier. Yay!

<iframe src="https://giphy.com/embed/11sBLVxNs7v6WA" width="480" height="217" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cheer-cheering-11sBLVxNs7v6WA"></a></p>

So, there's a new module named [tikzplotlib](https://github.com/texworld/tikzplotlib) that helps you convert your matplotlib code into a latex code. i will cover more details in this following post:

That's all for today! cheers!!!

<iframe src="https://giphy.com/embed/ZIzN7YWNuTUYg" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/the-lizzie-bennet-diaries-tlbd-thelbd-ZIzN7YWNuTUYg">via Giphy</a></p>
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA2MDg0OTk3NSw2MjY5OTUzOTYsLTEwND
AxODU1MTRdfQ==
-->