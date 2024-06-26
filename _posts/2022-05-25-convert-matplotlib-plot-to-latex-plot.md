---
layout: single
title: "How to Convert Python Matplotlib Plots to Latex Plots (Easiest Way) for Academic Papers"
excerpt:  "Learn how to easily convert your Python Matplotlib plots to LaTeX format using just a few lines of code. Latex plots are better in academic writings for conferences and journals. Save time and effort in creating publication-quality plots for your research papers."
seo_title:  "Convert Python Matplotlib Plots to LaTeX Format - Easy Tutorial using tikzplotlib module for academic writing"
seo_description:  "Easily convert Python Matplotlib plots to LaTeX format with just a few lines of code. Create publication-quality plots for your research papers in conferences and journals with minimal effort. Follow our tutorial for step-by-step instructions. It is just a few lines of codes. Here we use the module tikzplotlib to do the job."
header:
  image: "https://live.staticflickr.com/65535/52104303039_044542e267_o.png"
  teaser: "https://live.staticflickr.com/65535/52104303039_044542e267_o.png"
categories:
  - Latex
tags:
  - Latex
  - Tutorial
  - Overleaf
  - Tikz
  - matplotlib
  - pgfplot
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

I used to draw plots using matplotlib a lot and then add the figures in reports. Later I switched to latex plots as it is easier and works best for numerous reasons! 

