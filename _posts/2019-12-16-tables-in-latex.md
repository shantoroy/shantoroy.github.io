---
layout: single
title: "Preparing  Tables  for  Publication  and  Documentation  in  Latex"
header:
  image: "https://live.staticflickr.com/65535/49211373397_8de8c1daa4_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49211373397_8de8c1daa4_h.jpg"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Tables
  - Documentation
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

This post discusses the basic of `Latex tables` and usage in documentation. All the codes and outputs are available in the [Overleaf Document](https://www.overleaf.com/read/nybtcgkxdjhd).


## Basic Syntax
Let's look at a basic table syntax in latex. Then we will discuss the components of the code.
```latex
\begin{table}[h!]
\centering
\begin{tabular}{|c|c|c|c|} 
 \hline
 Col1 & Col2 & Col3 & Col4 \\
 \hline\hline
 1 & First & 111 & This is a test \\ 
 2 & Second & 222 & Another test \\
 3 & Third & 333 & this is too \\
 4 & Fourth & 444 & And it continues  \\
 5 & Fifth & 555 & To the end \\ [1ex] 
 \hline
\end{tabular}
\caption{Write your Caption Here}
\label{table:first_table}
\end{table}
```
Now, let's understand the code-
* A table starts with `\begin{table}` and ends with `\end{table}` containing one or multiple `tabular structure with rows and columns`, `caption`, and a `label`. 
* `[h!]` is float value; setting the table floating position to be just at the place of code. `[htb]` refers to `here`, `top`, and `bottom` with orderly preference. 
* In the tabular section we see four `c`; it is a column type and means four columns with putting the text in the center of the cell.  You can also use `l` for left-align or `r` for right-align format. The pipe symbol `|` denotes the side border of a cell. 
* `\hline` is used for generating a complete horizontal line for a table. `\cline{2-4}` can be used if horizontal line is required only from second to fourth cell.
* Column values are seperated by an `&`. If you are done with writing the values for a row, use `//` to start writing values for a new row.

## Latex Table Generator
[LatexTableGenerator](https://www.tablesgenerator.com/latex_tables) is a pretty good shortcut to generate code for Latex Tables. It almost feels like creating tables in `MS Word` or any other word processing tools. You can select a basic structure, add rows and columns, format texts, split and merge cells etc. and then click on `generate code` to have the code. All you need to do is copy and paste the code in your latex document.

##  Column types
We have already discussed about the `l/c/r` column type. Usually the cell width is defined by the length of the text. But that is inconvenient in terms of long paragraph. In that case, we can use `p{value in cm}` format; for example: `p{3cm}`, the cell width should be 3cm long. For better formatting, you can use custom column type, e.g.- 
```latex
\newcolumntype{M}[1]{>{\centering\arraybackslash}m{#1}}
```
Example table is provided in the overleaf document (Table 2).

## Multirow/ Multicolumn Formatting
Cell merging (row/column-wise) can be performed using the `multirow` package. Should be written as `\multirow{# of rows}{width}{text}` and `\multicolumn{# of columns}{col type}{text}` for merging cells row-wise and column-wise respectively.
```latex
\usepackage{multirow}
\multirow{2}{*}{text}
\multicolumn{2}{c}{text}
```
If required to use both together for a cell, use the following format.
```latex
\multicolumn{3}{c}{\multirow{2}{*}{text}}
```
Note that, if you have used custom `M` type column as I showed before, do not forget to add the total value of the each column width. Look at the following example:
```latex
\begin{tabular}{|M{4.1cm}|M{3cm}||M{5cm}|}
\hline
\multicolumn{2}{|M{7.1cm}|}{\textbf{Source-1}} & \textbf{Source-2} \\ \hline \hline
Data1 & Data2 & Data3 \\ \hline
\end{tabular}
```
As we are merging first two columns, we need to add the total value of cell-widths: `4.1+3 = 7.1 cm`.

## Adjusting the table
There is no default adjustment option for a latex table similar to latex figures. In case of figure, you can use `[width=\textwidth]` within the `includegraphics` command. For tables, `resizebox` and `adjustbox` can be used to adjust it with the default text column width of a document. Using `resizebox` is preferable.
```latex
\usepackage{graphics}
\resizebox{\columnwidth}{!}{
% \begin{tabular}...\end{tabular}
}
```
or use this:
```latex
\usepackage{adjustbox}
\begin{adjustbox}{width=\textwidth}
% \begin{tabular}...\end{tabular}
\end{adjustbox}
```

## Tables side by side
You can use any of the following to put small tables side by side.
```latex
\begin{table}[ht]
    \centering
    \begin{tabular}{|c|c|c|}
\hline
t1 & t2 & t3 \\\hline
d1 & d2 & d3 \\\hline
\end{tabular}
\quad
\begin{tabular}{|c|c|c|}
\hline
t1 & t2 & t3 \\\hline
d1 & d2 & d3 \\\hline
\end{tabular}
    \caption{Tables side by side}
    \label{tab:my_label}
\end{table}
```
or,
```latex
\usepackage{subfig} % note that it clashes with subcaption
\begin{table}[ht]
    \centering
    \subfloat[sub-caption 01]{
    \begin{tabular}{|c|c|c|}
    \hline
    t1 & t2 & t3 \\\hline
    d1 & d2 & d3 \\\hline
    \end{tabular}
    }
    \subfloat[sub-caption 02]{
    \begin{tabular}{|c|c|c|}
    \hline
    t1 & t2 & t3 \\\hline
    d1 & d2 & d3 \\\hline
    \end{tabular}
    }
    \caption{Tables side by side with sub-caption}
    \label{tab:my_label}
\end{table}
```
or,
```latex
\begin{table}[ht]
\parbox{.45\linewidth}{
\centering
\begin{tabular}{|c|c|c|}
    \hline
    t1 & t2 & t3 \\\hline
    d1 & d2 & d3 \\\hline
    \end{tabular}
\caption{Table 01}
}
\hfill
\parbox{.45\linewidth}{
\centering
\begin{tabular}{|c|c|c|}
    \hline
    t1 & t2 & t3 \\\hline
    d1 & d2 & d3 \\\hline
    \end{tabular}
\caption{Table 02}
}
\caption{Two different tables side by side}
\end{table}
```

For long tables, you can merge both tables and partition those with `hhline` package. In a recent paper work, I tried the abovementioned codes but did not succeed. Then I found it and to be honest, `hhline` is really awesome.

`\hhline{---||---}` is used instead of simple `\hline`. Here, the total number of cell in a row is 6 and the partition comes after 3 columns. Just remember, if you need to omit a horizontal line due to `multirow` cells, you need to use `~` instead of `-`. For example, `\hhline{~~-||---}` where first two columns have a multirow situation.

The following table code includes `multirow`, `multicolumn`, `resizebox`, and `hhline` all together:
```latex
\begin{table}[ht]
\caption{Multirow and Multicolumn together}
\label{tab:table 4}
%  resizebox is used just outside tabular
\resizebox{\columnwidth}{!}{
\begin{tabular}{|M{2.1cm}|M{1cm}||M{2cm}|M{1cm}|M{2cm}|M{1cm}|M{2cm}|M{1cm}|}
\hhline{--||------}
\multicolumn{2}{|M{3.1cm}||}{\multirow{2}{*}{\textbf{Source 1}}} & \multicolumn{6}{M{10.3cm}|}{\textbf{Source 2}} \\ \hhline{~~||------}\hhline{~~||------}
\multicolumn{2}{|M{3.1cm}||}{\textbf{}} &
\multicolumn{2}{M{3.5cm}|}{\textbf{Blockchain}} & \multicolumn{2}{M{3.3cm}|}{\textbf{SDN}} & \multicolumn{2}{M{3.5cm}|}{\textbf{Data Science}} \\ \hhline{--||------}
 \textbf{Key}  & \textbf{Value} & \textbf{Key}  & \textbf{Value} & \textbf{Key}& \textbf{Value} & \textbf{Key} & \textbf{Value} \\ \hhline{--||------}\hhline{--||------}
 
\textcolor{blue}{Test1} & 2121 & BC  & 1787  & SDN & 267 & DS &  567\\ \hhline{--||------}
Test2 & 1989 & Bitcoin & 857  & SW & 131  & Python & 438 \\ \hhline{--||------}
Test3 & 1600 & SC & 5013 & Ryu & 32 & R & 208 \\ \hhline{--||------}
\textcolor{blue}{Test4} & 1540 & MM & 21 & POX & 697 & Julia & 186 \\ \hhline{--||------}

\end{tabular}
}
\end{table}
```

Once again, all the codes are available in the [overleaf document](https://www.overleaf.com/read/nybtcgkxdjhd). 

Cheers!!! :smiley::sunglasses::v:
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcxNzg2NDYxNiwtMTc4MTI1MTAyOSwyMT
cxNDE3OTIsMTIxNjY5MTgyMiwtMTMwMDkxNTg3NywxMTcwODkw
OTgsLTYwNTIxMjk4OSw5ODE1MjcxMjQsMjUyOTI1OTYwLDUxMT
M3MDg3OSw0MDk3NDczNDEsLTU5ODYwMDkxMCwxNTY2MDczNzEw
XX0=
-->