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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMTI2Mzk5NjMsLTE3NzQ4MTY3OTBdfQ
==
-->