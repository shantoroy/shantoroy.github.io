---
layout: single
title: "How to Create Bar Charts using Latex PGFPlots"
excerpt:  "In this tutorial, we'll learn how to create beautiful bar charts using the PGFPlots package in Latex. Bar charts are useful for representing discrete data with rectangular bars of various heights, with each bar representing a category or group. We'll start with a basic example and then gradually add customization options such as colors, legends, axis labels, and more."
seo_title:  "How to Create Bar Charts using Latex PGFPlots"
seo_description:  "Learn how to create stunning bar charts in Latex using the PGFPlots package. This tutorial covers the basics of bar chart creation, along with customization options such as colors, legends, axis labels, and more."
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


## Related Posts
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
* [How to add Codes in Latex:  `listings`  package for code documentation](https://shantoroy.com/latex/how-to-add-codes-in-latex-listing-package/)
* [Bibliography management with Bibtex in Latex](https://shantoroy.com/latex/bibliography-management-with-bibtex/)
* [Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot](https://shantoroy.com/latex/multiple-line-plots-using-tikz-pgfplot/)
* [How to Draw a Literature Survey Taxonomy Tree in Latex](https://shantoroy.com/latex/Draw-literature-survey-tree-in-latex/)
* [How to Convert Python Matplotlib Plots to Latex Plots (Easiest Way) for Academic Papers](https://shantoroy.com/latex/convert-matplotlib-plot-to-latex-plot/)


## Promotions and Referrals (US Residents Only)
* **Chime:** Open a Checking account at Chime using [my referral link](https://chime.com/r/shantoroy) and get $100 after your employer deposit paycheck of minimum $200 within the first 45 days. 
* **Rakuten:** Get $30 after you spend $30 at Rakuten select stores after you use [my referral link](www.rakuten.com/r/STONEH425?eeid=44971) to open an account. 
* **Chase Freedom Credit Card:** Earn $200 cash back with Chase Freedom Unlimited or Chase Freedom Flex credit card. I can be rewarded if you apply using [my referral link](https://www.referyourchasecard.com/18o/E7MB03IG12) and are approved for the card.

* **Chase Checking Account:** Get $200 when you open a checking account using [my referral link](https://accounts.chase.com/raf/share/2564396166) after your first salary is deposited. 
* **Discover:** Earn $50 cash back with Discover when you apply using [my referral link](https://refer.discover.com/s/SHANTO10) and are approved for the card.
* **Amex Blue Cash Preferred:** Earn $250 as statement credit when you spend $3000 in first six months. Apply using [my referral link](https://americanexpress.com/en-us/referral/SHANTRzUOO?XL=MIANS).


## References

* [Having y-axis in log scale base 2 using pgfplots](https://tex.stackexchange.com/questions/132703/having-y-axis-in-log-scale-base-2-using-pgfplots)
* [PGFPlots Gallery](http://pgfplots.sourceforge.net/gallery.html)
* [PgfPlots creating bar chart from csv](https://tex.stackexchange.com/questions/364076/pgfplots-creating-bar-chart-from-csv)
* [How to plot the first n rows of a table using pgfplots?](https://tex.stackexchange.com/questions/199376/how-to-plot-the-first-n-rows-of-a-table-using-pgfplots)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjQ4OTUwODM5LDE3NjU2NTE0MTBdfQ==
-->