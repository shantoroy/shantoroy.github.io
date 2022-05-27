---
layout: single
title: "How to Draw a Literature Survey Taxonomy Tree in Latex"
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA3NTIyNDI0Ml19
-->