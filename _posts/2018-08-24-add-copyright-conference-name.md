---
layout: single
title: "How to Add Copyright Notice and Conference Name in IEEE Conference Latex Template"
excerpt:  "If you're using the IEEE conference format to submit your research paper, you may want to add a copyright notice and conference name to your document. In this tutorial, we'll show you how to add these elements to your IEEE conference paper using LaTeX. We'll walk you through the process step by step and provide code examples to help you get started."
seo_title:  "How to Add Copyright Notice and Conference Name in IEEE Conference LaTeX Template"
seo_description:  "Learn how to add a copyright notice and conference name to your IEEE conference paper using LaTeX. Follow this step-by-step guide with code examples to customize your paper and meet the formatting requirements."
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

## Code for Copyright Notice and Conference Name

```latex
\documentclass[conference]{IEEEtran}
\usepackage[latin9]{inputenc}
\usepackage{amsmath}
\usepackage{graphicx}

\makeatletter

\def\ps@IEEEtitlepagestyle{
  \def\@oddfoot{\mycopyrightnotice}
  \def\@evenfoot{}
}
\def\mycopyrightnotice{
  {\footnotesize xxx-x-xxxx-xxxx-x/xx/\$31.00~\copyright~2018 IEEE\hfill} % <--- Change here
  \gdef\mycopyrightnotice{}
}


\@ifundefined{showcaptionsetup}{}{
 \PassOptionsToPackage{caption=false}{subfig}}
\usepackage{subfig}
\makeatother

\usepackage{eso-pic}
\newcommand\AtPageUpperMyright[1]{\AtPageUpperLeft{
 \put(\LenToUnit{0.5\paperwidth},\LenToUnit{-1cm}){
     \parbox{0.5\textwidth}{\raggedleft\fontsize{9}{11}\selectfont #1}}
 }}
\newcommand{\conf}[1]{
\AddToShipoutPictureBG*{
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


If you find this post helpful, and want to support this blog, you can
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="shantoroy" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script> or

<div style="width: 300px; height: 200px;">
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


* [How to write an algorithm in Latex](https://shantoroy.com/latex/how-to-write-algorithm-in-latex/)
* [How to add subfigure in Latex](https://shantoroy.com/latex/how-to-add-subfig-in-latex/)
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM1NzA0MTE1Nyw4Njg4OTI3MjgsLTEzMD
MxOTkxMzQsLTE2MDI2MzM2ODZdfQ==
-->