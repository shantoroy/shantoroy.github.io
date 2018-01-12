---
layout: single
categories: 
  - Latex
tags:
  - Latex
  - Tutorial
toc: true
toc_label: "Table of Contents"
toc_icon: "heart" 
---

## How to add sub-figures in latex
To add sub-figures in a latex file you need to use the package `graphicx`. Then you can use both `subfigure` and `minipage` for inserting sub-figures or sub-images. Keep 

## Add sub-figures horizontally
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

So, applying the code the output should look like this-

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/142248809@N07/38744621035/in/dateposted-public/" title="subfigure"><img src="https://farm5.staticflickr.com/4651/38744621035_a725266755_b.jpg" width="1024" height="488" alt="subfigure"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>


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
## Add multiple subfigures in multiple rows

```latex
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
