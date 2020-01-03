---
layout: single
title: "Draw a Taxonomy Tree in Latex using Tikz for Publication"
header:
  image: "https://live.staticflickr.com/65535/49322225972_9fd2532e24_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49322225972_9fd2532e24_h.jpg"
categories:
  - Latex
tags:
  - Latex
  - Resources
  - Documentation
  - Taxonomy
  - Tutorial
  - Publication
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

While writing a paper, we often require to draw `classification tree` diagrams. In this post, I show you how to draw one in Latex. Previously, I used to draw one using `draw.io`. However, Latex is more convenient in terms of font size management.

You can also find the code and output in the [Overleaf Document](https://www.overleaf.com/read/wmbhxwjqsvkc).

## Include Packages
At first, include the `tikz` package:
```latex
\usepackage{tikz}
```
Then include the following libraries:
```latex
\usetikzlibrary{trees,positioning,shapes,shadows,arrows}
```

## Set Basic Styles
Set basic node styles for different levels. Adjust the `text width` based on your diagram. Use `thick` instead of thin if wanted a thicker line for the nodes. I usually avoid colors; if you want to fill the nodes with colors, change the color from `white` to your desired one.
```latex
\tikzset{
  basic/.style  = {draw, text width=2cm, drop shadow, font=\sffamily, rectangle},
  root/.style   = {basic, rounded corners=2pt, thin, align=center, fill=white},
  level-2/.style = {basic, rounded corners=6pt, thin,align=center, fill=white, text width=3cm},
  level-3/.style = {basic, thin, align=center, fill=white, text width=1.8cm}
}
```

## Final Code
Within the _level 1_ style definition, you can skip  `edge from parent path={(\tikzparentnode.south) -- (\tikzchildnode.north)}` because it works the similar way by default. You can also omit `edge from parent fork down` if you want a straight arrow from _root_ to _level 1_ children. Configure `node distance` according to your need.

```latex
\begin{figure}
    \centering
\begin{tikzpicture}[
  level 1/.style={sibling distance=12em, level distance=5em},
%   {edge from parent fork down},
  edge from parent/.style={->,solid,black,thick,draw}, 
  edge from parent path={(\tikzparentnode.south) -- (\tikzchildnode.north)},
  >=latex, node distance=1.2cm, edge from parent fork down]

% define root %
\node[root] {\textbf{Taxonomy}}

% Level-1 children %
  child {node[level-2] (c1) {\textbf{Category 1}}}
  child {node[level-2] (c2) {\textbf{Category 2}}}
  child {node[level-2] (c3) {\textbf{Category 3}}}
  child {node[level-2] (c4) {\textbf{Category 4}}};

% For Category 1 children %
\begin{scope}[every node/.style={level-3}]
\node [below of = c1, xshift=10pt] (c11) {item 1-1};
\node [below of = c11] (c12) {item 1-2};
\node [below of = c12] (c13) {item 1-3};

% For Category 2 children %
\node [below of = c2, xshift=10pt] (c21) {item 2-1};
\node [below of = c21] (c22) {item 2-2};
\node [below of = c22] (c23) {item 2-3};
\node [below of = c23] (c24) {item 2-4};

% For Category 3 children %
\node [below of = c3, xshift=10pt] (c31) {item 3-1};
\node [below of = c31] (c32) {item 3-2};
\node [below of = c32] (c33) {item 3-3};
\node [below of = c33] (c34) {item 3-4};
\node [below of = c34] (c35) {item 3-5};

% For Category 4 children %
\node [below of = c4, xshift=10pt] (c41) {item 4-1};
\node [below of = c41] (c42) {item 4-2};
\end{scope}


% Draw arrows from level-1 to it's children %
\foreach \value in {1,2,3}
  \draw[->] (c1.195) |- (c1\value.west);

\foreach \value in {1,...,4}
  \draw[->] (c2.195) |- (c2\value.west);
  
\foreach \value in {1,...,5}
  \draw[->] (c3.195) |- (c3\value.west);
  
\foreach \value in {1,2}
  \draw[->] (c4.195) |- (c4\value.west);
\end{tikzpicture}
    \caption{This is a simple Taxonomy}
    \label{fig:my_label}
\end{figure}
```

## Output
The output looks like the following. 
Once again, you can also find the code and output in the [Overleaf Document](https://www.overleaf.com/read/wmbhxwjqsvkc).
<figure>
	<a href="https://live.staticflickr.com/65535/49322010141_7b08974351_h.jpg"><img src="https://live.staticflickr.com/65535/49322010141_7b08974351_h.jpg"></a>
</figure>

That's all folks. Cheers!!! :smiley:

## References
1. [edge from parent (dashed) makes nodes themselves dashed?](https://tex.stackexchange.com/questions/350252/edge-from-parentdashed-makes-nodes-themselves-dashed)
2. [Trees Examples](http://www.texample.net/tikz/examples/feature/trees/)
3. [TikZ and pgf](https://www.bu.edu/math/files/2013/08/tikzpgfmanual.pdf)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY3MzIxNTI4MiwtMjYwMjgzNjMwLC01Mj
YyNDM2MSwyNDY5NDMxMDYsOTk2NTY3OTQ1XX0=
-->