---
layout: single
title: "Remove Copyright Information from the ACM sigconf template"
header:
  image: "https://live.staticflickr.com/65535/51205458808_32b32577cb_c.jpg"
  teaser: "https://live.staticflickr.com/65535/51205458808_32b32577cb_c.jpg"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Template
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA0MzQwNTg5NCwxOTY5NDc3NzM0LDQzNT
Q2NTM2N119
-->