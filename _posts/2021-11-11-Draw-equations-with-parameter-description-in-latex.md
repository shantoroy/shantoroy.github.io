---
layout: single
title: "How to Draw Equations with Parameter Description in Latex using Tikz"
excerpt:  "If you're looking to create professional-looking equations with clear parameter descriptions, then using Tikz in Latex can be a great solution. In this tutorial, I'll walk you through the process of drawing equations with parameter descriptions using Tikz in Latex, so you can easily and clearly display mathematical equations in your documents."
seo_title:  "How to Draw Equations with Parameter Description in Latex using Tikz"
seo_description:  "Learn how to create clear and professional-looking equations with parameter descriptions in Latex using Tikz. This tutorial will walk you through the process step-by-step, so you can easily display mathematical equations in your documents."
header:
  image: "https://live.staticflickr.com/65535/52102560767_07df211900_o.png"
  teaser: "https://live.staticflickr.com/65535/52102560767_07df211900_o.png"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Overleaf
  - Tikz
  - Equation
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
---

I was looking for a code that has a visualization of equation parameter description like the following.

<figure>
  <a href="/assets/images/post_images/2021-11-17-draw-equation-with-parameter-description.png"><img src="/assets/images/post_images/2021-11-17-draw-equation-with-parameter-description.png"></a>
</figure>
<br/>

Then I found this [awesome collection of Tikz Examples](https://github.com/walmes/Tikz) and I just modified a little from their code.


First, we need the following packages:
```latex
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{xcolor}
```


Now, here's the code that produces this output. You can also check out the output in [this overleaf project](https://www.overleaf.com/read/kyqrmhfcnrwx). 

```latex
\def\hd{0.5}
\def\vd{0.5}
\newcommand{\tm}[1]{\tikz[overlay, anchor=base] \node[red] (#1) {};}
\tikzstyle{every picture}+=[remember picture]

\begin{tikzpicture}[
  >=stealth,
  every path/.style={->, color=green!70!white, thin, rounded corners},
  every node/.style={color=black},
  bx/.style={text width=3cm, font=\footnotesize, minimum height=4ex},
  bxl/.append style={bx, left, align=flush right},
  bxr/.append style={bx, right, align=flush left}]

  \node {
    $\tm{y}y =
    \tm{b0}\beta_0+
    \tm{b1}\beta_1
    \tm{x1}x_1+
    \tm{b2}\beta_2
    \tm{x2}x_2+\cdots+
    \tm{bk}\beta_k
    \tm{xk}x_k+
    \tm{er}\epsilon$
  };

  \node[bx, align=center] (preds) at (0.4,1.5)
  {Independent Variables};
  \node[bx, align=center] (tx) at (0.4,-1.5) {Coefficients};

  \path[draw] (y)+(0.5ex,2ex) to[out=90, in=0] +(-\vd,\hd)
  node[bxl] {Dependent variable};
  \path[draw] (x1)+(0.5ex,2ex) to[out=90, in=-90] (preds);
  \path[draw] (x2)+(0.5ex,2ex) to[out=90, in=-90] (preds);
  \path[draw] (xk)+(0.5ex,2ex) to[out=90, in=-90] (preds);
  \path[draw] (b1)+(1ex,-1ex) to[out=-90, in=90] (tx);
  \path[draw] (b2)+(1ex,-1ex) to[out=-90, in=90] (tx);
  \path[draw] (bk)+(1ex,-1ex) to[out=-90, in=90] (tx);
  \path[draw] (b0)+(1ex,-1ex) to[out=-90, in=0] +(-\vd,-\hd)
  node[bxl] {Intercept};
  \path[draw] (er)+(0.5ex,-1ex) to[out=-90, in=180] +(\vd,-\hd)
  node[bxr] {Random Error};

\end{tikzpicture}
```



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

<!--stackedit_data:
eyJoaXN0b3J5IjpbMzYwODE4NjMyLC0yMTI2ODYzMzQzLDIzNT
Y4MDUxMSwyMzI4OTMyOV19
-->