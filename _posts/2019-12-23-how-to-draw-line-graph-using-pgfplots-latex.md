---
layout: single
title: "Line Plotting using Latex PGFPlots"
redirect_from:
  - /latex/line-graph-pgfplots/
  - /latex/how-to-draw-line-graph-using-pgfplots-latex/
excerpt:  "If you are a researcher or a student looking for a way to create high-quality line plots for your scientific documents, then you might want to consider using LaTeX with PGFPlots. In this blog post, I will cover the basics of line plotting using PGFPlots, including how to create simple line plots, add labels, change the axis scale, and customize the style of your plots. This post will also show you how to create more complex plots like multiple lines, error bars, and shaded regions. With the help of this guide, you will be able to create professional-looking line plots that will impress your readers."
seo_title:  "A Beginner's Guide to Line Plotting using LaTeX PGFPlots" 
seo_description:  "Learn how to create high-quality line plots using LaTeX with PGFPlots. This guide covers everything from creating simple line plots to more complex plots with multiple lines, error bars, and shaded regions."
header:
  image: "https://live.staticflickr.com/65535/49274059347_9de083b1a5_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49274059347_9de083b1a5_h.jpg"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Charts
  - Graphs
  - Documentation
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

In this post I have added example codes and a short explanation on how to draw line plots using latex. All codes and outputs are available in the [Overleaf Document](https://www.overleaf.com/read/rbkstfzrydpk).

## Required packages for plotting 
```latex
\usepackage{pgfplots}
\usepackage{pgfplotstable}
\pgfplotsset{compat=1.7}
\usepackage{tikz}
```
## A simple line plot
Code for a simple line plot in latex is as follows:
```latex
\begin{tikzpicture}
\begin{axis}[
	xlabel=put ur xlabel,
	ylabel=put ur ylabel,
	width=10cm,height=7cm,
    legend style={at={(0.0,.91)},anchor=west}
    ]

% Add values and attributes for the first plot
\addplot[color=red,mark=x] coordinates {
	(1, 7)
	(2, 8)
	(3, 9)
	(4, 10)
	(5, 11)
	(6, 12)
};

% Add values and attributes for the second plot
\addplot[color=blue,mark=*] coordinates {
	(1, 9)
	(2, 10)
	(3, 11)
	(4, 12)
	(5, 13)
	(6, 14)
};

\legend{Case 1,Case 2}
\end{axis}
\end{tikzpicture}
```

You can define different axis attributes including the `x-label`, `y-label`, `legend style` or `legend position`, `width`, `height`, etc. within the `[]` block after `\begin{axis}`. Then use `\addplot` to generate a line plot. Include as many `\addplot` as the number of legends you want. Put line attributes within the `[]` and `(x,y)` value pairs within `coordinates{};`. Then add legends sequentially seperated by a comma within `\legend{}`.

If you want the plot as a figure, you need to put the whole code within `\begin{figure}...\end{figure}` environment:
```latex
\begin{figure}[!ht]
    \centering
    \begin{tikzpicture}
        \begin{axis}[domain=0:10,legend pos=outer north east]
        \addplot {sin(deg(x))}; 
        \addplot {cos(deg(x))}; 
        \legend{$\sin(x)$,$\cos(x)$,}
        \end{axis}
    \end{tikzpicture}
    \caption{Put your Caption}
    \label{fig:my_label}
\end{figure}
```

## Plotting on Graph paper background 
Use the following code to generate a graph-paper alike background for line plots:
```latex
\begin{tikzpicture}
  \begin{axis}
    [grid=both,
     % number of ticks in between grids, 9 ticks = 10 cells
     minor tick num=9,
     % define regular grid style with line width and color
     grid style={line width=.2pt, draw=black!10},
     % define major grid style with line width and color
     major grid style={line width=.4pt,draw=black!50},
     axis lines=middle,
     enlargelimits={abs=0.1},
     % define width and height
     width=12cm, height=9cm
    ]
    \addplot[domain=-5:5,samples=50,smooth,red] {sin(deg(pi*x))};
  \end{axis}
\end{tikzpicture}
```

## Subplotting
Put multiple plots within the `\begin{subfigure}...\end{subfigure}` and  environment to put multiple plots as subfigures. You can also use `\resizebox{\columnwidth}{!}{}` environment for maintaining column width. Btw, do not forget to add the following packages beforehand:
```latex
\usepackage{graphicx}
\usepackage{caption}
\usepackage{subcaption}
```
The following example has two subplots-
```latex
\begin{figure*}[!ht]
    \centering
    \resizebox{\columnwidth}{!}{
    \begin{subfigure}[pt]{0.45\linewidth}
    \begin{tikzpicture}
\begin{axis}[
	xlabel=put ur xlabel,
	ylabel=put ur ylabel (\%),
	width=7cm,height=6cm,
    legend style={at={(0.0,.91)},anchor=west},
    yticklabel=\pgfmathprintnumber{\tick}\,\%
    ]
\addplot[color=red,mark=x] coordinates {
	(1, 7)
	(2, 8)
	(3, 9)
	(4, 10)
	(5, 11)
	(6, 12)
};

\addplot[color=blue,mark=*] coordinates {
	(1, 9)
	(2, 10)
	(3, 11)
	(4, 12)
	(5, 13)
	(6, 14)
};

\legend{Case1,Case2}
\end{axis}
\end{tikzpicture}
\caption{Put your subcaption!!!}
\label{fig:sub1}
    \end{subfigure}\hspace{8mm}
    
    
    \begin{subfigure}[pt]{0.45\linewidth}
    \begin{tikzpicture}
\begin{axis}[
	xlabel=put ur xlabel,
	ylabel=put ur ylabel (\%),
	width=7cm,height=6cm,
    legend style={at={(0.0,.91)},anchor=west},
    yticklabel=\pgfmathprintnumber{\tick}\,\%
    ]
\addplot[color=red,mark=x] coordinates {
	(1, 7)
	(2, 8)
	(3, 9)
	(4, 10)
	(5, 11)
	(6, 12)
};

\addplot[color=blue,mark=*] coordinates {
	(1, 9)
	(2, 10)
	(3, 11)
	(4, 12)
	(5, 13)
	(6, 14)
};

\legend{Case1,Case2}
\end{axis}
\end{tikzpicture}
\caption{Put your subcaption!!!}
\label{fig:sub1}
    \end{subfigure}
    }
    
\caption{Put your Caption Here}
\end{figure*}
```



## References
* [Plotting sinx and cosx on pgf tikz](https://tex.stackexchange.com/questions/231052/plotting-fx-sin-x-and-fx-cos-x-on-pgf-tikz)
* [tikz or pgfplots- plotting a trigonometric function](https://tex.stackexchange.com/questions/361915/tikz-or-pgfplots-plotting-a-trigonometric-function-cos-sin-tan)
* [How to plot sinx and cosx with tikz](https://tex.stackexchange.com/questions/16232/how-to-plot-fx-sinx-kx-cosx-and-ux-x%C2%B2-with-tikz)


## Related posts on Latex
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
* [How to add Codes in Latex:  `listings`  package for code documentation](https://shantoroy.com/latex/how-to-add-codes-in-latex-listing-package/)
* [Bibliography management with Bibtex in Latex](https://shantoroy.com/latex/bibliography-management-with-bibtex/)
* [Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot](https://shantoroy.com/latex/multiple-line-plots-using-tikz-pgfplot/)
* [How to Draw a Literature Survey Taxonomy Tree in Latex](https://shantoroy.com/latex/Draw-literature-survey-tree-in-latex/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzI3MjY2NzQxLC05NzUyNTU3NjEsLTk3OT
EyOTE2Ml19
-->