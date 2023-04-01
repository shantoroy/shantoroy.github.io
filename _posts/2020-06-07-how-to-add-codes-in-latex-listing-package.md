---
layout: single
title: "How to add Codes in Latex: `listings` package for code documentation"
excerpt:  "If you're writing a document that requires code snippets, you'll need to use a package that supports code formatting in LaTeX. One such package is `listings`. This package is easy to use and provides a variety of options for formatting code. In this post, I'll walk you through the steps of adding code snippets to your LaTeX document using the `listings` package."
seo_title:  "How to Add Code Snippets to LaTeX using the `listings` Package"
seo_description:  Learn how to easily format and add code snippets to your LaTeX document using the `listings` package. Follow our step-by-step guide to use the package and make your code look professional and polished.
header:
  image: "https://live.staticflickr.com/65535/51214156890_330427f781_c.jpg"
  teaser: "https://live.staticflickr.com/65535/51214156890_330427f781_c.jpg"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Codes
  - Lstlisting
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Sometimes we need to include codes in our Latex documents. In this post we will see how to add codes with color formatting and line numbers.

## Requirements
We need to packages to work with code environments. `listing` is used to create styles and environments for adding codes in the document. `color` or `xcolor` is used to define custom colors only if you feel to use a custom one.
```latex
\usepackage{listings}
\usepackage{xcolor}
```

## Define Color
If you need to use custom defined colors, you can use `\definecolor` command followed by the custom color name and the `rgb` settings.
```latex
\definecolor{customgreen}{rgb}{0,0.6,0}
\definecolor{customgray}{rgb}{0.5,0.5,0.5}
\definecolor{custommauve}{rgb}{0.6,0,0.8}
```


## Supported Languages
Based on [LaTeX/Source Code Listings](https://en.wikibooks.org/wiki/LaTeX/Source_Code_Listings), the package supports the following languages.

```
ABAP2,4, ACSL, Ada4, Algol4, Ant, Assembler2,4,
Awk4, bash, Basic2,4, C#5, C++4, C4, Caml4, Clean,
Cobol4, Comal, csh, Delphi, Eiffel, Elan, erlang, 
Euphoria, Fortran4, GCL, Go (golang), Gnuplot, 
Haskell, HTML, IDL4, inform, Java4, JVMIS, ksh, 
Lisp4, Logo, Lua2, make4, Mathematica1,4, Matlab, 
Mercury, MetaPost, Miranda, Mizar, ML, Modelica3, 
Modula-2, MuPAD, NASTRAN, Oberon-2, Objective C5, 
OCL4, Octave, Oz, Pascal4, Perl, PHP, PL/I, Plasm, 
POV, Prolog, Promela, Python, R, Reduce, Rexx, RSL, 
Ruby, S4, SAS, Scilab, sh, SHELXL, Simula4, SQL, 
tcl4, TeX4, VBScript, Verilog, VHDL4, VRML4, XML, XSLT
```
## Code Styles 
Here, we will see two different ways to use styles and environments: one is common and can be used for any language, another is defining custom style and environment for different languages.

### Common Style
We can define common formatting for any language we want to include in our document.
```latex
\lstset{ 
  basicstyle=\small,        % the size of the fonts that are used for the code
  breaklines=true,                 % sets automatic line breaking
  commentstyle=\color{customgreen},    % comment style
  firstnumber=1,                % start line enumeration with line 1000
  frame=single,	                   % adds a frame around the code
  keepspaces=true,                 % keeps spaces in text, useful for keeping indentation of code (possibly needs columns=flexible)
  keywordstyle=\color{blue},       % keyword style
  numbers=left,                    % where to put the line-numbers; possible values are (none, left, right)
  numbersep=10pt,                   % how far the line-numbers are from the code
  numberstyle=\tiny\color{customgray}, % the style that is used for the line-numbers
  rulecolor=\color{black},         % if not set, the frame-color may be changed on line-breaks within not-black text (e.g. comments (green here))
  showspaces=false,                % show spaces everywhere adding particular underscores; it overrides 'showstringspaces'
  showstringspaces=false,          % underline spaces within strings only
  showtabs=false,                  % show tabs within strings adding particular underscores
  stepnumber=1,                    % the step between two line-numbers. If it's 1, each line will be numbered
  stringstyle=\color{custommauve},     % string literal style
  tabsize=2,	                   % sets default tabsize to 2 spaces
  title=\lstname                   % show the filename of files included with \lstinputlisting; also try caption instead of title
}
```

Now, include your code within the `\begin{lstlisting}...\end{lstlisting}` with defining the language you want to format with. For python, it will look like as follows:
```latex
\begin{lstlisting}[language=python]
class MyClass(Yourclass):
    def __init__(self, test):
        self.test = test
\end{lstlisting}
```

Or for a `C` program
```latex
\begin{lstlisting}[language=C]
#include <stdio.h>
int main() {
   // printf() displays the string
   printf("Hello, World!");
   return 0;
}
\end{lstlisting}
```

For adding an external file, we can use `\lstinputlisting` and define the language as well. For including an external `python` file, the code will look like as follows:

```latex
\lstinputlisting[language=python]{mypythonfile.py}
```

### Custom Style
We can define custom styles and environments as well for different languages. In that case, first we will have to define a new style, for example, for `python` it might look like as follows
```latex
\DeclareFixedFont{\ttb}{T1}{txtt}{bx}{n}{9} % for bold
\DeclareFixedFont{\ttm}{T1}{txtt}{m}{n}{9}  % for normal

\newcommand\pystyle{\lstset{
language=Python,
basicstyle=\ttm,
morekeywords={self},          % Add more keywords here
commentstyle=\color{gray},
keywordstyle=\ttb\color{blue},
emphstyle=\ttb\color{red},    % Custom highlighting style
stringstyle=\color{green},
showstringspaces=false
}}
```

Then we have to define a new environment for `python` using a custom name (here we used `python`)
```latex
\lstnewenvironment{python}[1][]
{
\pystyle
\lstset{#1}
}
{}
```

This allows you to put your code inside
```latex
\begin{python}
	# your code goes here
\end{python}
```



This is how we can add custom environment for each and every language. However, this requires time to do that for every language. 

That's it for today! Cheers!!!




## References
* [LaTeX/Source Code Listings](https://en.wikibooks.org/wiki/LaTeX/Source_Code_Listings)
* [Code listing](https://www.overleaf.com/learn/latex/Code_listing)
* [How to highlight Python syntax in LaTeX Listings \lstinputlistings command](https://tex.stackexchange.com/questions/83882/how-to-highlight-python-syntax-in-latex-listings-lstinputlistings-command)


## Related Other Posts (Latex)

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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0OTI0Mzk5MSwxODAxNTc4ODE3LC0xNz
A5MjgzMTI3LC0xNTI5NDA0MTY3XX0=
-->