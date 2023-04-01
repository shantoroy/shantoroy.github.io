---
layout: single
title: "[solved] `tikz` package causing error in IEEE Access template"
excerpt:  "If you are working on a LaTeX document using the IEEE Access template and have run into an error caused by the `tikz` package, you are not alone. In this blog post, we will discuss the reason behind this error and provide a simple solution to fix it. I'll also provide some background information on the IEEE Access template and how to use it. So, let's get started!"
seo_title:  Your  meta  title  
seo_description:  Your  meta  description
header:
  image: "https://live.staticflickr.com/65535/49273391188_54c1ce853b_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49273391188_54c1ce853b_h.jpg"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - pgfplot
  - tikz
  - IEEE Access
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

One of my previous collaborators was having an issue while adding the `tikz` package to the `IEEE Access` template. Later I looked into the problem and tried the existing solutions available online. However, none of those worked alone and I had to summarize the solution. Here is how I solved the problem.
## Required packages for plotting 
```latex
\usepackage{pgfplots}
\usepackage{pgfplotstable}
\pgfplotsset{compat=1.7}
\usepackage{tikz}
```
Usually the `\usepackage{tikz}` arises an issue if included in the `IEEE Access` Latex template.
The solutions available in the net have several issues and I had a tough time figuring out which works better. Later I summarized the solution in just two steps and it works fine now. The solution template is available in a modified short [Overleaf IEEE Access Template](https://www.overleaf.com/read/gkvjydqjnjdn).

## Solution
* In `ieeeaccess.cls` file -> change `\def\year` to `\def\Year`
* In `access.tex` file -> add the following after `\usepackage{tikz}`
	```latex
	\NewSpotColorSpace{PANTONE}
	\AddSpotColor{PANTONE} {PANTONE3015C} {PANTONE\SpotSpace 3015\SpotSpace C} {1 0.3 0 0.2}
	\SetPageColorSpace{PANTONE}
	```
Now, you are all set. Once again, you can access and download the modified files from the modified [Overleaf IEEE Access Template](https://www.overleaf.com/read/gkvjydqjnjdn).

## Reference
[# tikz package causing error in IEEE access template](https://tex.stackexchange.com/questions/440422/tikz-package-causing-error-in-ieee-access-template)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkwNjU2ODAxMiw3MDU5NDczLDIxMzk0Mj
I4MjMsMjA1NDkwOTgzMSwtMTI4MzYyNjUyNl19
-->