---
layout: single
title: "PhD/MS Dissertation Latex Template for Students of the College of Natural Sciences and Mathematics- University of Houston"
excerpt:  "Writing a thesis or dissertation can be daunting in Latex, especially when it comes to formatting, including tables and algorithms or subfigures. Fortunately, the University of Houston's College of Natural Sciences and Mathematics offers a LaTeX template that can make the process much easier. However, it is not designed in a modular way. In this blog post, I will guide you through the steps of using the template in a more organized and modular way to write your PhD or MS dissertation."
seo_title:  "University of Houston: Organized and Modular NSM Dissertation LaTeX Template"
seo_description:  "Make writing your PhD or MS dissertation easier with the LaTeX template provided by the University of Houston's College of Natural Sciences and Mathematics. In this tutorial, the modular organization will help you use this template to format your thesis with ease."
header:
  image: "https://live.staticflickr.com/65535/52014195409_effd1f1538_o.png"
  teaser: "https://live.staticflickr.com/65535/52014195409_effd1f1538_o.png"
categories:
  - Latex
tags:
  - Template
  - NSM-UH
  - University of Houston
  - Latex
  - Dissertation
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Although I am not anywhere close to writing dissertation, I wanted to check out the PhD/MS latex template University of Houston NSM uses. 

Later, I found it and modified it with a lot better organization. I also added examples of writing algorithm, creating subfigures, pgfplots, and comments, etc.

I hope, it helps the upcoming PhD/MS students of the [College of Natural Sciences and Mathematics](https://www.uh.edu/nsm/), [University of Houston](https://www.uh.edu/).

Please, find the template here:
[UH NSM Dissertation Template on Overleaf](https://www.overleaf.com/read/shdqcsrbbvnz)

## Organization
### Primary Organization
1. `main.tex` $\rightarrow$ contains packages and inputs sections and intro files
2. `References.bib` $\rightarrow$ contains references in bibtex format. If you don't know how to manage references using bibtex, checkout my [other post](https://shantoroy.com/latex/bibliography-management-with-bibtex/)
3. folders containing files of different type of contents

### Folders
1. `algorithms` $\rightarrow$ Includes algorithms in separate files.
2. `chapters` $\rightarrow$ Includes separate file for each section. Final dissertations are supposed to have chapters, which have many sections. Not sure, why they used sections here. But, it what it is.
3. `data` $\rightarrow$ If you have XLS or CSV files for `latex graphs`, put these files here.
4. `figures` $\rightarrow$ Include all your figures in this folder
5. `intro_files` $\rightarrow$ this folder includes the `acknowledgement`, `cover page`, `dedication`, and `abstract`.
6. `miscellaneous` $\rightarrow$ You do not need to do anything here. Just keep it as it is. The document style file and bibliographic style files are included here. Just to keep the main folder clean.
7. `tables` $\rightarrow$ Put your tables in this folder
8. `tex_graphs` $\rightarrow$ If you have `pgfplot graphs`, just use different files for each graph and put those files in this folder
9. `trash` $\rightarrow$ Not really important. Only in case if you want to dump unnecessary files, you can use this folder. I recommend putting these files here rather than deleting because from my experience, sometimes we may need a few deleted files back.


## New Addition
I have included several packages that may or may not be necessary for you.  I just included these in case you need these types of items in the document.

### Algorithm
I have added the `algorithm2e` package for writing an algorithm. Also, added a demo algorithm in the `Methodology` section for your reference. For more details check out my other post:

[How to write algorithm in Latex](https://shantoroy.com/latex/how-to-write-algorithm-in-latex/).

### Subfigures
Added a few codes in the `Evaluation` section to show how to add subfigures in latex. For details, you can check out this post:

[How to add subfigure in Latex](https://shantoroy.com/latex/how-to-add-subfig-in-latex/).

### PGFPlots
My professor prefers `pgfplots` over python generated graphs as these graphs can be easily configured if the template is changed. Here, I added necessary packages for latex graphs and provided a few examples as well. The data has been used here is located in the `data` folder. For details, check out my other posts:

* [Line Plotting using Latex PGFPlots](https://shantoroy.com/latex/how-to-draw-line-graph-using-pgfplots-latex/)
* [Creating Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)
* [Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot](https://shantoroy.com/latex/multiple-line-plots-using-tikz-pgfplot/)

### ToDoNotes
Added the package `todonotes` for creating outside-margin comments. I like to use this type of comments for collaboration and for myself. There is an example as well. I just added a command under my name as `\shanto{}` and write contents within it.


## Other Advices

1. Use [Table Generator](https://www.tablesgenerator.com/) for creating tables
2. Use [Grammarly](https://app.grammarly.com/) for spell and grammar checking
3. Check out [Latex Resources](https://shantoroy.com/latex/latex-resources-in-a-nutshell/)
4. Create any types of diagrams using [draw.io](https://www.draw.io)


Please let me know, if I should include anything else.

Once again, you will find the template on [Overleaf](https://www.overleaf.com/read/shdqcsrbbvnz). 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwNDA1MDkwNDQsLTE2Njg0OTUyODQsLT
YyOTM4NDY1XX0=
-->