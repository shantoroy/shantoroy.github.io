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



<figure>
<a href="https://www.rakuten.com/r/STONEH425?eeid=44971" target="_blank">
  <img src="/assets/images
/Rakuten-Promotion-Banner.png" alt="Rakuten Promotion get 30 dollar" width="100%">
</a>
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

If you find this post helpful, and want to support this blog, you can
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="shantoroy" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script> or

<div style="width: 200px; height: 150px;">
<form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="business" value="Q9F45GULUSYMY" />
<input type="hidden" name="no_recurring" value="0" />
<input type="hidden" name="item_name" value="I appreciate your support! 😊" />
<input type="hidden" name="currency_code" value="USD" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
</form></div>



## Related Posts
You can find a comprehensive list of Latex resources in the following post:

[Latex Resources in a Nutshell](https://shantoroy.com/latex/latex-resources-in-a-nutshell/)

If you are a new Latex user, check out this post:
[20 Most Common Mistakes Made by New Latex Users](https://shantoroy.com/latex/common-mistakes-made-by-new-latex-typesetting-users/)

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


## Promotions and Referrals (US Residents Only)
* **Chime:** Open a Checking account at Chime using [my referral link](https://chime.com/r/shantoroy) and get $100 after your employer deposit paycheck of minimum $200 within the first 45 days. 
* **Rakuten:** Get $30 after you spend $30 at Rakuten select stores after you use [my referral link](www.rakuten.com/r/STONEH425?eeid=44971) to open an account. 
* **Chase Freedom Credit Card:** Earn $200 cash back with Chase Freedom Unlimited or Chase Freedom Flex credit card. I can be rewarded if you apply using [my referral link](https://www.referyourchasecard.com/18o/E7MB03IG12) and are approved for the card.

* **Chase Checking Account:** Get $200 when you open a checking account using [my referral link](https://accounts.chase.com/raf/share/2564396166) after your first salary is deposited. 
* **Discover:** Earn $50 cash back with Discover when you apply using [my referral link](https://refer.discover.com/s/SHANTO10) and are approved for the card.
* **Amex Blue Cash Preferred:** Earn $250 as statement credit when you spend $3000 in first six months. Apply using [my referral link](https://americanexpress.com/en-us/referral/SHANTRzUOO?XL=MIANS).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE2ODIxOTExOSwxODY5NzU4NTI5LDM3Mz
E2ODI2MiwxNTI0ODk1ODM1LDc1NTMyMTQ0NywxMDUyNTIwNjEw
LDg2NjkzNjExMiwtMTkyMjgzOTA4MSwxMzQwNTY5ODA1LDE2NT
I4NTMzNTRdfQ==
-->