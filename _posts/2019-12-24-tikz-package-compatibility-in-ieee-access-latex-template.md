---
layout: single
title: "[solved] `tikz` package causing error in IEEE Access template"
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
eyJoaXN0b3J5IjpbNzA1OTQ3MywyMTM5NDIyODIzLDIwNTQ5MD
k4MzEsLTEyODM2MjY1MjZdfQ==
-->