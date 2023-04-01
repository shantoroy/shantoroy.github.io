---
layout: single
title: "How to add subfigure in Latex: : Step-by-Step Tutorial with Examples"
redirect_from:
  - /latex/add-subfig-in-latex/
  - /latex/how-to-add-subfig-in-latex/
excerpt:  "Subfigures in LaTeX are a great way to add multiple images to a document while maintaining proper placement and referencing. However, they can be a bit tricky to implement. In this tutorial, I will show you how to add subfigures in LaTeX using the subcaption package, and provide examples to help you get started."
seo_title:  "How to Add Subfigure in Latex: Step-by-Step Tutorial with Examples"
seo_description:  "Want to add multiple images in your LaTeX document without causing any formatting issues? Learn how to add subfigure in Latex using the subcaption package. Our step-by-step tutorial with examples will guide you through the process."
header: 
  image: "https://farm5.staticflickr.com/4618/39005424665_7933a838e6_b.jpg"
  teaser: "https://farm5.staticflickr.com/4618/39005424665_7933a838e6_b.jpg"
categories: 
  - Latex
tags:
  - Latex
  - Tutorial
  - subfigure
  - minipage
toc: true
toc_label: "Table of Contents"
toc_icon: "heart" 
---

In research articles, we need to add subfigures often. To create subfigure in latex, you can use both `\begin{minipage}...\end{minipage}` and `\begin{subfigure}...\end{subfigure}` block to insert subfigures or sub-images. Subfigurs are generally inserted horizontally in one or multiple rows. Here, some example codes with output screenshots are provided in the following.

## Add subfigures horizontally
The following code puts two subfigures in a figure portion-

```latex
\usepackage{subcaption}
\begin{figure}[ht]
\begin{subfigure}{.5\textwidth}
  \centering
  % include first image
  \includegraphics[width=.8\linewidth]{image_file_name}  
  \caption{Put your sub-caption here}
  \label{fig:sub-first}
\end{subfigure}
\begin{subfigure}{.5\textwidth}
  \centering
  % include second image
  \includegraphics[width=.8\linewidth]{image_file_name}  
  \caption{Put your sub-caption here}
  \label{fig:sub-second}
\end{subfigure}
\caption{Put your caption here}
\label{fig:fig}
\end{figure}
```

So, applying the code the output should look like this -

<figure>
	<a href="https://farm5.staticflickr.com/4651/38744621035_a725266755_b.jpg"><img src="https://farm5.staticflickr.com/4651/38744621035_a725266755_b.jpg"></a>
</figure>

Here is another code to do the same. Only difference is, this time we are using `\begin{minipage}...\end{minipage}` instead of `\begin{subfigure}...\end{subfigure}` block.

```latex
\begin{figure}[ht]
  \subfloat[Percentage storage utilization]{
	\begin{minipage}[c][1\width]{
	   0.3\textwidth}
	   \centering
	   \includegraphics[width=1\textwidth]{image_file_name}
	\end{minipage}}
 \hfill 	
  \subfloat[standard deviation]{
	\begin{minipage}[c][1\width]{
	   0.3\textwidth}
	   \centering
	   \includegraphics[width=1.1\textwidth]{image_file_name}
	\end{minipage}}
 \hfill	
  \subfloat[execution time]{
	\begin{minipage}[c][1\width]{
	   0.3\textwidth}
	   \centering
	   \includegraphics[width=1.2\textwidth]{image_file_name}
	\end{minipage}}
\caption{}
\end{figure}
```

So, applying the code the output should look like this-

<figure>
	<a href="https://farm5.staticflickr.com/4658/39612703392_1bf583c3ed_b.jpg"><img src="https://farm5.staticflickr.com/4658/39612703392_1bf583c3ed_b.jpg"></a>
</figure>

## Add multiple subfigures in multiple rows

Multiple subfigures can be put in multiple rows by adding a `\newline` after one row is complete. For example, if you have four figures and you want to put them in 2x2 style, put `\newline` after two subfigures which will be placed in the first rwo. The command will create a new row for rest of the subfigures. 

```latex
\usepackage{caption}
\usepackage{subcaption}
\begin{document}
\begin{figure}
\begin{subfigure}{.5\textwidth}
  \centering
  % include first image
  \includegraphics[width=.8\linewidth]{log_demo1.png}  
  \caption{Put your sub-caption here}
  \label{fig:sub-first}
\end{subfigure}
\begin{subfigure}{.5\textwidth}
  \centering
  % include second image
  \includegraphics[width=.8\linewidth]{log_demo2.png}  
  \caption{Put your sub-caption here}
  \label{fig:sub-second}
\end{subfigure}

\newline

\begin{subfigure}{.5\textwidth}
  \centering
  % include third image
  \includegraphics[width=.8\linewidth]{log_demo1.png}  
  \caption{Put your sub-caption here}
  \label{fig:sub-third}
\end{subfigure}
\begin{subfigure}{.5\textwidth}
  \centering
  % include fourth image
  \includegraphics[width=.8\linewidth]{log_demo2.png}  
  \caption{Put your sub-caption here}
  \label{fig:sub-fourth}
\end{subfigure}
\caption{Put your caption here}
\label{fig:fig}
\end{figure}
```

So, applying the code the output should look like this-
<figure>
	<a href="https://farm5.staticflickr.com/4673/39642619871_bc6b328e85_b.jpg"><img src="https://farm5.staticflickr.com/4673/39642619871_bc6b328e85_b.jpg"></a>
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
* [How to write algorithm in Latex](https://shantoroy.com/latex/how-to-write-algorithm-in-latex/)
* [How to Write Matrix with Row/Column Labels in Latex](https://shantoroy.com/latex/matrix-labeling-in-latex/)
* [How to Collaboratively Write a Paper using Overleaf Latex Platform](https://shantoroy.com/latex/how-to-collaborately-write-a-paper-using-latex-overleaf/)
* [Itemize, Enumerate, and To-do-list in Latex](https://shantoroy.com/latex/playing-with-latex-itemize-enumerate-fontawesome/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ0OTQ0Nzg4NSwxNjQzMDA0OTIxXX0=
-->