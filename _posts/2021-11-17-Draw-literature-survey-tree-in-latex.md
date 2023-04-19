---
layout: single
title: "How to Draw a Literature Survey Taxonomy Tree in Latex"
excerpt:  "In academic writing, a literature survey is an essential component for presenting a comprehensive review of a topic. A taxonomy tree can be used to visually represent the relationships between different papers, authors, and themes in the field. In this blog post, I will show how to draw a literature survey taxonomy tree in LaTeX, which is a powerful tool for typesetting high-quality scientific documents."
seo_title:  "How to Draw a Literature Survey Taxonomy Tree in LaTeX - A Step-by-Step Guide"
seo_description:  "Learn how to draw a literature survey taxonomy tree in LaTeX, a powerful tool for typesetting scientific documents. This step-by-step guide will show you how to visually represent the relationships between entities in your field using a taxonomy tree."
header:
  image: "https://live.staticflickr.com/65535/52103583338_6325627e1f_o.png"
  teaser: "https://live.staticflickr.com/65535/52103583338_6325627e1f_o.png"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Overleaf
  - Taxonomy
  - Tree
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
---



I was trying to draw a taxonomy like tree where the child nodes are aligned  to the right rather than bottom. It is for drawing a literature survey alike tree, which looks like following:

<a data-flickr-embed="true" href="https://www.flickr.com/photos/142248809@N07/52103780019/in/dateposted-public/" title="literature-survey-tree-taxonomy-in-latex"><img src="https://live.staticflickr.com/65535/52103780019_55cca5a6c5_o.png" width="700" height="352" alt="literature-survey-tree-taxonomy-in-latex"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

To draw a taxonomy tree like this, first, we need the following packages:
```latex
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{forest}
\usetikzlibrary{trees,positioning,shapes,shadows,arrows.meta}
```


Now, here's the code that produces this output. You can also check out the output in [this overleaf project](https://www.overleaf.com/read/wmbhxwjqsvkc). 

```latex
\begin{figure}
    \centering
    
% I am using only the basic, xnode, and tnode styles
\tikzset{
    basic/.style  = {draw, text width=3cm, align=center, font=\sffamily, rectangle},
    root/.style   = {basic, rounded corners=2pt, thin, align=center, fill=green!30},
    onode/.style = {basic, thin, rounded corners=2pt, align=center, fill=green!60,text width=3cm,},
    tnode/.style = {basic, thin, align=left, fill=pink!60, text width=15em, align=center},
    xnode/.style = {basic, thin, rounded corners=2pt, align=center, fill=blue!20,text width=5cm,},
    wnode/.style = {basic, thin, align=left, fill=pink!10!blue!80!red!10, text width=6.5em},
    edge from parent/.style={draw=black, edge from parent fork right}

}
%

\begin{forest} for tree={
    grow=east,
    growth parent anchor=west,
    parent anchor=east,
    child anchor=west,
    edge path={\noexpand\path[\forestoption{edge},->, >={latex}] 
         (!u.parent anchor) -- +(10pt,0pt) |-  (.child anchor) 
         \forestoption{edge label};}
}
% l sep is used for arrow distance
[Reconnaissance Survey, basic,  l sep=10mm,
    [Network Scanning, xnode,  l sep=10mm,
        [Shaikh et al.\, 2008, tnode]
        [Bhuyan et al.\, 2011, tnode]
        [Bou et al.\, 2013, tnode] ]
    [Social Engineering, xnode,  l sep=10mm,
        [Chiew et al.\, 2018, tnode]
        [Heartfield \& Loukas\, 2015, tnode]
        [Salahdine et al.\, 2019, tnode] 
        [Alharthi et al.\, 2020, tnode] ]
    [Open-Source Footprinting, xnode,  l sep=10mm,
        [Rai et al.\, 2021, tnode]
        [Kanta et al.\, 2020, tnode]
        [Glassman et al.\, 2012, tnode] 
         ] ]
\end{forest}

    \caption{Literature Survey Tree}
    \label{fig:lit_surv}
\end{figure}
```

There are a few node styles defined earlier in the code. However, I am using only the `basic`, `xnode,` and `tnode` styles. you can change the designs of the node by changing the parameters like `align`, `fill`, etc.

Then under the `\begin{forest}...\end{forest}` environment, all you need to do is create a python list-alike array of contents, where you put child nodes as a nested list.

You can also check out my other post:
[Draw a Taxonomy Tree in Latex using Tikz for Publication](https://shantoroy.com/latex/taxonomy-tree-in-latex-for-publication/).


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
* [How to Draw Equations with Parameter Description in Latex using Tikz](https://shantoroy.com/latex/Draw-equations-with-parameter-description-in-latex/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NjQ4MDM3NjYsMTA3NTIyNDI0Ml19
-->