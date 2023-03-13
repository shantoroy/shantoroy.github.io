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
1. [Line Plotting using Latex PGFPlots](https://shantoroy.com/latex/line-graph-pgfplots/)
2. [Creating Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)
3. [Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot](https://shantoroy.com/latex/multiple-line-plots-using-tikz-pgfplot/)

## References
1. [pgfplots: Legends in multiple y-axis plot overlapping](https://tex.stackexchange.com/questions/42697/pgfplots-legends-in-multiple-y-axis-plot-overlapping)
2. [Can I draw figure 3 y axis using pgfplot?](https://tex.stackexchange.com/questions/62291/can-i-draw-figure-3-y-axis-using-pgfplot)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDgzNjM5MTU2LDExMjczOTI4MDksLTU3MT
g1OTYxMF19
-->