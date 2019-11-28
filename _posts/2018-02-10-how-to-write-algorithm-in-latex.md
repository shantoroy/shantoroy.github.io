---
layout: single
title: "How to write algorithm in Latex"
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

You will find the code in [Overleaf](https://www.overleaf.com/read/rddymzwmnqgb) or clone with git from [here](https://git.overleaf.com/13752479mvffzrkgykhg)

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

\begin{algorithm}[H]
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

You will find the code in [Overleaf](https://www.overleaf.com/read/wzwnrbbwrvyx) or clone with git from [here](https://git.overleaf.com/13864807ptspmwgdbnqt)

The output will look like the following-
<figure>
	<a href="https://farm5.staticflickr.com/4612/26696807688_f6940a208e_b.jpg"><img src="https://farm5.staticflickr.com/4612/26696807688_f6940a208e_b.jpg"></a>
</figure>
