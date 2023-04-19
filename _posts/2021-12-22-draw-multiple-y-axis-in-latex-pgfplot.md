---
layout: single
title: "How to Draw Multiple Y-Axis in Latex PGFPlots"
excerpt:  "Want to plot multiple y-axes on a single LaTeX PGFPlots plot? Check out this tutorial on how to draw multiple y-axes in LaTeX PGFPlots. Whether you are a scientist or a student, this easy-to-follow guide will show you how to create impressive, multi-dimensional plots that are perfect for research papers, presentations, and more."
seo_title:  "Drawing Multiple Y-Axes in Latex PGFPlots: A Step-by-Step Guide"
seo_description:  "Learn how to draw multiple y-axes in LaTeX PGFPlots with this comprehensive tutorial. Follow my easy-to-understand instructions and create stunning, multi-dimensional plots for your research papers and presentations. Perfect for scientists, students, and anyone looking to enhance their LaTeX skills."
header:
  image: "https://live.staticflickr.com/65535/52102245910_94d1a1a625_o.png"
  teaser: "https://live.staticflickr.com/65535/52102245910_94d1a1a625_o.png"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - PGFPlot
  - Tikz
  - Overleaf
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



Sometimes, we need to plot two or three line charts in the same plot due to lack of space. Also, if we need to plot three different y-axis against the same x-axis, it is better we put all three in a single plot diagram.

Now, thw question is why we might need different scales! Why don't we use the same y-axis for all!

The answer is, you may not find the plots meaningful if there is large gaps between the ranges of y-axis values. If ranges are very small and very distant, you may find several straight lines in your plot. That's why we need to use different y-axis for plotting different lines.

