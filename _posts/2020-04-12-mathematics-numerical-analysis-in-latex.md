---
layout: single
title: "Mathematics Documentation in Latex"
header:
  image: "https://live.staticflickr.com/65535/49814118206_a5cf091236_b.jpg"
  teaser: "https://live.staticflickr.com/65535/49814118206_a5cf091236_b.jpg"
categories:
  - Latex
tags:
  - Latex
  - Resources
  - Documentation
  - Mathematics
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Writing mathematics in Latex seems to be a bit difficult at first. However, here I compiled a short summary on how you can write good mathematical expressions easily with examples.

I am assuming, you already know some basics how to write basic equations. Here, I show you how you can present and document it in well manner.

If you are new to Latex, this post might be helpful for you. Check [Latex Resources in a Nutshell](https://shantoroy.com/latex/latex-resources-in-a-nutshell/).

## Environments
### Within Paragraph/Texts
1. Use **`$$`** for mathematical expressions inside text. For example, `$x^2 + y^2 = z^2$` will look like $x^2 + y^2 = z^2$. 

2. You can also use `parenthesis` for equations inside text. For example, `\(x^2  + y^2  = z^2\)` will look like $x^2 + y^2 = z^2$ in the output document.


### Outside Paragraph/Texts
1. Use `\begin{equation}...\end{equation}` to write equations. Put your mathematical symbols within this environment and it will add an equation number as well.
```
% With equation number
\begin{equation}
	x^2 + y^2 = z^2 
\end{equation}
```
To avoid equation number, use `\begin{equation*}...\end{equation*}`
```
% Without equation number
\begin{equation}
	x^2 + y^2 = z^2 
\end{equation}
```
2. Aligning equations is one of my favorite option and it can be done using `\begin{align*}...\end{align*}`. We actually use it to align several equations.
```
\usepackage{amsmath}
\begin{align*}
	x^2 + y^2 &= z^2 \\
	x^3 + y^3 &= z^3
\end{align*}
```
Here, `&` helps to keep the equations aligned. Use `\\` for newline.
Or, you can use `\begin{multline*}...\end{multline*}`.
```
\begin{multline*}
f(x) = (a^2 + b^2 + c^2 + d^2 + e^2 + f^2)\\ 
-(g^2 + h^2 + i^2 + j^2)
\end{multline*}
```

3. You can also simply use `\[...\]` and put mathematical expressions within this.
```
\[
	x^2 + y^2 = z^2
\]
```


## Mathematics Symbols in Latex
You can find all necessary Latex commands in the following link-

[http://cs.brown.edu/about/system/managed/latex/doc/symbols.pdf](http://cs.brown.edu/about/system/managed/latex/doc/symbols.pdf)

As this is a public document, I embed here for your convenience.

<iframe src="https://drive.google.com/file/d/1mZ9nyAn1PN1vd4Ls7--0-ox8ns-FNwin/preview" width="100%" height="100%"></iframe>


## Example Equations
Please check this [Overleaf Document](https://www.overleaf.com/read/kyqrmhfcnrwx) to find real different examples related to general equations, matrix, and calculus.



## Related Resources

1. [UnicodeMath: A Nearly Plain-Text Encoding of Mathematics](http://www.unicode.org/notes/tn28/UTN28-PlainTextMath-v3.1.pdf)
2. [LaTeX Math in MicroSoft Office](https://docs.microsoft.com/en-us/archive/blogs/murrays/latex-math-in-office)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NTM1NjA5MjRdfQ==
-->