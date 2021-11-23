---
layout: single
title: "Creating Bar Charts using Latex PGFPlots"
header:
  image: "https://live.staticflickr.com/65535/49149608331_427d999f03_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49149608331_427d999f03_h.jpg"
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

## Bar plots using Latex PGFPlot

Previously, I used to include plots as a figure generated using `python` `matplotlib`.
However, recently, while working on a paper, my supervisor wanted us to include plots in the paper using `latex` `pgfplot`. It is convenient to use these plots if we need to change conference/journal templates without worrying about image quality/configurations. In this post, I have added latex codes to create bar plots using `latex` `pgfplot`. Regardless to say, codes have been included for note purpose and collected from our paper and online resources.

Find outputs in this [Overleaf Document](https://www.overleaf.com/read/tpmkcgvsnhgg).

## A simple Bar Plot

Here, we plot a simple bar chart having data from a CSV file.

### Prerequisite Configuration

The CSV file had 100 entries. But, I included first 20 rows.
For that I needed to include an extra rule as follows:

```latex
\pgfplotsset{select coords between index/.style 2 args={
    x filter/.code={
        \ifnum\coordindex<#1\def\pgfmathresult{}\fi
        \ifnum\coordindex>#2\def\pgfmathresult{}\fi
    }
}}
```

### Bar Plot Code

```latex
\begin{figure}
    \centering
\pgfplotstableread[col sep=comma,]{100SalesRecords.csv}\datatable
\begin{tikzpicture}
\begin{axis}[
    ybar,
    bar width=.1cm,
    width=\textwidth,
    height=10cm,
    ymin = 0,
    xtick=data,
    xticklabels from table={\datatable}{Country},
    x tick label style={font=\normalsize, rotate=90, anchor=east},
    ylabel={Units Sold in Number}]
    \addplot [select coords between index={1}{20}] table [x expr=\coordindex, y={Units Sold}]{\datatable};
\end{axis}
\end{tikzpicture}
\caption{Units sold by Different countries}
\label{fig:my_label}
\end{figure}
```

## Group Plotting

### Prerequisites

The following configuration has been collected from our recent paper.

```latex
\pgfplotsset{
SmallBarPlot/.style={
    font=\footnotesize,
    ybar,
    width=\linewidth,
    ymin=0,
    xtick=data,
    xticklabel style={text width=1.5cm, rotate=90, align=center}
},
BlueBars/.style={
    fill=blue!20, bar width=0.25
},
RedBars/.style={
    fill=red!20, bar width=0.25
}
}

\DeclareRobustCommand\legendbox[1]{(\textcolor{#1}{#1}~\begin{tikzpicture}[x=0.2cm, y=0.2cm] \draw [color=black, fill=#1!20] (0,0) -- (0,1) -- (0.6,1) -- (0.6,0) -- (0, 0); \end{tikzpicture})}
```

### Simple Group Bar Plotting

```latex
\begin{figure}[ht!]
\pgfplotstableread[col sep = comma]{100SalesRecords.csv}\table
\centering
    \begin{tikzpicture}
    \begin{axis}[
            SmallBarPlot,
            xticklabels from table={\table}{Country},
            ylabel=Value in Number,
            xlabel=Countries
        ]
        \addplot [BlueBars] [select coords between index={1}{5}] table [x expr=\coordindex, y=Units Sold] {\table};
        \addlegendentry{First}
        \addplot [RedBars] [select coords between index={1}{5}] table [x expr=\coordindex, y=Unit Price] {\table};
        \addlegendentry{Second}
        \legend{}
    \end{axis}
    \end{tikzpicture}
\caption{The first legend \legendbox{blue} and the second one \legendbox{red}}
\label{fig:multiBar}
\end{figure}
```

## Subplots with Group Plotting

### Prerequisite

The previous configurations.

### Subplotting with group bars

The second subplot includes logarithmic scale.

```latex
\begin{figure}[ht!]
\pgfplotstableread[col sep = comma]{100SalesRecords.csv}\table
\centering
\begin{subfigure}[b]{.5\linewidth}
    \centering
    \begin{tikzpicture}
    \begin{axis}[
            SmallBarPlot,
            xticklabels from table={\table}{Country},
            ylabel=Value in Number,
            xlabel=Countries
        ]
        \addplot [BlueBars] [select coords between index={1}{5}] table [x expr=\coordindex, y=Units Sold] {\table};
        \addlegendentry{First}
        \addplot [RedBars] [select coords between index={1}{5}] table [x expr=\coordindex, y=Unit Price] {\table};
        \addlegendentry{Second}
        \legend{}
    \end{axis}
    \end{tikzpicture}
\end{subfigure}%
\begin{subfigure}[b]{.5\linewidth}
     \centering
    \begin{tikzpicture}
    \begin{axis}[
            SmallBarPlot,
            xticklabels from table={\table}{Country},
            ylabel= ylabel=Value in Number,
            xlabel=Countries,
            ymode=log,
            log basis y={10}
        ]
        \addplot [BlueBars] [select coords between index={1}{5}] table [x expr=\coordindex, y=Total Revenue] {\table};
        \addlegendentry{First}
        \addplot [RedBars] [select coords between index={1}{5}] table [x expr=\coordindex, y=Total Cost] {\table};
        \addlegendentry{Second}
        \legend{}
    \end{axis}
    \end{tikzpicture}
\end{subfigure}
\caption{The first legend \legendbox{blue} and the second one \legendbox{red}.}
\label{fig:subBarPlot}
\end{figure}
```

Happy Documentation and writing papers.


## References

* [Having y-axis in log scale base 2 using pgfplots](https://tex.stackexchange.com/questions/132703/having-y-axis-in-log-scale-base-2-using-pgfplots)
* [PGFPlots Gallery](http://pgfplots.sourceforge.net/gallery.html)
* [PgfPlots creating bar chart from csv](https://tex.stackexchange.com/questions/364076/pgfplots-creating-bar-chart-from-csv)
* [How to plot the first n rows of a table using pgfplots?](https://tex.stackexchange.com/questions/199376/how-to-plot-the-first-n-rows-of-a-table-using-pgfplots)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI3NzYyODc2OV19
-->