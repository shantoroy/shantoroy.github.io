---
layout: single
title: "How to Convert Python Matplotlib Plots to Latex Plots (Easiest Way)"
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
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
---

I used to draw plots using matplotlib a lot and then add the figures in reports. Later I switched to latex plots as it is easier and works best for numerous reasons! 

Read my other post to learn the benifits of using latex plots in reports:


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
table{%
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
table {%
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
table{%
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
table {%
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


<!--stackedit_data:
eyJoaXN0b3J5IjpbMjQwOTg4NzU0LDE5MDI4Mzc3MDBdfQ==
-->