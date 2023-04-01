---
layout: single
title: "How to Remove Copyright Information from the ACM sigconf template"
excerpt:  "Are you tired of manually removing the ACM sigconf template's copyright information from your research papers or latex documents like reports or homeworks? This can be a tedious task, especially when you need to prepare multiple documents for different conferences or purposes. Fortunately, there is an easy way to remove it."
seo_title:  "How to Remove Copyright Information from the ACM sigconf Template"
seo_description: "Learn how to quickly and easily remove the copyright information from the ACM sigconf template with the steps mentioned in the blog post. Save time and streamline your paper preparation process with this helpful guide."
header:
  image: "https://live.staticflickr.com/65535/51205458808_32b32577cb_c.jpg"
  teaser: "https://live.staticflickr.com/65535/51205458808_32b32577cb_c.jpg"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Template
  - ACM
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


The ACM emplate is pretty cool, and a lot of the students use it to submit assignments or write the initial paper. However, the copyright information in the first page is kinda boring and we want to remove that sometimes. 

Here, in this post, we will see how to remove the copyright information, and add page numbers at the bottom of each page in the template. You can also check my [Overleaf](https://www.overleaf.com/read/jfyggffthwqk) version.

### Remove Copyright from the first page
Add the following lines after your package list, and that will remove the copyright information from the first page. 
```latex
\setcopyright{none}
\settopmatter{printacmref=false} % Removes citation information below abstract
\renewcommand\footnotetextcopyrightpermission[1]{} % removes footnote with conference information in first column
\pagestyle{plain}
```

### Add page number in the bottom
People can face another issue that sometimes page numbers are missing at the bottom of the template. Just add the `\settopmatter{printfolios=true}` before `\maketitle` and you will find the page numbers in the template.

```latex
\settopmatter{printfolios=true}
\maketitle
```

You can also simply copy my template project in [Overleaf](https://www.overleaf.com/read/jfyggffthwqk) or download from there for offline use. 

## Related Posts
Read my other Latex-related Blog posts!
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5ODgwOTU1MDYsMjA0MzQwNTg5NCwxOT
Y5NDc3NzM0LDQzNTQ2NTM2N119
-->