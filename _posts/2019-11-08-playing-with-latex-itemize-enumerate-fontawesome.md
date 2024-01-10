---
layout: single
title: "Itemize, Enumerate, and To-do-list in Latex"
excerpt:  "Learn how to make lists in Latex using the itemize, enumerate, and to-do-list environments. These are essential tools for organizing and presenting information in a clear and concise manner. Whether you're writing a research paper, a thesis, or simply taking notes, this tutorial will help you master the art of list-making in Latex."
seo_title:  "Itemize, Enumerate, and To-do-list in Latex: A Comprehensive Guide"
seo_description:  "Organize your text with ease using the itemize, enumerate, and to-do-list environments in Latex. From research papers to notes, this comprehensive guide will teach you the basics of list-making in Latex."
header:
  image: "https://live.staticflickr.com/65535/51648791820_873f7cea50_b.jpg"
  teaser: "https://live.staticflickr.com/65535/51648791820_873f7cea50_b.jpg"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

In this post we will learn how to use itemized lists in Latex.

## Unordered List
Unordered lists are created using the `\begin{itemize}...\end{itemize}` environment. Normally, an item is added using the `\item` command inside the environment.

```latex
\begin{itemize}
    \item first item
    \item second item
\end{itemize}
```

Usually, the command `\item` creates a bullet point list. If you want to use different notations, you need to use `[]` to customize the target notation.
```latex
\begin{itemize}
    \item[Q1.] first item
    \item[Q2.] second item
\end{itemize}
```

## Ordered List
Ordered list can be created using the `\begin{enumerate}...\end{enumerate}` environment. This simply adds $1,2,3,\dots$ to the items.

However, you can use `[i.]` with the environment to convert the number to appear as Roman numbers.
```latex
\usepackage{enumerate}
\begin{enumerate}[i.]
    \item first item
    \item second item
\end{enumerate}

```

## To-do Items
### Combining `fontawesome` and `itemize`
This is the best way to create and customize to-do lists. You can check the [fontawesome handbook](http://mirrors.ibiblio.org/CTAN/fonts/fontawesome/doc/fontawesome.pdf) for more symbols.
```latex
\usepackage{fontawesome}
\begin{itemize}
    \item[\faCheckSquareO] This is done
    \item[\faSquareO] To be done 
    \item[\faSquareO] To be done 
\end{itemize}
```

Here are some other example icons: 
```latex
\faCalendarCheckO, \faCalendarPlusO, \faCalendarMinusO, 
\faCheck, \faCheckCircleO, \faClone, 
\faClose, \faCut, \faEdit, \faMailForward, 
\faPencilSquareO, \faRemove
```

### Creating new `todolist` environment
Based on the thread in StackExchange:  [How to create checkbox todo list?](https://tex.stackexchange.com/questions/247681/how-to-create-checkbox-todo-list), here is another way to create such lists.
```latex
% enumitem clashes with enumerate
\usepackage{enumitem,amssymb} 
\newlist{todolist}{itemize}{2}
\setlist[todolist]{label=$\square$}

\usepackage{pifont}
\newcommand{\cmark}{\ding{51}}%
\newcommand{\xmark}{\ding{55}}%
\newcommand{\done}{\rlap{$\square$}{\raisebox{2pt}{\large\hspace{1pt}\cmark}}%
\hspace{-2.5pt}}
\newcommand{\wontfix}{\rlap{$\square$}{\large\hspace{1pt}\xmark}}
```

And then-
```latex
 \begin{todolist}
	  \item[\done] Frame the problem
	  \item Write solution
	  \item[\wontfix] profit
 \end{todolist}
```

That's all. Cheers!!!


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
eyJoaXN0b3J5IjpbLTEwMDg4MTU4OTAsLTEwODA4OTcwODMsLT
E3NzQ4MTY3OTBdfQ==
-->