---
layout: single
title: "How to write algorithm in Latex"
excerpt:  "Learn how to write algorithms in Latex using the algorithmicx package. This package provides an easy-to-use and flexible environment for writing algorithms with customizable formatting options. With Latex, you can create professional-looking algorithms for your research papers, theses, or technical reports." 
seo_title:  "How to Write Algorithm in Latex: A Comprehensive Guide"
seo_description:  "Want to write algorithms in Latex? Discover the algorithmicx package, a powerful tool for creating professional-looking algorithms for research papers, theses, or technical reports. In this guide, learn how to write algorithms in Latex with customizable formatting options."
header:
  image: "https://farm5.staticflickr.com/4662/40356609652_d977cf85a9_b.jpg"
  teaser: "https://farm5.staticflickr.com/4662/40356609652_d977cf85a9_b.jpg"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

While writing any research article in Latex, so often we demonstrate an algorithm according to our proposed model, workflow or architecture.

It can be done so easily using the `algorithm` or `algorithm2e` package in `article` documentclass. Some demo codes including the loops, functions and comments are given below.

## Code using `algorithm` package

```latex
\documentclass[a4paper]{article}

\usepackage[margin=1.5in]{geometry}    % For margin alignment
\usepackage[english]{babel}
\usepackage[utf8]{inputenc}
\usepackage{algorithm}
\usepackage{arevmath}     % For math symbols
\usepackage[noend]{algpseudocode}

\title{Algorithm template}
\author{Roy}

\date{\today}    % Today's date

\begin{document}
\maketitle
\section{Demo code}

\begin{algorithm}
\caption{Put your caption here}
\begin{algorithmic}[1]

\Procedure{Roy}{$a,b$}       \Comment{This is a test}
    \State System Initialization
    \State Read the value 
    \If{$condition = True$}
        \State Do this
        \If{$Condition \geq 1$}
        \State Do that
        \ElsIf{$Condition \neq 5$}
        \State Do another
        \State Do that as well
        \Else
        \State Do otherwise
        \EndIf
    \EndIf

    \While{$something \not= 0$}  \Comment{put some comments here}
        \State $var1 \leftarrow var2$  \Comment{another comment}
        \State $var3 \leftarrow var4$
    \EndWhile  \label{roy's loop}
\EndProcedure

\end{algorithmic}
\end{algorithm}

\end{document}
```

You will find the code in [Overleaf](https://www.overleaf.com/read/rddymzwmnqgb).

The output will look like the following-
<figure>
	<a href="https://farm5.staticflickr.com/4747/25697721187_0986b0d994_b.jpg"><img src="https://farm5.staticflickr.com/4747/25697721187_0986b0d994_b.jpg"></a>
</figure>


## Code using `algorithm2e` package

```latex
\documentclass{article}
\usepackage{xcolor}
\usepackage[linesnumbered,ruled,vlined]{algorithm2e}

\title{Another algorithm template}
\author{Roy}

%%% Coloring the comment as blue
\newcommand\mycommfont[1]{\footnotesize\ttfamily\textcolor{blue}{#1}}
\SetCommentSty{mycommfont}

\SetKwInput{KwInput}{Input}                % Set the Input
\SetKwInput{KwOutput}{Output}              % set the Output


\begin{document}
\maketitle

\begin{algorithm}[!ht]
\DontPrintSemicolon
  
  \KwInput{Your Input}
  \KwOutput{Your output}
  \KwData{Testing set $x$}
  $\sum_{i=1}^{\infty} := 0$ \tcp*{this is a comment}
  \tcc{Now this is an if...else conditional loop}
  \If{Condition 1}
    {
        Do something    \tcp*{this is another comment}
        \If{sub-Condition}
        {Do a lot}
    }
    \ElseIf{Condition 2}
    {
    	Do Otherwise \;
        \tcc{Now this is a for loop}
        \For{sequence}    
        { 
        	loop instructions
        }
    }
    \Else
    {
    	Do the rest
    }
    
    \tcc{Now this is a While loop}
   \While{Condition}
   {
   		Do something\;
   }

\caption{Example code}
\end{algorithm}

\end{document}
```

You will find the code in [Overleaf](https://www.overleaf.com/read/wzwnrbbwrvyx).

The output will look like the following-
<figure>
	<a href="https://farm5.staticflickr.com/4612/26696807688_f6940a208e_b.jpg"><img src="https://farm5.staticflickr.com/4612/26696807688_f6940a208e_b.jpg"></a>
</figure>


## Write Function within Algorithm
```latex
\begin{algorithm}[H]
\SetKwInput{KwInput}{Input}                % Set the Input
\SetKwInput{KwOutput}{Output}              % set the Output
\DontPrintSemicolon
  
  \KwInput{Your Input}
  \KwOutput{Your output}
  \KwData{Testing set $x$}

% Set Function Names
  \SetKwFunction{FMain}{Main}
  \SetKwFunction{FSum}{Sum}
  \SetKwFunction{FSub}{Sub}
 
% Write Function with word ``Function''
  \SetKwProg{Fn}{Function}{:}{}
  \Fn{\FSum{$first$, $second$}}{
        a = first\;
        b = second\;
        sum = first + second\;
        \KwRet sum\;
  }
  \;

% Write Function with word ``Def''
  \SetKwProg{Fn}{Def}{:}{}
  \Fn{\FSub{$first$, $second$}}{
        a = first\;
        b = second\;
        sum = first - second\;
        \KwRet sum\;
  }
  \;

  \SetKwProg{Fn}{Function}{:}{\KwRet}
  \Fn{\FMain}{
        a = 5\;
        b = 10\;
        Sum(5, 10)\;
        Sub(5, 10)\;
        print Sum, Sub\;
        \KwRet 0\;
  }
\end{algorithm}
```

You will find the code in [Overleaf](https://www.overleaf.com/read/qpsqbngcqkpq).

The output will look like the following-
<figure>
	<a href="https://live.staticflickr.com/65535/49815560527_396893a427_z.jpg"><img src="https://live.staticflickr.com/65535/49815560527_396893a427_z.jpg"></a>
</figure>


## Related Posts
You can find a comprehensive list of Latex resources in the following post:

[Latex Resources in a Nutshell](https://shantoroy.com/latex/latex-resources-in-a-nutshell/)

You can find all `Latex` oriented posts of mine in: [https://shantoroy.com/categories/#latex](https://shantoroy.com/categories/#latex)

Some of those are included here.
* [Add Copyright Notice and Conference Name in IEEE Conference Template](https://shantoroy.com/latex/add-copyright-conference-name/)
* [Preparing Tables for Publication and Documentation in Latex](https://shantoroy.com/latex/how-to-create-tables-in-latex/)
* [Creating Bar Charts using Latex PGFPlots](http://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)
* [Line Plotting using Latex PGFPlots](https://shantoroy.com/latex/how-to-draw-line-graph-using-pgfplots-latex/)
* [How to add subfigure in Latex](https://shantoroy.com/latex/how-to-add-subfig-in-latex/)
* [How to Write Matrix with Row/Column Labels in Latex](https://shantoroy.com/latex/matrix-labeling-in-latex/)
* [How to Collaboratively Write a Paper using Overleaf Latex Platform](https://shantoroy.com/latex/how-to-collaborately-write-a-paper-using-latex-overleaf/)
* [Itemize, Enumerate, and To-do-list in Latex](https://shantoroy.com/latex/playing-with-latex-itemize-enumerate-fontawesome/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjQ1OTc4MTMxLC0xOTIyODM5MDgxLDEzND
A1Njk4MDUsMTY1Mjg1MzM1NF19
-->