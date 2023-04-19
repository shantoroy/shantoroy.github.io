---
layout: single
title: "20 Most Common Mistakes Made by New Latex Users"
excerpt: "Are you new to LaTeX and struggling to get the desired output for your document? You are not alone. Many new users make common mistakes that hinder their progress. In this post, we will discuss the top 20 most common mistakes made by new LaTeX users and how to avoid them."
seo_title: "20 Most Common Mistakes Made by New Latex Users"
seo_description: "Are you struggling to use LaTeX for your document? Learn how to avoid the 20 most common mistakes made by new LaTeX users and improve your LaTeX skills."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - Latex
tags:
  - Latex
  - Mistakes
  - Reddit
  - StackExchange
  - bibtex
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

LaTeX is a powerful typesetting language used for creating high-quality documents, such as academic papers, reports, and presentations. It is known for its ability to produce professional-looking documents with complex mathematical equations, diagrams, and figures. 

However, for new users, LaTeX can be confusing, leading to many common mistakes. In this blog post, I will discuss the 20 most common mistakes made by new LaTeX users and provide tips on how to avoid them. 

By learning from these mistakes, you can save time, frustration, and improve the quality of your documents.

## Common Mistakes for New Users
1.  **Not making enough use of LaTeX's features:**  LaTeX is a powerful typesetting system that can do a lot of things automatically. New users often try to do too much manually, which can lead to errors and frustration. For example, I used to do so much manual stuffs over and over when there is just a one-line command that could solve the problem throughout the document.
2.  **Not using the right packages:**  There are many LaTeX packages available that can add new features and functionality to your documents. New users often don't know about these packages, or they don't know how to use them. It's always recommended to search for the required packages if having an error. I used to miss adding `graphicx` (for figures) a lot of times when started a new blank project.
3.  **Not understanding the document structure:**  LaTeX documents are organized in a specific way. New users often don't understand this structure, which can lead to errors and confusion. Many new users used to have hard times finding the right file if their collaborators used different files to divide the whole text of the document. It's typically using other `<file_name>.tex` as `\input{<path/file_name>.tex}` within the main file or another file to avoid putting large content in a single file.
4.  **Not using the right commands:**  LaTeX has a large number of commands that can be used to format your documents. New users often don't know which commands to use, or they don't know how to use them correctly. Same thing can be achieved in multiple ways and it's difficult sometimes to find out the best ones to use. For example, there are seperate packages to [write an algorithm](https://shantoroy.com/latex/how-to-write-algorithm-in-latex/) or [add subfigures](https://shantoroy.com/latex/how-to-add-subfig-in-latex/) in Latex.
5.  **Not using the right environments:**  LaTeX has a number of environments that can be used to format specific types of content, such as lists, tables, and figures. New users often don't know which environments to use, or they don't know how to use them correctly. Also, you may be amused by looking at `\begin{figure}...\end{figure}` vs `\begin{figure*}...\end{figure*}`. So, in a two column format document, the first one puts the figure in one column and the later one puts the image across both columns (if you need wider space). You can check [Itemize, Enumerate, and To-do-list in Latex](https://shantoroy.com/latex/playing-with-latex-itemize-enumerate-fontawesome/).
6.  **Not using the right line breaks:**  LaTeX can automatically break pages for you, but you can also manually break pages if you need to. New users often don't know how to manually break pages, or they don't know when to do it. I have seen people using  `\\`  (two backslashes) or `\newline` or `\hfill \break`, which is not necessary most of the times. If you simply start a new paragraph after pressing Enter or Return 2/3 or more times, you automatically get line breaks.
7.  **Not using the right sectioning commands:**  LaTeX has a number of sectioning commands that can be used to create different levels of headings in your documents. New users often don't know which sectioning commands to use, or they don't know how to use them correctly. Always follow the tree: `\chapter`$\rightarrow$`\section`$\rightarrow$`\subsection`$\rightarrow$`\subsubsection`$\rightarrow$`\paragraph`. Well, except for books, you do not need to use `\chapter`.
8.  **Not using the right cross-referencing commands:**  LaTeX has a number of cross-referencing commands that can be used to create links between different parts of your documents. New users often don't know which cross-referencing commands to use, or they don't know how to use them correctly. The most usual way is using `\ref{<label>}`. If your figure has the label `\label{fig:test-image}`, refer it as `Figure~\ref{fig:test-image}` within the texts.
9.  **Not using the right bibliography commands:**  LaTeX has a number of bibliography commands that can be used to create a bibliography for your document. New users often don't know which bibliography commands to use, or they don't know how to use them correctly. I would always suggest using the `bibtex`. At first, it may seem complex, but trust me, it will save you tons of times in the future. You can check [Bibliography management with Bibtex in Latex](https://shantoroy.com/latex/bibliography-management-with-bibtex/).
10.  **Not using the right tools:**  There are a number of tools available that can help you with LaTeX, such as editors, previewers, and table generators. New users often don't know about these tools, or they don't know how to use them. For example, many people don't even know that using `tablesgenerator.com`, they can easily create table like MS word and generate corresponding Latex codes for tables. You can check [Preparing Tables for Publication and Documentation in Latex](https://shantoroy.com/latex/how-to-create-tables-in-latex/).
11.  **Not asking for help:**  If you're having trouble with LaTeX, there are a number of resources available to help you, such as online forums, mailing lists, and books. Don't be afraid to ask for help! I have always asked my professor and labmates for help. To get help online, the best way is to post your issues on [r/LaTeX/](https://www.reddit.com/r/LaTeX/) or [tex.stackexchange](https://tex.stackexchange.com/). You'll have some answers for sure.
12. **Not Using Overleaf for Project Management:** Many people start installing latex on their machine to work offline and that's the biggest mistake you would ever make. Use [Overleaf](https://www.overleaf.com/) for any of your projects. You don't need to install anything. Access your projects from anywhere in the earth. If you are concerned about privacy, just let me make your doubt clear by ensuring that almost all professors and researchers use overleaf to manage their publications, note taking, and other documentations. If you are looking for a list of online tools, check out [A Comprehensive List of Free OnlineTools for Researchers, Students, and Authors](https://medium.com/@shantoroy/a-comprehensive-list-of-free-onlinetools-for-researchers-students-and-authors-b01ec48b19d2).
13. **Not Using Tikz/PGFPlots for Graph:** I know it takes some time to learn how to use `tikz/pgfplots` for plotting things. But, it actually provides significantly better quality than putting a python/R generated graph because of font size/matching issue across different templates. You can get the code of almost any type of graph here on [PGFplot gallery](https://pgfplots.sourceforge.net/gallery.html). You can also checkout my posts: [Creating Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/), [Line Plotting using Latex PGFPlots](https://shantoroy.com/latex/how-to-draw-line-graph-using-pgfplots-latex/), and [Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot](https://shantoroy.com/latex/multiple-line-plots-using-tikz-pgfplot/). One more suggestion is to convert your python matplotlib-to-pgfplot code converter. Check out: [How to Convert Python Matplotlib Plots to Latex Plots](https://shantoroy.com/latex/convert-matplotlib-plot-to-latex-plot/).
14. **Not Organizing Documents/Files:** Organizing is good for managing a document. It's better to put all images under a folder named `figures` or `images` and then use `\includegraphics{figures/test_image.png}` like that. Similarly, I use seperate folders to maintain sections, tables, algorithms, and all different types of contents. Also, use seperate files for each section and then use something like `\input{sections/intro.tex}` in the `main.tex` to add introduction to the document (if you write introduction section in a file named `intro.tex` and it's located under `sections` folder). I usually avoid putting contents in the main file, it makes the life easier.
15. **Using improper syntax:** Syntax errors such as forgetting to close brackets or parentheses is quite common at the beginning. Especially when people use equations and use `$$`, they forget to close a `$` with another and makes life hell. Also, do not use `&` in the text, always use the word `and` because `&` is a special character typically used in a table environment. Many new users use `&` within texts and can't figure out what the error even is.
16. **Using hard-coded spacing:** instead of using LaTeX's automatic spacing, many new users start using `\vspace{3mm}` or  `\\\\\\` or similar other commands to have spaces between paragraphs. Well, you can use and tweak similar to something as follows:
	```latex
	\setlength{\parskip}{\baselineskip}%
	\setlength{\parindent}{0pt}%
	```
17. **Searching Templates Elsewhere:** I would suggest not looking for templates on different sites when you have everything on [Overleaf Template Gallery](https://www.overleaf.com/latex/templates). If you need ACM format, it's there. If you need IEEE format, it's there. Literally all journal templates are available there. There are tons of CV/resume and Homework/report templates as well. Just choose the one you like most.
18. **Including non-ASCII characters without properly encoding them:** Sometimes new users copy paste contents from pdfs and this can end in errors because of encoding issues. What I prefer is using notepad/grammerly or similar tools first to paste and then copy agin from there and then paste on Latex.
19. **Not properly handling errors or warnings generated by LaTeX** Warnings are okay. But, you definitely should fix the errors. Just check out what is the issue and then google it. Or now, there is `chatGPT`. 😎
20. **Create new document to move to a new template:** Many new users create/start a new document, for example, say they need to change from IEEE conference template to ACM conference template. So, you do not need to create a whole new document and paste things there. In the main file headers just change the class/style files and do some extra lines of tweaking (e.g., author section) and you are just good to go. Literally saves a few hours at the least.


## Latex-related Posts on my Blog
* [Add Copyright Notice and Conference Name in IEEE Conference Template](https://shantoroy.com/latex/add-copyright-conference-name/)
* [Preparing Tables for Publication and Documentation in Latex](https://shantoroy.com/latex/how-to-create-tables-in-latex/)
* [Creating Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)
* [How to write an algorithm in Latex](https://shantoroy.com/latex/how-to-write-algorithm-in-latex/)
* [How to add subfigure in Latex](https://shantoroy.com/latex/how-to-add-subfig-in-latex/)
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


So, these are the top 20 common mistakes of new Latex users. Feel free to let me know if there is any other you have faced or thought of.

Thanks guys for reading! Cheers!!!

___

___

Thank you for reading my blog post! 🙏

If you enjoyed it and would like to stay updated on my latest content and plans for next week, be sure to subscribe to my newsletter on Substack. 👇

Once a week, I'll be sharing the latest weekly updates on my published articles, along with other news, content and resources. Enter your email below to subscribe and join the conversation for Free! ✍️

<iframe src="https://shantoroy.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

I am also writing on Medium. You can [follow me here](https://medium.com/@shantoroy).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzczODM4MTkzXX0=
-->