Read my other post to learn the benifits of using latex plots in reports:
[Why you should use Latex Plots in your Reports instead of Matplotlib Plots](https://shantoroy.com/latex/why-you-should-use-latex-plots-instead-of-matplotlib-plots/)

Recently, I found a module that converts `python matplotlib` plots to `latex` plots. I was literally fascinated by this since sometimes I have to struggle creating similar results using latex pgfplots and most of all it requires some times to do that.

In this post I will provide some examples on how to do that.



## Install `tikzplotlib`
Let's first install the following python module names [tikzplotlib](https://github.com/texworld/tikzplotlib)

```bash
$ pip install tikzplotlib
```

## Using `tikzplotlib`
Write the following code piece after your matplotlib code

```python
# your matplotlib code
# remove or comment `plt.show()`

import tikzplotlib
tikzplotlib.save("test.tex")
# or
tikzplotlib.save("test.tex", flavor="context")
# tikzplotlib.get_tikz_code()
```

It will store the latex code in `test.tex` file that resides in the same directory.

However, you may find an empty code in the `tex` file if you don't remove the `plt.show()` line from your python code. Initially, I was trying that with this line and it didn't work.

You can use `tikzplotlib.get_tikz_code()` if you want the code as string.


## Example
As an example, I was able to convert the following python code
```python
import numpy as np
import matplotlib.pyplot as plt

A = np.arange(1, 11)
B = np.random.randn(10) # 10 rand. values from a std. norm. distr.
C = B.cumsum()

fig, (ax0, ax1) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(10,5))

## A) via plt.step()

ax0.step(A, C, label='cumulative sum') # cumulative sum via numpy.cumsum()
ax0.scatter(A, B, label='actual values')
ax0.set_ylabel('Y value')
ax0.legend(loc='upper right')


## B) via plt.plot()

ax1.plot(A, C, label='cumulative sum') # cumulative sum via numpy.cumsum()
ax1.scatter(A, B, label='actual values')
ax1.legend(loc='upper right')

fig.text(0.5, 0.04, 'sample number', ha='center', va='center')
fig.text(0.5, 0.95, 'Cumulative sum of 10 samples from a random normal distribution', ha='center', va='center')

# plt.show()

import tikzplotlib
tikzplotlib.save("mytikz.tex")
```

to this:

```latex
\begin{tikzpicture}

\definecolor{color0}{rgb}{0.12156862745098,0.466666666666667,0.705882352941177}

\begin{groupplot}[group style={group size=2 by 1}]
\nextgroupplot[
legend cell align={left},
legend style={fill opacity=0.8, draw opacity=1, text opacity=1, draw=white!80!black},
tick align=outside,
tick pos=both,
x grid style={white!69.0196078431373!black},
xmin=0.417841810613945, xmax=10.5821581893861,
xtick style={color=black},
y grid style={white!69.0196078431373!black},
ylabel={Y value},
ymin=-1.30024730980492, ymax=1.49472414429111,
ytick style={color=black}
]
\addplot [draw=color0, fill=color0, mark=*, only marks]
table{
x  y
1 -0.170017665288662
2 -0.0464802941273717
3 0.586557002451665
4 0.255262853207627
5 -0.545461307198665
6 -1.01133555864772
7 -0.241728183197433
8 0.782843124656819
9 0.799589432056481
10 0.958450583374001
};
\addlegendentry{actual values}
\addplot [semithick, color0, const plot mark right]
table {
1 -0.170017665288662
2 -0.216497959416034
3 0.370059043035632
4 0.625321896243259
5 0.0798605890445936
6 -0.931474969603124
7 -1.17320315280056
8 -0.390360028143738
9 0.409229403912743
10 1.36767998728674
};
\addlegendentry{cumulative sum}

\nextgroupplot[
legend cell align={left},
legend style={fill opacity=0.8, draw opacity=1, text opacity=1, draw=white!80!black},
scaled y ticks=manual:{}{\pgfmathparse{#1}},
tick align=outside,
tick pos=both,
x grid style={white!69.0196078431373!black},
xmin=0.417841810613945, xmax=10.5821581893861,
xtick style={color=black},
y grid style={white!69.0196078431373!black},
ymin=-1.30024730980492, ymax=1.49472414429111,
ytick style={color=black},
yticklabels={}
]
\addplot [draw=color0, fill=color0, mark=*, only marks]
table{
x  y
1 -0.170017665288662
2 -0.0464802941273717
3 0.586557002451665
4 0.255262853207627
5 -0.545461307198665
6 -1.01133555864772
7 -0.241728183197433
8 0.782843124656819
9 0.799589432056481
10 0.958450583374001
};
\addlegendentry{actual values}
\addplot [semithick, color0]
table {
1 -0.170017665288662
2 -0.216497959416034
3 0.370059043035632
4 0.625321896243259
5 0.0798605890445936
6 -0.931474969603124
7 -1.17320315280056
8 -0.390360028143738
9 0.409229403912743
10 1.36767998728674
};
\addlegendentry{cumulative sum}
\end{groupplot}

\draw ({$(current bounding box.south west)!0.5!(current bounding box.south east)$}|-{$(current bounding box.south west)!0.04!(current bounding box.north west)$}) node[
  scale=0.5,
  text=black,
  rotate=0.0
]{sample number};
\draw ({$(current bounding box.south west)!0.5!(current bounding box.south east)$}|-{$(current bounding box.south west)!0.95!(current bounding box.north west)$}) node[
  scale=0.5,
  text=black,
  rotate=0.0
]{Cumulative sum of 10 samples from a random normal distribution};
\end{tikzpicture}
```

All you need to do is, put the latex code within `figure` environment for better positioning, captioning, and labeling.

```latex
\begin{figure}[!ht]
    \centering
    
    \caption{Matplotlib to Tikz}
    \label{fig:my_tikz}
\end{figure}
```

Check the output in [this overleaf project](https://www.overleaf.com/read/tpmkcgvsnhgg).

That's all for today!

<iframe src="https://giphy.com/embed/f9RzoxHizH72k15FKS" width="480" height="268"></iframe>


## Latex-related Posts
You can find a comprehensive list of Latex resources in the following post:

[Latex Resources in a Nutshell](https://shantoroy.com/latex/latex-resources-in-a-nutshell/)

If you are a new Latex user, check out this post:
[20 Most Common Mistakes Made by New Latex Users](https://shantoroy.com/latex/common-mistakes-made-by-new-latex-typesetting-users/)

You can find all `Latex` oriented posts of mine in: [https://shantoroy.com/categories/#latex](https://shantoroy.com/categories/#latex)


* [How to write an algorithm in Latex](https://shantoroy.com/latex/how-to-write-algorithm-in-latex/)
* [How to add subfigure in Latex](https://shantoroy.com/latex/how-to-add-subfig-in-latex/)
* [Add Copyright Notice and Conference Name in IEEE Conference Template](https://shantoroy.com/latex/add-copyright-conference-name/)
* [Preparing Tables for Publication and Documentation in Latex](https://shantoroy.com/latex/how-to-create-tables-in-latex/)
* [Creating Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)

* [How to Write Matrix with Row/Column Labels in Latex](https://shantoroy.com/latex/matrix-labeling-in-latex/)
* [How to Collaboratively Write a Paper using Overleaf Latex Platform](https://shantoroy.com/latex/how-to-collaborately-write-a-paper-using-latex-overleaf/)
* [Itemize, Enumerate, and To-do-list in Latex](https://shantoroy.com/latex/playing-with-latex-itemize-enumerate-fontawesome/)
* [Latex Table for Survey in IEEE two-column format](https://shantoroy.com/latex/latex-table-for-survey-ieee-template/)
* [Line Plotting using Latex PGFPlots](https://shantoroy.com/latex/how-to-draw-line-graph-using-pgfplots-latex/)
* [How to Create Bar Charts using Latex PGFPlots](https://shantoroy.com/latex/bar-plots-in-latex-pgfplot/)
* [How to add Codes in Latex:  `listings`  package for code documentation](https://shantoroy.com/latex/how-to-add-codes-in-latex-listing-package/)
* [Bibliography management with Bibtex in Latex](https://shantoroy.com/latex/bibliography-management-with-bibtex/)
* [Creating Multiple Line plots from CSV file using Latex Tikz and PGFPlot](https://shantoroy.com/latex/multiple-line-plots-using-tikz-pgfplot/)
* [How to Draw a Literature Survey Taxonomy Tree in Latex](https://shantoroy.com/latex/Draw-literature-survey-tree-in-latex/)
* [How to Convert Python Matplotlib Plots to Latex Plots (Easiest Way) for Academic Papers](https://shantoroy.com/latex/convert-matplotlib-plot-to-latex-plot/)
* [How to Draw Equations with Parameter Description in Latex using Tikz](https://shantoroy.com/latex/Draw-equations-with-parameter-description-in-latex/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTMzMDIyOTcsLTIxMTU2NzQ3MSwtMTU0Nj
A2OTYxOSwtNjI2NTg4OTA1LDM1NzQzNzAzMyw2MzQ3NzY0Niwy
NDA5ODg3NTQsMTkwMjgzNzcwMF19
-->