In this post, I adapt the codes from two stack overflow threads (links in the reference section) and provide the code for 2- and 3-y axis plots. 
You can find the outputs in [this Overleaf Project](https://www.overleaf.com/read/tpmkcgvsnhgg). 

<a data-flickr-embed="true" href="https://www.flickr.com/photos/142248809@N07/52100272667/in/dateposted-public/" title="multiple y-axis in latex pgfplot"><img src="https://live.staticflickr.com/65535/52100272667_b3fcfb5139_o.png" width="437" height="639" alt="multiple y-axis in latex pgfplot"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

## Required Packages
```latex
\usepackage{pgfplots}
\usepackage{pgfplotstable}
\pgfplotsset{compat=1.7}
\usepackage{subcaption}
```

## Multiple Axis in PGFPlot
### Two y-axis
```latex
\begin{figure}
    \centering
    \begin{tikzpicture}
    \pgfplotsset{
        scale only axis,
        scaled x ticks=base 10:3,
        xmin=0, xmax=0.06,
        y axis style/.style={
            yticklabel style=#1,
            ylabel style=#1,
            y axis line style=#1,
            ytick style=#1
       }
    }
    
    \begin{axis}[
      axis y line*=left,
      y axis style=blue!75!black,
      ymin=0, ymax=80,
      xlabel=$x\_label$,
      ylabel=$y\_label\_1$
    ]
    \addplot[smooth,mark=x,blue] 
      coordinates{
        (0,68.6)
        (0.0148,72) 
        (0.0295,68.6)
        (0.0441,53.4)
        (0.059,22.8) 
    };
    \end{axis}
    
    \begin{axis}[
      axis y line*=right,
      axis x line=none,
      ymin=0, ymax=100,
      ylabel=$y\_label\_2$,
      y axis style=red!75!black
    ]
    \addplot[smooth,mark=*,red] 
      coordinates{
        (0,0)
        (0.0148,48) 
        (0.0295,66)
        (0.0441,66)
        (0.059,45.0) 
    };
    \end{axis}
    
    \end{tikzpicture}
    \caption{PGFplot Code for two y-Axis}
    \label{fig:pgfplot-two}
\end{figure}
```


### Three y-axis
```latex
\begin{figure}
    \centering

\begin{tikzpicture}
 \pgfplotsset{every axis/.style={ymin=0},
                 y axis style/.style={
                            yticklabel style=#1,
                            ylabel style=#1,
                            y axis line style=#1,
                            ytick style=#1}}
\begin{axis}[ scale only axis, xmin=0,xmax=12, axis y line*=left, xlabel=fractions, ylabel=Small Axis (green), y axis style=green!75!black]
    \addplot[smooth, green!75!black, mark=o, draw] coordinates {(0,0)
    (1,0.3)(2,0.4)
    (3,0.6)(4,0.7)
    (5,1)(6,1.4)
    (7,1.3)(8,1.1)
    (9,0.7)(10,0.6)
    (11,0.5)(12,0.4)};
\end{axis}
%
\begin{axis}[ scale only axis, xmin=0,xmax=12, axis y line*=right, axis x line=none, ylabel=Second ordinate (blue), y axis style=blue]%
    \addplot[smooth, blue, mark=x] coordinates {(0,0)
    (1,2)(2,6)
    (3,10)(4,20)
    (5,18)(6,15)
    (7,12)(8,10)
    (9,8)(10,7)
    (11,6)(12,5)};
\end{axis}
%
\begin{axis}[red, scale only axis, xmin=0,xmax=12, axis y line*=right, axis x line=none, ylabel=third ordinate (red)]%
\pgfplotsset{every outer y axis line/.style={xshift=2cm}, every tick/.style={xshift=2cm}, every y tick label/.style={xshift=2cm} }
    \addplot[smooth, red ,mark=+] coordinates {(0,4)
    (1,6)(2,8)
    (3,9)(4,13)
    (5,18)(6,29)
    (7,40)(8,50)
    (9,38)(10,27)
    (11,23)(12,10)};
\end{axis} 

\end{tikzpicture}
    \caption{PGFplot Code for three y-Axis}
    \label{fig:pgfplot-three}
\end{figure}
```

## Output
<a data-flickr-embed="true" href="https://www.flickr.com/photos/142248809@N07/52100272667/in/dateposted-public/" title="multiple y-axis in latex pgfplot"><img src="https://live.staticflickr.com/65535/52100272667_b3fcfb5139_o.png" width="437" height="639" alt="multiple y-axis in latex pgfplot"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>


## My Other Posts on PGFPlots
1. [Line Plotting using Latex PGFPlots](https://shantoroy.com/latex/how-to-draw-line-graph-using-pgfplots-latex/)
2. [Creating Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)
3. [Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot](https://shantoroy.com/latex/multiple-line-plots-using-tikz-pgfplot/)


## Other Latex-related Posts
You can find a comprehensive list of Latex resources in the following post:

[Latex Resources in a Nutshell](https://shantoroy.com/latex/latex-resources-in-a-nutshell/)

If you are a new Latex user, check out this post:
[20 Most Common Mistakes Made by New Latex Users](https://shantoroy.com/latex/common-mistakes-made-by-new-latex-typesetting-users/)

You can find all `Latex` oriented posts of mine in: [https://shantoroy.com/categories/#latex](https://shantoroy.com/categories/#latex)


* [How to write an algorithm in Latex](https://shantoroy.com/latex/how-to-write-algorithm-in-latex/)
* [How to add subfigure in Latex](https://shantoroy.com/latex/how-to-add-subfig-in-latex/)
* [Add Copyright Notice and Conference Name in IEEE Conference Template](https://shantoroy.com/latex/add-copyright-conference-name/)
* [Preparing Tables for Publication and Documentation in Latex](https://shantoroy.com/latex/how-to-create-tables-in-latex/)

* [How to Write Matrix with Row/Column Labels in Latex](https://shantoroy.com/latex/matrix-labeling-in-latex/)
* [How to Collaboratively Write a Paper using Overleaf Latex Platform](https://shantoroy.com/latex/how-to-collaborately-write-a-paper-using-latex-overleaf/)
* [Itemize, Enumerate, and To-do-list in Latex](https://shantoroy.com/latex/playing-with-latex-itemize-enumerate-fontawesome/)
* [Latex Table for Survey in IEEE two-column format](https://shantoroy.com/latex/latex-table-for-survey-ieee-template/)
* [How to add Codes in Latex:  `listings`  package for code documentation](https://shantoroy.com/latex/how-to-add-codes-in-latex-listing-package/)
* [Bibliography management with Bibtex in Latex](https://shantoroy.com/latex/bibliography-management-with-bibtex/)
* [How to Draw a Literature Survey Taxonomy Tree in Latex](https://shantoroy.com/latex/Draw-literature-survey-tree-in-latex/)
* [How to Convert Python Matplotlib Plots to Latex Plots (Easiest Way) for Academic Papers](https://shantoroy.com/latex/convert-matplotlib-plot-to-latex-plot/)
* [How to Draw Equations with Parameter Description in Latex using Tikz](https://shantoroy.com/latex/Draw-equations-with-parameter-description-in-latex/)

## References
1. [pgfplots: Legends in multiple y-axis plot overlapping](https://tex.stackexchange.com/questions/42697/pgfplots-legends-in-multiple-y-axis-plot-overlapping)
2. [Can I draw figure 3 y axis using pgfplot?](https://tex.stackexchange.com/questions/62291/can-i-draw-figure-3-y-axis-using-pgfplot)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjYwMDg3MTg0LDQ4MzYzOTE1NiwxMTI3Mz
kyODA5LC01NzE4NTk2MTBdfQ==
-->