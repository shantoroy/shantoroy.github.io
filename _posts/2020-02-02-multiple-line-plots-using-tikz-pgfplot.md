---
layout: single
title: "Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot"
header:
  image: "https://live.staticflickr.com/65535/51232995681_568b5ea17b_w.jpg"
  teaser: "https://live.staticflickr.com/65535/51232995681_568b5ea17b_w.jpg"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Charts
  - Graphs
  - Tikz
  - PGFPlot
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


In this tutorial, we will see how to create multiple line-plot using Latex `Tikz` and `PGFPlot`.

Let's first create a document and import the necessary packages
```latex
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{pgfplotstable}
\pgfplotsset{compat=1.7}
\usepackage{subcaption}
```

Now, let's create a dataset, or you can upload a CSV/DAT file.

```latex
\begin{filecontents}{testdata.csv}
x-axis,a,b,c,d,e,f,g,h
x1,0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125
x2,0.4776,0.0048,0.4729,0.5,0.0199,0.0002,0.1,0.2
x3,0.5041,0.0001,0.4941,0.4,0.0009,0.0001,0.1,0.2
x4,0.5075,0.0001,0.4924,0.45,0.0009,0,0.0001,0.1
x5,0.51,0.0001,0.4899,0.5,0.0009,0,0.0001,0.01
x6,0.5126,0.0001,0.4874,0.5,0.0009,0,0.0001,0.01
\end{filecontents}
```

Now, let's create a `\begin{tikzpicture}...\end{tikzpicture}` environment and put that within the `\begin{figure}...\end{figure}` environment. All of our code will be within the `tikzpicture` environment.

```latex
\begin{figure}[!ht]
    \centering
\pgfplotstableread[col sep=comma,]{testdata.csv}\datatable
\begin{tikzpicture}
\begin{axis}[
    width=\textwidth,
    height=10cm,
    xtick=data,
    xticklabels from table={\datatable}{x-axis},
    x tick label style={font=\normalsize, rotate=35, anchor=east},
    legend style={at={(0.98,0.3)},anchor=south east},
    ylabel={Probability}]
    
    \addplot [mark=o, blue!80 ] table [x expr=\coordindex, y={a}]{\datatable};
    \addlegendentry{$mod-a$}
    
    \addplot [mark=o, red!80] table [x expr=\coordindex, y={b}]{\datatable};
    \addlegendentry{$mod-b$}
    
    \addplot [mark=o, black!50 ] table [x expr=\coordindex, y={c}]{\datatable};
    \addlegendentry{$mod-c$}
    
    \addplot [mark=o, violet!80] table [x expr=\coordindex, y={d}]{\datatable};
    \addlegendentry{$mod-d$}
    
    \addplot [mark=o, cyan!80] table [x expr=\coordindex, y={e}]{\datatable};
    \addlegendentry{$mod-e$}
    
    \addplot [mark=o, orange!30] table [x expr=\coordindex, y={f}]{\datatable};
    \addlegendentry{$mod-f$}
    
    \addplot [mark=o, brown!90] table [x expr=\coordindex, y={g}]{\datatable};
    \addlegendentry{$mod-g$}
    
    \addplot [mark=o, green!80!red!80] table [x expr=\coordindex, y={h}]{\datatable};
    \addlegendentry{$mod-h$}
\end{axis}
\end{tikzpicture}
\caption{Multiple Line-plots using Tikz}
\label{fig:my_label}
\end{figure}
```

Here, `\pgfplotstableread` is used to read the file contents and declare as a new table name.

Within the `\axis` environment, first we define the width, height, xtick information, and legend place. Then we use `\addplot` for each column to convert to individual line plots. `\addlegendentry` is used to add an entry for that line in the legendbox.

The output can be viewed in the [Overleaf Document](https://www.overleaf.com/read/dpkydqvjcpds)

That's it for today! Cheers!!!

If this post helps you to solve your problem, and you want to thank/support me for that, you can  [Buy me Coffee](https://www.paypal.me/shantoroy). :smiley:
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NDMzNzUxODEsMTQ1OTAxMzMzMl19
-->