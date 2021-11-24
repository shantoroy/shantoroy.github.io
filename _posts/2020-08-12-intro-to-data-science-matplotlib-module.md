---
layout: single
title: "Introduction to Data Science: Matplotlib Module"
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/51699752275_9f18c8cb49_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Numpy
  - Pandas
  - Matplotlib
  - Visualization
  - Data Science
  - Machine Learning
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post explains the basic syntax of matplotlib module for data visualization."
---


In this tutorial, we will see basic syntax of producing plots for data visualization using the `matplotlib` module. `matplotlib` and `seaborn` are widely used for basic data visualization. `seaborn` actually uses the underlying functionalities of the `matplotlib` module for more beautiful less code-oriented visualizations.

Let's first import the module like this
```python
import matplotlib.pyplot as plt
```

If you are using the `Jupyter Notebook`, also add the following:
```python
# Only for jupyter notebook
%matplotlib inline
```

## Plotting
### Basic Plotting
The simplest way of plotting $(x,y)$-values is to use `matplotlib.pyplot.plot(x,y)`. I have added the labels and titles here as well. 
```python
x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.plot(x, y, 'black')
plt.xlabel('Write your X-label')
plt.ylabel('Write your Y-label')
plt.title('Write your plot title')
plt.show()
```

### Basic Subplotting
The most basic subplotting can be visualized using the subplot allocation and numbering. $(1,2,1)$ means the subplot has allocation for one row (first value) and two columns (second value) (*that means two subplots possible*) where the last value defines the first column.
```python
x = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [1,8,27,64,125]

plt.subplot(1,2,1)
plt.plot(x, y1, 'r+-')
plt.subplot(1,2,2)
plt.plot(x, y2, 'g*-');
```
Similarly, if you want to have three subplots in one row:
```python
x = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [1,8,27,64,125]
y3 = [2,4,6,8,10]

plt.subplot(1,3,1)
plt.plot(x, y1, 'ro-')
plt.subplot(1,3,2)
plt.plot(x, y2, 'g*-')
plt.subplot(1,3,3)
plt.plot(x, y3, 'b+-');
```

## Plotting using `plt.figure()` class
### Basic Plotting
You can create a basic plot object by using the `matplotlib.pyplot.figure()` class.
```python
fig = plt.figure()

# define axes in this format:
# [x0, y0, width, height] (range 0 to 1)
axes = fig.add_axes([0, 0, 1, 1]) 

# Plot on that set of axes
axes.plot(x, y, 'ro-')
axes.set_xlabel('Set X-label')
axes.set_ylabel('Set y-label')
axes.set_title('Write your title');
```

### Inset Plotting
You can generate an inset plot by defining the axes value for the second plot.
```python
fig = plt.figure()

axes1 = fig.add_axes([0, 0, 1, 1]) # larger axes
axes2 = fig.add_axes([0.65, 0.25, 0.25, 0.2]) # inset axes


axes1.plot(x, y1, 'b*-')
axes1.set_xlabel('X label')
axes1.set_ylabel('Y label')
axes1.set_title('Axes 1 Title')

axes2.plot(x, y2, 'r+-')
axes2.set_xlabel('X label')
axes2.set_ylabel('Y label')
axes2.set_title('Axes 2 Title');
```

### Automatic Subplots
The `matplotlib.pyplot.subplots()` object can assign automatic subplots.
```python
# Automatic fig and axes
fig, axes = plt.subplots()

axes.plot(x, y, 'r')
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('title');
```
You can define the number of rows and columns under `nrows` and `ncols` parameters while creating objects.
```python
fig, axes = plt.subplots(nrows=1, ncols=3)
yList = [y1,y4,y5]
for roy,j in zip(axes,yList):
    roy.plot(x, j, 'b')
    roy.set_xlabel('X label')
    roy.set_ylabel('Y label')
    roy.set_title('title')
```


## Other Customizations
### Custom Figure Size
You can define custom figure size using the `figsize` parameter. The length and height values are defined inside a tuple.
```python
fig, axes = plt.subplots(figsize=(15,5))

axes.plot(x, y, 'g')
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('title')

plt.show()
```

### Save a Figure
Save a figure using the `<fig_obj>.savefig()` method
```python
fig.savefig("thisistest.png", dpi=300)
```

### Multiple Plots in one figure
In the following example, multiple plots has been be drawn using `<axes_obj>.plot()` method multiple times.
```python
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x, y1)
axes.plot(x, y2)
plt.show()
```

### Title
Use `<axes_obj>.set_title()` method to set the title of the plot
```python
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x, y1)
axes.plot(x, y2)

ax.set_title("write your title")
plt.show()
```

### Legends
The legend is defined by providing a name to the `label` option.
```python
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x, y1, label="sin(x)")
axes.plot(x, y2, label="cos(x)")
axes.legend()
plt.show()
```

Legend locations can be set like this
```python
ax.legend(loc=0) # optimal location
ax.legend(loc=1) # upper right corner
ax.legend(loc=2) # upper left corner
ax.legend(loc=3) # lower left corner
ax.legend(loc=4) # lower right corner
```

More customization is possible using the `bbox_to_anchor` option. For example, to put the legend-box outside right top, you can use the following code:
```python
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
```

### Axis Labels
Use `<axes_obj>.set_xlabel()` and `<axes_obj>.set_ylabel()` to set axis labels in $x$ and $y$ directions, respectively.
```python
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

axes.plot(x, y1)
axes.plot(x, y2)
axes.set_xlabel("x")
axes.set_ylabel("y")
plt.show()
```

### Colors

```python
fig, ax = plt.subplots()
axes.plot(x, y1, 'b.-') # blue dotted line
axes.plot(x, y2, 'g--') # green dashed line
```

Also, `color` parameter is available to set custom color hex codes

```python
axes.plot(x, y1, color="#7a7a7a")
axes.plot(x, y2, color="#FFC98A") 
```

### Line Width
Line width can be set using the `lw` parameter.
```python
fig, ax = plt.subplots()
axes.plot(x, y1, lw=3,'b.-')
axes.plot(x, y2, lw=3,'g--')
```

### Line Style
Use `ls` parameter to define a custom line style

```python
fig, ax = plt.subplots()
axes.plot(x, y1,ls='-')
axes.plot(x, y2,ls='--')
```

### Custom Marker
Use custom marker using the `marker` parameter.
```python
fig, ax = plt.subplots()
axes.plot(x, y1, color="blue", lw=3, ls='-', marker='+')
axes.plot(x, y2, color="blue", lw=3, ls='--', marker='o')
```

### Scaling
Use logarithmic scales for large difference values

```python
fig, axes = plt.subplots(1, 2, figsize=(10,4))
      
axes[0].plot(x, x**3, x, np.exp(x))
axes[0].set_title("Normal scale")

axes[1].plot(x, x**2, x, np.exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)");
```

In this post, I tried to cover basic plotting using the `matplotlib` module. So far, we have learnt how to draw line charts. In the next tutorial, we will learn other plots, for example, bar plots, pie plots, scatter plots, and others.

Thanks for your patience. Have a good day!
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzOTIzNTQzNjYsLTEyNzY5MzIwMjEsLT
EzNDI1MjIxNzcsMjU4OTU0NTY1XX0=
-->