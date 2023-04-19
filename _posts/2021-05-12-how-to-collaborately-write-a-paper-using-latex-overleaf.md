---
layout: single
title: "How to Collaboratively Write a Paper using Overleaf Latex Platform"
excerpt:  "Collaborating with others on a writing project can be a challenge, especially when everyone is working on different parts of the document. Overleaf, a collaborative LaTeX editor, makes it easy to work together on documents in real time, with features like track changes and version control. In this post, we'll walk through the steps for setting up a collaborative writing project on Overleaf, from inviting collaborators to making changes and managing versions."
seo_title:  "How to Collaboratively Write a Paper using Overleaf Latex Platform"
seo_description:  "Learn how to collaborate on a writing project using Overleaf, a collaborative LaTeX editor that allows for real-time collaboration, track changes, and version control. Invite collaborators, make changes, and manage versions with ease."
header:
  image: "https://live.staticflickr.com/65535/51678387310_9e01a03f7e_o.png"
  teaser: "https://live.staticflickr.com/65535/51678387310_9e01a03f7e_o.png"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Overleaf
  - Sharelatex
  - paper writing
  - collaboration
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

We often collaboratively write manuscripts using Latex and [Overleaf](https://www.overleaf.com) the best online Latex platform. In this tutorial, I will discuss the best strategies to collaboratively work in a [Overleaf](https://www.overleaf.com) document.

## Selecting a Journal/Conference template
There are tons of templates available in the [Overleaf Gallery](https://www.overleaf.com/gallery). For writing a paper, we typically use a journal or conference template. For engineering students, the most common templates are:
* [ACM SigConf Template Overleaf](https://www.google.com/url?q=https%3A%2F%2Fwww.overleaf.com%2Flatex%2Ftemplates%2Fassociation-for-computing-machinery-acm-sig-proceedings-template%2Fbmvfhcdnxfty&sa=D&sntz=1&usg=AFQjCNH9E9ycWMKCwoFop9S-ac11ZVGyCg)
* [ACM Journal Template Overleaf](https://www.google.com/url?q=https%3A%2F%2Fwww.overleaf.com%2Flatex%2Ftemplates%2Fassociation-for-computing-machinery-acm-generic-journal-manuscript-template%2Fyffvrvzbhhpt&sa=D&sntz=1&usg=AFQjCNEEps62nCp5ix5_LzyoIQ5fjJsZxQ)
* [IEEE Conference template in Overleaf](https://www.google.com/url?q=https%3A%2F%2Fwww.overleaf.com%2Flatex%2Ftemplates%2Fieee-conference-template-example%2Fnsncsyjfmpxy&sa=D&sntz=1&usg=AFQjCNE1ZkmpzmLoyDXN6MkaDUouuUjrBQ)
* [IEEE Journal template in Overleaf](https://www.google.com/url?q=https%3A%2F%2Fwww.overleaf.com%2Flatex%2Ftemplates%2Fieee-journal-paper-template%2Fjbbbdkztwxrd&sa=D&sntz=1&usg=AFQjCNHTRHaB44Eu6y3XtwYP-nLHpNscqg)
* [Springer Book Chapter/Conference template in Overleaf](https://www.google.com/url?q=https%3A%2F%2Fwww.overleaf.com%2Flatex%2Ftemplates%2Fspringer-book-chapter%2Fhrdcrfynnzjn&sa=D&sntz=1&usg=AFQjCNFkAMPBlaldj62kIQpqnYtPvu8MOg)

Apart from these templates, you can download the zip file from an official conference or journal website and upload as a new project in Overleaf. However, typically, almost any journal or conference template can be found in the [Overleaf Academic Journal Gallery](https://www.overleaf.com/gallery/tagged/academic-journal). 


## Sharing the Document
After creating a new document using selected template, you need to share the document with your peers or collaborators. You can do it by clicking on `share` on the right top after entering the project. Now, a dialog box will pop up on your screen and you can share the project in two ways-
1. Using your collaborators' emails
2. Sharing the edit or view link after clicking on `Turn on link sharing` appered on the dialog box.


## Using package `todonotes`
Now you can use the package `todonotes` to comment on the document in a better way. For example, I want to use comments in the margin area, I can use the following code:
```latex
\usepackage{todonotes}
\newcommand{\Authorone}[1]{\todo[color=yellow!10, linecolor=black!50!yellow]{\textbf{AO:} #1}}
```
It will create a new command `\Authorone` and when using the command like the following will create a yellow background comment box and comment on top in the margin area.
```latex
\Authorone{This is author one's comment}
```
For a comment box inside the document paragraph area, you can use an extra argument `inline`, which is as follows:
```latex
\newcommand{\TODO}[1]{\todo[color=green!10, linecolor=black!50!green, inline]{\textbf{TODO:} #1}}
```


Feel free to check the outputs in this [Example Overleaf Document](https://www.overleaf.com/read/vnwqdpgvyhgv). The code of creating commands are put in between lines $66-69$. The comments are in line $260$, $266$, and $273$.

## Using the `Chat`
You can send messages to other collaborators by clicking `chat` button which is available on the right top. You can chat instantly like you do in messenger, whatsapp, or other instant messaging platforms.

## Using the `History`
The `history` button is also available on the right top where you can find all the changes made to the document by different authors. however, in the free version, you can find history of only last $24$ hours.

That's all for today. Have a good day. Cheers!


## Latex-related Posts
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
* [How to Create Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)
* [How to add Codes in Latex:  `listings`  package for code documentation](https://shantoroy.com/latex/how-to-add-codes-in-latex-listing-package/)
* [Bibliography management with Bibtex in Latex](https://shantoroy.com/latex/bibliography-management-with-bibtex/)
* [Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot](https://shantoroy.com/latex/multiple-line-plots-using-tikz-pgfplot/)
* [How to Draw a Literature Survey Taxonomy Tree in Latex](https://shantoroy.com/latex/Draw-literature-survey-tree-in-latex/)
* [How to Convert Python Matplotlib Plots to Latex Plots (Easiest Way) for Academic Papers](https://shantoroy.com/latex/convert-matplotlib-plot-to-latex-plot/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNTU4NTY1NTUsLTE3NDY0NDcwNThdfQ
==
-->