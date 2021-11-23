---
layout: single
title: "Line Plotting using Latex PGFPlots"
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU4NDA5ODkzNCwxNTM3MjU5MDY3LC0xNT
Y4MjcyOTIxXX0=
-->