---
layout: single
title: "[solved] `tikz` package causing error in IEEE Access template"
excerpt:  "If you are working on a LaTeX document using the IEEE Access template and have run into an error caused by the `tikz` package, you are not alone. In this blog post, we will discuss the reason behind this error and provide a simple solution to fix it. I'll also provide some background information on the IEEE Access template and how to use it. So, let's get started!"
seo_title:  "[Solved] Tikz Package Causing Error in IEEE Access Template"  
seo_description:  "Are you facing an error while using the `tikz` package in your LaTeX document using the IEEE Access template? Don't worry, we have got you covered. Read this blog post to learn the reason behind the error and how to fix it. Also, get some useful insights on the IEEE Access template and its usage."
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
* [tikz package causing error in IEEE access template](https://tex.stackexchange.com/questions/440422/tikz-package-causing-error-in-ieee-access-template)


## Related Posts on Latex
You can find a comprehensive list of Latex resources in the following post:

[Latex Resources in a Nutshell](https://shantoroy.com/latex/latex-resources-in-a-nutshell/)

If you are a new Latex user, check out this post:
[20 Most Common Mistakes Made by New Latex Users](https://shantoroy.com/latex/common-mistakes-made-by-new-latex-typesetting-users/)

You can find all `Latex` oriented posts of mine in: [https://shantoroy.com/categories/#latex](https://shantoroy.com/categories/#latex)

* [Add Copyright Notice and Conference Name in IEEE Conference Template](https://shantoroy.com/latex/add-copyright-conference-name/)
* [Preparing Tables for Publication and Documentation in Latex](https://shantoroy.com/latex/how-to-create-tables-in-latex/)
* [Creating Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)
* [How to write an algorithm in Latex](https://shantoroy.com/latex/how-to-write-algorithm-in-latex/)
* [How to add subfigure in Latex](https://shantoroy.com/latex/how-to-add-subfig-in-latex/)
* [How to Write Matrix with Row/Column Labels in Latex](https://shantoroy.com/latex/matrix-labeling-in-latex/)
* [How to Collaboratively Write a Paper using Overleaf Latex Platform](https://shantoroy.com/latex/how-to-collaborately-write-a-paper-using-latex-overleaf/)
* [Itemize, Enumerate, and To-do-list in Latex](https://shantoroy.com/latex/playing-with-latex-itemize-enumerate-fontawesome/)
* [Latex Table for Survey in IEEE two-column format](https://shantoroy.com/latex/latex-table-for-survey-ieee-template/)
* [Line Plotting using Latex PGFPlots](https://shantoroy.com/latex/how-to-draw-line-graph-using-pgfplots-latex/)
* [How to add Codes in Latex:  `listings`  package for code documentation](https://shantoroy.com/latex/how-to-add-codes-in-latex-listing-package/)
* [Bibliography management with Bibtex in Latex](https://shantoroy.com/latex/bibliography-management-with-bibtex/)
* [Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot](https://shantoroy.com/latex/multiple-line-plots-using-tikz-pgfplot/)
* [How to Draw a Literature Survey Taxonomy Tree in Latex](https://shantoroy.com/latex/Draw-literature-survey-tree-in-latex/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MTg2MDI3Niw3MDU5NDczLDIxMzk0Mj
I4MjMsMjA1NDkwOTgzMSwtMTI4MzYyNjUyNl19
-->