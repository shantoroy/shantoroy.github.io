---
layout: single
title: "How to Draw Equations with Parameter Description in Latex using Tikz"
header:
  image: "https://live.staticflickr.com/65535/52102560767_07df211900_o.png"
  teaser: "https://live.staticflickr.com/65535/52102560767_07df211900_o.png"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Overleaf
  - Tikz
  - Equation
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
---

I was looking for a code that has a visualization of equation parameter description like the following.
```
<figure>
  <a href="/assets/images/post_images/2021-11-17-draw-equation-with-parameter-description.png"><img src="/assets/images/post_images/2021-11-17-draw-equation-with-parameter-description.png"></a>
</figure>
<br/>
```
Then I found this [awesome collection of Tikz Examples](https://github.com/walmes/Tikz) and I just modified a little from their code.


First, we need the following packages:
```latex
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{xcolor}
```


Now, here's the code that produces this output. You can also check out the output in [this overleaf project](https://www.overleaf.com/read/kyqrmhfcnrwx). 

```latex
\def\hd{0.5}
\def\vd{0.5}
\newcommand{\tm}[1]{\tikz[overlay, anchor=base] \node[red] (#1) {};}
\tikzstyle{every picture}+=[remember picture]

\begin{tikzpicture}[
  >=stealth,
  every path/.style={->, color=green!70!white, thin, rounded corners},
  every node/.style={color=black},
  bx/.style={text width=3cm, font=\footnotesize, minimum height=4ex},
  bxl/.append style={bx, left, align=flush right},
  bxr/.append style={bx, right, align=flush left}]

  \node {
    $\tm{y}y =
    \tm{b0}\beta_0+
    \tm{b1}\beta_1
    \tm{x1}x_1+
    \tm{b2}\beta_2
    \tm{x2}x_2+\cdots+
    \tm{bk}\beta_k
    \tm{xk}x_k+
    \tm{er}\epsilon$
  };

  \node[bx, align=center] (preds) at (0.4,1.5)
  {Independent Variables};
  \node[bx, align=center] (tx) at (0.4,-1.5) {Coefficients};

  \path[draw] (y)+(0.5ex,2ex) to[out=90, in=0] +(-\vd,\hd)
  node[bxl] {Dependent variable};
  \path[draw] (x1)+(0.5ex,2ex) to[out=90, in=-90] (preds);
  \path[draw] (x2)+(0.5ex,2ex) to[out=90, in=-90] (preds);
  \path[draw] (xk)+(0.5ex,2ex) to[out=90, in=-90] (preds);
  \path[draw] (b1)+(1ex,-1ex) to[out=-90, in=90] (tx);
  \path[draw] (b2)+(1ex,-1ex) to[out=-90, in=90] (tx);
  \path[draw] (bk)+(1ex,-1ex) to[out=-90, in=90] (tx);
  \path[draw] (b0)+(1ex,-1ex) to[out=-90, in=0] +(-\vd,-\hd)
  node[bxl] {Intercept};
  \path[draw] (er)+(0.5ex,-1ex) to[out=-90, in=180] +(\vd,-\hd)
  node[bxr] {Random Error};

\end{tikzpicture}
```


You can also check out my other posts:
* [Mathematics Documentation in Latex](https://shantoroy.com/latex/mathematics-numerical-analysis-in-latex/)
* [Latex Resources in a Nutshell](https://shantoroy.com/latex/latex-resources-in-a-nutshell/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjMyODkzMjldfQ==
-->