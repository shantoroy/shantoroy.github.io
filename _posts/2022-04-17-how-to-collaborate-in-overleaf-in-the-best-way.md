---
layout: single
title: "How to Utilize Overleaf Latex platform for Collaboration!!!"
excerpt:  "Overleaf is a popular web-based platform for writing and collaborating on LaTeX documents. The platform is widely used extensively in the academic communities. This article provides a comprehensive guide on how to use Overleaf for collaboration and how to utilize its features to make the collaborative writing process easier and more efficient."
seo_title:  "A Complete Guide to Collaborating on LaTeX Documents with Overleaf"
seo_description:  "Looking for an efficient way to collaborate on LaTeX documents with your collaborators? Check out this guide on how to use Overleaf, the most popular web-based LaTeX platform. In this post, I discuss how to make our collaborative writing process smoother and more streamlined. Learn how to utilize Overleaf's features to boost your team's productivity and create high-quality LaTeX documents quickly and easily."
header:
  image: "https://live.staticflickr.com/65535/52012497165_8a03814fd4_o.png"
  teaser: "https://live.staticflickr.com/65535/52012497165_8a03814fd4_o.png"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Documentation
  - Collaboration
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


We often write a paper in latex and use the overleaf platform for collaboration purpose. In fact we use overleaf for all types of documentation no matter if it is for collaboration or personal purpose, for example, notes, homeworks, reports, etc.

Overleaf is the best platform out there for collaboration tasks and researchers' number one choice. In this post, I will discuss how to utilize the platform for collaboration tasks.

Let's start!

### Organizing the Files in Folders
Keep all the different types of contents in seperate folders. For example, I always create separate folders for images, sections, tables, and latex graphs. You can even create subfolders for organizing section-wise contents.

The primary benifit of organizing all these contents is, everyone can easily find out specific contents without putting that much effort. 

### Use Different Files for Sections
Never write all sections in a single tex file. I usually create separate tex files for each section. For example, if I am writing a paper and I have the five most common sections, I create `intro.tex`, `background.tex`, `method.tex`, `result.tex`, and `conclude.tex` for writing the introduction, literature review, methodology/model, implementation/result, related work/conclusion/future work, respectively.

### Keep the `main.tex` Clean
I recommend putting only the packages, document title, author names, and section files inclusion in the `main.tex` file. Many people write the whole paper or book in the main file which is not convenient at all when someone else edit the contents.

As said earlier, I create separate files for sections and then keep the files under a folder named `sections`. All I need to do is, add the section files in the `main.tex` as follows:

```latex
\input{sections/intro.tex}
\input{sections/background.tex}
\input{sections/method.tex}
\input{sections/result.tex}
\input{sections/conclude.tex}
```



### Using Relevant Names for Files and Folders
Most people name the files based on the contents. however, there are people who just name a file like `a.tex`, `this.tex`, `that.png`, `yyy.jpg`, etc., which is not convenient to understand the underlying contents without opening the file. Try to keep the name relevant.


### Using `todonotes` package for commenting
I did not know about this package until I joined the RNS lab here in the University of Houston. My professor and other collaborators always use this package for named comments in the margin.

You can use inline comments or other boxs outside the margin. In the following code, I created three new commands `\iTODO`, `\shanto`, and `\roy`.

```latex
\usepackage[textsize=tiny, textwidth=1.2cm]{todonotes}
\newcommand{\iTODO}[1]{\todo[color=yellow!10, linecolor=black!50!yellow, inline]{\textbf{TODO:} #1}}
\newcommand{\shanto}[1]{\todo[color=green!10, linecolor=black!50!green]{\textbf{SR1:} #1}}
\newcommand{\roy}[1]{\todo[color=red!10, linecolor=black!50!red, inline]{\textbf{SR2:} #1}}
```

Now, to put a comment, I can do this:

```latex
\shanto{this is a comment.}
```
and it will show up in a box like `SR1: this is a comment`. Use different colors for different authors.

### Use Red and Blue for Changed texts
If you are revising your contents, it is better to use different colors for the change. The following code helps you to show red textthrough line for the removed text and the blue for the newly added texts.
```latex
\usepackage[normalem]{ulem}
\newcommand{\change}[2]{\sout{\textcolor{red}{#1}}\textcolor{blue}{#2}}
```

Now write like this:
```latex
There is definitely some changes, for example, \change{this is an old text}{write something new here}.
```
Here, `this is an old text` was written in the previous version. Now, i changed the line to `write something new here`. It will be easier for other collaborators to understand what changes have been made here.

Also, when the full revision is done, if you want the new text only in usual black font color, just add this after the first code. It will overwrite the previous definition of the `\change` command.

```latex
\renewcommand{\change}[2]{\textcolor{black}{#2}}
```

### Share `edit/view link` to others
Share the `edit link` with others if you allow them to edit the document. If you do not want them to edit but check out the writing, then share the `view link`.

### Using the `Chat` box for instant communication
Although I do not use it, however, might be useful for different situation. For example, if you have to submit today, everyone is editing at the same time, and you need frequent communication, then the `chat` option can be extremely useful.

### Always Check the `History`

If you want to find out who is contributing what part and what they have changed so far, you can check the `history` tab. It works as a version control system. Although, to check the full history you will need a premium account. In the free version, you can check up to last 24 hours.

That's all for now. please, let me know if I have missed any important tip that needs to be included in this post.


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
* [How to Draw Equations with Parameter Description in Latex using Tikz](https://shantoroy.com/latex/Draw-equations-with-parameter-description-in-latex/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNjgwMDkzOTAsMzIxMzU1MjM4LDIxMz
M5Mzc4NjFdfQ==
-->