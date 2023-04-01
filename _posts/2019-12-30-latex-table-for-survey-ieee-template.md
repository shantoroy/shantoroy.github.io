---
layout: single
title: "Example Template of Latex Table for Literature Survey in Research Survey Papers"
excerpt:  "If you're writing a research survey paper, a well-organized and properly formatted literature survey table is a must-have. A literature survey table summarizes the key characteristics of the surveyed papers in a concise and easy-to-read format. In this post, we'll walk you through the process of creating a literature survey table in LaTeX, including how to define the table's structure, how to populate it with data, and how to add captions and labels."
seo_title:  "Latex Table for Literature Survey in Research Survey Papers"
seo_description:  "Learn how to create a literature survey table in LaTeX for your research survey paper. I'll cover the table structure, data population, and how to add captions and labels for an organized and easy-to-read format. This post provides a nice template for your next survey work."
header:
  image: "https://live.staticflickr.com/65535/49301962946_8eef420816_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49301962946_8eef420816_h.jpg"
categories:
  - Latex
tags:
  - Latex
  - Publication
  - Table
  - Survey
  - IEEE Template
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

In the survey papers, authors usually put a table intending to compare the works based on particular parameters or features. Here is a simple comparison table based on `tabularx` in `IEEE two-column` latex template. 

You will find the code and output in the [Overleaf Document](https://www.overleaf.com/read/bqjtshzgspsj).

N.B. I am not discussing basic about latex table in this post. You can find the basic in my other post:

> [Preparing Tables for Publication and Documentation in Latex](https://shantoroy.com/latex/how-to-create-tables-in-latex/)

## Prerequisite 
Include the following packages and define column type as follows:


```latex
\usepackage{graphicx}
\usepackage{tabularx,booktabs}
\usepackage{dingbat}
\usepackage{diagbox}
\newcolumntype{C}{>{\centering\arraybackslash}X}
\setlength{\extrarowheight}{1pt}
```
`dingbat` is not required if you do not use `\checkmark`. Similarly, `diagbox` is not required if you do not use the diagonal seperator in a particular column.

## Table Code
The last 11 columns include the previous references and the first column is the category. You can skip the `\multicolumn` parts if you do not have grouping for previous papers.


```latex
\begin{table*}[!ht]
 \caption{Previous Survey Comparison}
\label{tab:comparison}
\begin{tabularx}{\textwidth}{@{}l*{15}{C}c@{}}
\toprule
Group $\rightarrow$    & \multicolumn{4}{|@{}c@{\hskip0.25in}|}{Group 1} & \multicolumn{4}{@{}c@{\hskip0.25in}|}{Group 2}  & \multicolumn{3}{@{}c@{\hskip0.25in}}{Group 3} \\ 
\midrule
\diagbox[width=7em]{Category}{Papers}  & \rotatebox[origin=c]{90}{Abcde et al.}  & \rotatebox[origin=c]{90}{Abcde et al.}  & \rotatebox[origin=c]{90}{Abcde et al.}  & \rotatebox[origin=c]{90}{Abcde et al.}  & \rotatebox[origin=c]{90}{Abcde et al.}   & \rotatebox[origin=c]{90}{Abcde et al.}  & \rotatebox[origin=c]{90}{Abcde et al.}   & \rotatebox[origin=c]{90}{Abcde et al.}  & \rotatebox[origin=c]{90}{Abcde et al.}  & \rotatebox[origin=c]{90}{Abcde et al.}  & \rotatebox[origin=c]{90}{Abcde et al.}  \\ \midrule
cat-01 & \checkmark & \checkmark  & \checkmark & x & x   & x & x & \checkmark & x & x & \checkmark \\ 
cat-02 & \checkmark & x & \checkmark & x & \checkmark  & x & \checkmark  & x  & x & x   & \checkmark \\ 
cat-03 & \checkmark & x & x & \checkmark & x & x  & \checkmark & x & x & x & \checkmark\\ 
% \addlinespace
cat-04 & x & x  & \checkmark & \checkmark & x  & \checkmark & x & \checkmark & x & x & \checkmark \\ 
cat-05 & x & \checkmark  & x & \checkmark & x & x & \checkmark & x  & \checkmark  & x & x \\ 
cat-06 & x & x  & x  & \checkmark & x  & x  & x & \checkmark  & x    & x   & x  \\ 
cat-07 & x  & x  & \checkmark  & x  & x   & \checkmark & x & x  & \checkmark & x  & x \\ 
cat-08 & x & \checkmark & \checkmark & \checkmark & x   & \checkmark & x & \checkmark & x  & \checkmark & x \\ 
\bottomrule
\end{tabularx}
\end{table*}
```

## Output
The output is as follows:
<figure>
	<a href="https://live.staticflickr.com/65535/49301916326_898d3640d6_h.jpg"><img src="https://live.staticflickr.com/65535/49301916326_898d3640d6_h.jpg"></a>
</figure>

Once again, you will find the code and output in the [Overleaf Document](https://www.overleaf.com/read/bqjtshzgspsj).



## References
* [Grouping of Aligned Table Columns in Combination with Multicolumn](https://tex.stackexchange.com/questions/262760/grouping-of-aligned-table-columns-in-combination-with-multicolumn-and-a-long-hea)
* [How Can I Insert a Big Table in IEEE Template](https://tex.stackexchange.com/questions/305411/how-can-i-insert-a-big-table-in-ieee-template)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMyNjUwODIzMiwtMTM3ODI2NDg1NSwyMD
U0MTY3OTQ5LC0yMDcyNjY4MDkxXX0=
-->