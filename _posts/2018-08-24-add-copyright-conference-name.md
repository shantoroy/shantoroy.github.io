---
layout: single
title: "Add Copyright Notice and Conference Name in IEEE Conference Template"
header: 
  image: "https://farm5.staticflickr.com/4833/44165377060_0353fbcc5c_b.jpg"
  teaser: "https://farm5.staticflickr.com/4833/44165377060_0353fbcc5c_b.jpg"
categories: 
  - Latex
tags:
  - Latex
  - Tutorial
toc: true
toc_label: "Table of Contents"
toc_icon: "heart" 
---

After sending the acceptance notification, most of the IEEE conferences ask authors to add a copyright notice at the left footer and the conference name at the right header position of the first page in the manuscript. In this tutorial, I note the required code to do that.

## Code for "Copyright Notice" and "Conference Name"

```latex
\documentclass[conference]{IEEEtran}
\usepackage[latin9]{inputenc}
\usepackage{amsmath}
\usepackage{graphicx}

\makeatletter

\def\ps@IEEEtitlepagestyle{%
  \def\@oddfoot{\mycopyrightnotice}%
  \def\@evenfoot{}%
}
\def\mycopyrightnotice{%
  {\footnotesize xxx-x-xxxx-xxxx-x/xx/\$31.00~\copyright~2018 IEEE\hfill}% <--- Change here
  \gdef\mycopyrightnotice{}
}


\@ifundefined{showcaptionsetup}{}{
 \PassOptionsToPackage{caption=false}{subfig}}
\usepackage{subfig}
\makeatother

\usepackage{eso-pic}
\newcommand\AtPageUpperMyright[1]{\AtPageUpperLeft{%
 \put(\LenToUnit{0.5\paperwidth},\LenToUnit{-1cm}){%
     \parbox{0.5\textwidth}{\raggedleft\fontsize{9}{11}\selectfont #1}}%
 }}%
\newcommand{\conf}[1]{%
\AddToShipoutPictureBG*{%
\AtPageUpperMyright{#1}
}
}

\title{Your Paper Title goes right Here}
\conf{International Conference on XXXXX, XXXX and XXXXX (ICXXX) 14-16 November, 2018} % Change according to their suggestion

\begin{document}

\author{\IEEEauthorblockN{Author I\IEEEauthorrefmark{1}, Author II\IEEEauthorrefmark{2}, Author III\IEEEauthorrefmark{3}, and Author IV\IEEEauthorrefmark{4}}
\IEEEauthorblockA{Dept of Computer Science and Engineering, University of X,
Country X\IEEEauthorrefmark{1}\\
Dept of Computer Science and Engineering, University of Y, Country Y\IEEEauthorrefmark{2}\IEEEauthorrefmark{3}\\
Institute of Information Technology, University of Z, Country Z\IEEEauthorrefmark{4}\\
Email: authorI\IEEEauthorrefmark{1}@gmail.com,  authorII\IEEEauthorrefmark{2}@ieee.org,  authorIII\IEEEauthorrefmark{3}@gmail.com,
authorIV\IEEEauthorrefmark{4}@universityz.edu}
}


\maketitle
\begin{abstract}
Abstract goes here
\end{abstract}

\section{Introduction}
Introduction here

\section{Literature Overview}
Background or existing work summaries \cite{roy2017combined}

\section{Methodology}
Methodology explained here

\section{Implementation and Result}
Graphs or outputs here

\section{Discussion}
Significance, Limitations, and Future works here

\section{Conclusion}
Conclusion here

\bibliographystyle{IEEEtran}
\bibliography{References}   % Using Bibtex for References.bib


% that's all folks
\end{document}
```

You will find the code in [Overleaf](https://www.overleaf.com/read/rvcwtfkzsxgn)

The output will look like the following-
<figure>
  <a href="https://farm5.staticflickr.com/4910/44165382050_376fa6e935_b.jpg"><img src="https://farm5.staticflickr.com/4910/44165382050_376fa6e935_b.jpg"></a>
</figure>


