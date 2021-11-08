---
layout: single
title: "How to Write Matrix with Row/Column Labels in Latex"
header:
  image: "https://live.staticflickr.com/65535/51663858257_8c17ded63f_b.jpg"
  teaser: "https://live.staticflickr.com/65535/51663858257_8c17ded63f_b.jpg"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - matrix
  - math equations
  - Overleaf
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Sometimes, we have to create matrix while writing a math document in Latex. Here, I list a number of ways you can create matrices and also labeling the rows and columns if needed.

You can check the outputs in this [Overleaf Document](https://www.overleaf.com/read/hygqjqwcnfxb).

First, we need to include the following packages.
```latex
\usepackage{amsmath,blkarray,booktabs, bigstrut}
```

Now, let's take a look at the codes for matrices.
1. This is a simple matrix without any border
	```latex
	\[
	\begin{matrix}
	1 & 2 & 3 \\
	4 & 5 & 6 \\
	7 & 8 & 9 \\
	\end{matrix}
	\]
	```

2. This code creates a bordered matrix with brackets
	```latex
	\[
	\begin{bmatrix}
	1 & 2 & 3 \\
	4 & 5 & 6 \\
	7 & 8 & 9 \\
	\end{bmatrix}
	\]
	```
3. A simple equation where we generate the dot product of two matrices
	```latex
	\[ 
	\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} 
	\cdot 
	\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} 
	= 
	\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} 
	\]
	```
4. A bordered matrix with row and column labels
	```latex
	\[
	  \mathbf{\alpha} = 
	    \bordermatrix{ & \bar{f_1} & \bar{f_2} & \bar{f_3} \cr
	      k_1 & 0 & 0 & 1 \cr
	      k_2 & 1 & 0 & 0 \cr
	      k_3 & 0 & 0 & 1 \cr
	      k_4 & 0 & 1 & 0 } \qquad
	\]
	```
5. Another way to create a bordered matrix with row and column labels. I find this more helpful and easier than the other one. If you understand the code of writing a latex table, then this one is pretty simple. Use `\begin{block}{c(ccc)} ... \end{block}` to create the matrix, and then put the labels outside it using `\begin{blockarray}{cccc} ... \end{blockarray}`. Remember, the number of total column number `c` must be equal. 

	```latex
	\[
	  \mathbf{\beta} = 
	    \begin{blockarray}{cccc}
	        & \bar{f_1} & \bar{f_2} & \bar{f_3} \\
	      \begin{block}{c(ccc)}
	        f_1 & 3 & 2 & 0 \\
	        f_2 & 2 & 4 & 2 \\
	        f_3 & 5 & 3 & 1 \\
	      \end{block}
	    \end{blockarray}
	\]
	```

	Using `(ccc)` creates `()` shaped matrix while using `[ccc]` creates `[]` shaped matrix.
	```latex
	\[
	\begin{blockarray}{ccccc}
	 & C_1 & C_2 & \dots & C_n \\
	\begin{block}{c[cccc]}
	N_1 & a_{11} &a_{12} &\cdots & a_{1n}\bigstrut[t] \\
	N_2 & a_{21}&a_{22}&\cdots &a_{2n} \\
	 & \vdots & \vdots & \ddots & \vdots\\
	N_n & a_{n1}&a_{n2}&\cdots &a_{nn}\bigstrut[b]\\
	\end{block}
	\end{blockarray}\vspace*{-1.25\baselineskip}
	\]
	```

	NoLet's take a look at the all side labeling matrix
	```latex
	\[
	\gamma  = 
	\begin{blockarray}{cccccc}
	 & \bar{f_1} & \bar{f_2} & \dots & \bar{f_n} \\
	\begin{block}{c[cccc]c}
	k_1 & 0 & 1 &\cdots & 0\bigstrut[t] & =1 \\
	k_2 & 1 & 0 &\cdots & 0 & =1 \\
	 & \vdots & \vdots & \ddots & \vdots &\\
	k_n & 0 & 0 &\cdots & 1\bigstrut[b] & =1\\
	\end{block}
	 & \leq 4 & \leq 5 & \dots & \leq 10 \\
	\end{blockarray}\vspace*{-1.25\baselineskip}
	\]
	```

6. The following example follows the same way. The example is taken from this [stackexchange thread](https://tex.stackexchange.com/questions/388138/labels-and-captions-of-a-matrix).
	```latex
	\newcommand{\cX}{\mathcal{X}}
	\newcommand{\fixhd}[1]{%
	  \smash[#1]{\vphantom{\Big|}}%
	}
	```

	```latex
	\[
	\begin{blockarray}{c ccccc c ccccc}
	& S_1 & \cdots & S_j & \cdots & S_N & & S_1 & \cdots & S_i & \cdots & S_N \\
	\cmidrule{2-6} \cmidrule{8-12}
	\begin{block}{c [ccccc] c [ccccc]}
	T_1 & \fixhd{b} x_1 & \cdots & 0 & \cdots & 0 & T_{N+1} & 0 & \cdots & \cX_i^1 & \cdots & \cX_N^1 \\
	\vdots & \vdots & \ddots & \vdots & \cdots & \vdots &
	\vdots & \vdots & \ddots & \vdots & \cdots & \vdots \\
	T_j & 0 & \cdots & x_j & \cdots & 0 & T_{N+i} & \cX_1^i & \cdots & 0 & \cdots & \cX_N^i \\
	\vdots & \vdots & \ddots & \vdots & \cdots & \vdots &
	\vdots & \vdots & \ddots & \vdots & \cdots & \vdots \\
	T_N & 0 & \cdots & 0 & \cdots & x_N & T_{2N} & \cX_1^N & \cdots & \cX_i^N & \cdots & 0 \fixhd{t} \\
	\end{block}
	\noalign{\vspace{-1.5ex}}
	& \BAmulticolumn{5}{c}{%
	    \underbrace{\hphantom{\begin{bmatrix}x_1&\cdots&x_j&\cdots&x_N\end{bmatrix}}}%
	    _{\text{Broadcasting phase}}%
	  }
	&& \BAmulticolumn{5}{c}{%
	    \underbrace{\hphantom{\begin{bmatrix}\cX^N&\cdots&\cX^N&\cdots&\cX^N\end{bmatrix}}}%
	    _{\text{Cooperation phase}}%
	  }
	\\
	\end{blockarray}
	\]
	```
7. If you want to label the whole row or column, the following example is for you. This is a simple `bmatrix` with `\underbrace{\begin{bmatrix} ... \end{bmatrix} }_{\displaystyle your-label}` for columns and `\left.\vphantom{ \begin{bmatrix} ... \end{bmatrix} }\right\} your-label` for labeling rows on the right side.
	```latex
	\[
	\underbrace{
	\begin{bmatrix}
	1/2 & 1/2 & 0 & 0 & \cdots & 0\\
	0 & 1/2 & 1/2 & 0 & \cdots & 0\\
	0 & 0 & 1/2 & 1/2 & \cdots & 0\\
	\vdots & \vdots & \vdots & \ddots & \vdots & \vdots\\
	1/2 & 0 & 0 & 0 & \cdots & 1/2\\
	\end{bmatrix}}_{\displaystyle n}
	\left.\vphantom{\begin{bmatrix}
	1/2 & 1/2 & 0 & 0 & \cdots & 0\\
	0 & 1/2 & 1/2 & 0 & \cdots & 0\\
	0 & 0 & 1/2 & 1/2 & \cdots & 0\\
	\vdots & \vdots & \vdots & \ddots & \vdots & \vdots\\
	1/2 & 0 & 0 & 0 & \cdots & 1/2\\
	\end{bmatrix}}\right\}m
	\]
	```

Once again, you can check the outputs in this [Overleaf Document](https://www.overleaf.com/read/hygqjqwcnfxb).



## References
1. [Labels and captions of a matrix](https://tex.stackexchange.com/questions/388138/labels-and-captions-of-a-matrix)
2. [Labeling the Dimensions of a Matrix](https://tex.stackexchange.com/questions/416635/labeling-the-dimensions-of-a-matrix)
3. [Matrix with column and row headings [duplicate]](https://tex.stackexchange.com/questions/423621/matrix-with-column-and-row-headings)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMjE4OTQwOTksODYzNzA4NDExXX0=
-->