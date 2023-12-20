---
layout: single
title: "How to add a Signature line and Space in Latex"
excerpt:  "Adding a signature line and space in LaTeX is an essential part of writing formal documents such as letters, resumes, and contracts. In this tutorial, we will show you how to create a signature line with a space in LaTeX by using the `tabular` environment and some simple commands. We will also discuss some of the formatting options you can use to customize your signature line to fit your needs."
seo_title:  "How to Add a Signature Line and Space in LaTeX: A Step-by-Step Guide"
seo_description:  "Learn how to create a signature line with space in LaTeX for your formal documents like letters and resumes. Follow our step-by-step guide using the `tabular` environment and formatting options to customize your signature line."
header:
  image: "https://live.staticflickr.com/65535/51887360931_5dfb39dbd7_o.png"
  teaser: "https://live.staticflickr.com/65535/51887360931_5dfb39dbd7_o.png"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Table
  - How-to
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


If you need to add a signature space and line, just create a table of one column. You can do it without creating a table too, however, it helps if you need additional customization in the left or right side.

In the following code, `\vspace{25mm}` is used to have a space for the signature. You can customize the number according to your need.

Later, `\hrulefill` is used to fill up the size of the column with a horizontal line. Here, I used $2.5$ inches. Customize it based on your need.

```latex
\vspace{25mm}
\begin{tabular}{@{}p{2.5in}@{}}
\hrulefill \\
Shanto Roy \\
University of Houston
\end{tabular}
```

If you want to add a date in thr right side, just add two extra columns in the table: the first one to have extra space in the middle, and the last column includes the date.
```latex
\vspace{25mm}
\begin{tabular}{@{}p{2.5in}p{2in}p{2in}@{}}
\hrulefill && Date: 17 February, 2022\\
Shanto Roy &&\\
University of Houston
\end{tabular}
```

That's all, cheers!


## Latex-related Posts
You can find a comprehensive list of Latex resources in the following post:

[Latex Resources in a Nutshell](https://shantoroy.com/latex/latex-resources-in-a-nutshell/)

If you are a new Latex user, check out this post:
[20 Most Common Mistakes Made by New Latex Users](https://shantoroy.com/latex/common-mistakes-made-by-new-latex-typesetting-users/)

You can find all `Latex` oriented posts of mine in: [https://shantoroy.com/categories/#latex](https://shantoroy.com/categories/#latex)


* [How to write an algorithm in Latex](https://shantoroy.com/latex/how-to-write-algorithm-in-latex/)
* [How to add subfigure in Latex](https://shantoroy.com/latex/how-to-add-subfig-in-latex/)
* [Add Copyright Notice and Conference Name in IEEE Conference Template](https://shantoroy.com/latex/add-copyright-conference-name/)
* [Preparing Tables for Publication and Documentation in Latex](https://shantoroy.com/latex/how-to-create-tables-in-latex/)
* [Creating Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)

* [How to Write Matrix with Row/Column Labels in Latex](https://shantoroy.com/latex/matrix-labeling-in-latex/)
* [How to Collaboratively Write a Paper using Overleaf Latex Platform](https://shantoroy.com/latex/how-to-collaborately-write-a-paper-using-latex-overleaf/)
* [Itemize, Enumerate, and To-do-list in Latex](https://shantoroy.com/latex/playing-with-latex-itemize-enumerate-fontawesome/)
* [Latex Table for Survey in IEEE two-column format](https://shantoroy.com/latex/latex-table-for-survey-ieee-template/)
* [Line Plotting using Latex PGFPlots](https://shantoroy.com/latex/how-to-draw-line-graph-using-pgfplots-latex/)
* [How to Create Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)
* [How to add Codes in Latex:  `listings`  package for code documentation](https://shantoroy.com/latex/how-to-add-codes-in-latex-listing-package/)
* [Bibliography management with Bibtex in Latex](https://shantoroy.com/latex/bibliography-management-with-bibtex/)
* [Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot](https://shantoroy.com/latex/multiple-line-plots-using-tikz-pgfplot/)
* [How to Draw a Literature Survey Taxonomy Tree in Latex](https://shantoroy.com/latex/Draw-literature-survey-tree-in-latex/)
* [How to Convert Python Matplotlib Plots to Latex Plots (Easiest Way) for Academic Papers](https://shantoroy.com/latex/convert-matplotlib-plot-to-latex-plot/)

If you find this post helpful, and want to support this blog, you can
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="shantoroy" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script> or

<div style="width: 300px; height: 200px;">
<form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="business" value="Q9F45GULUSYMY" />
<input type="hidden" name="no_recurring" value="0" />
<input type="hidden" name="item_name" value="I appreciate your support! 😊" />
<input type="hidden" name="currency_code" value="USD" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
</form></div>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg0NjcxMjA5MywxMjExOTc5MTExLDM1Nz
I3ODgwN119
-->