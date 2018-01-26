---
layout: single
title: "How to add subfigure in Latex"
header: 
  image: "https://farm5.staticflickr.com/4618/39005424665_7933a838e6_b.jpg"
  teaser: "https://farm5.staticflickr.com/4618/39005424665_7933a838e6_b.jpg"
categories: 
  - Latex
tags:
  - Latex
  - Tutorial
toc: true
toc_label: "Table of Contents"
toc_icon: "heart" 
---

## How to add subfigures in latex
In research articles, we need to add subfigures often. To create subfigure in latex, you can use both `\begin{minipage}...\end{minipage}` and `\begin{subfigure}...\end{subfigure}` block to insert subfigures or sub-images. Subfigurs are generally inserted horizontally in one or multiple rows. Here, some example codes with output screenshot is provided in the following.

## Add subfigures horizontally
The following code puts two subfigures in a figure portion-

```
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
