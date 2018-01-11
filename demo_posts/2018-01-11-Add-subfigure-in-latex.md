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
To add sub-figures in a latex file you need to use the package `graphicx`. Then you can use both `subfigure` and `minipage` for inserting sub-figures or sub-images. 

## Add sub-figures horizontally
```
\usepackage{subcaption}
\begin{figure}
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{image1}
  \caption{1a}
  \label{fig:sfig1}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{image2}
  \caption{1b}
  \label{fig:sfig2}
\end{subfigure}
\caption{plots of....}
\label{fig:fig}
\end{figure}
```

```latex
\begin{figure}
  \subfloat[Percentage storage utilization]{%
	\begin{minipage}[c][1\width]{%
	   0.3\textwidth}
	   \centering%	
	   \includegraphics[width=1\textwidth]{F1}
	\end{minipage}}
 \hfill 	
  \subfloat[standard deviation]{%
	\begin{minipage}[c][1\width]{%
	   0.3\textwidth}
	   \centering%
	   \includegraphics[width=1.1\textwidth]{F2}
	\end{minipage}}
 \hfill	
  \subfloat[execution time]{%
	\begin{minipage}[c][1\width]{%
	   0.3\textwidth}
	   \centering%
	   \includegraphics[width=1.2\textwidth]{F3}
	\end{minipage}}
\caption{}
\end{figure}
```
## Add subfigures vertically
