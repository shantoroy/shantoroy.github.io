---
layout: single
title: "Introduction to Data Science: Matplotlib Module (Part 02)"
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/51221326129_1df153df24_c.jpg"
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
excerpt: "This post includes code snippets for drawing bar, pie, box, scatter plots, and histograms."
---

In the [previous post](https://shantoroy.com/python/intro-to-data-science-matplotlib-module/), we have learnt the basics of using the `matplotlib` module for data visualization. Also, we have only learnt how to draw a line plot. 

In this post, we will learn to draw other plots including bar plot, pie plot, scatter plot, box plot, and histogram.

## Bar Plot
Use `matplotlib.pyplot.bar()` to create bar plots. Find out more details in the [official documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html).
```python
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

# Defines the chart font style
font = {'family' : 'Times New Roman',
        'weight' : 'bold',
        'size'   : 18}

# includes the chart font style
plt.rc('font', **font)

# You can also define like this
# plt.rcParams["font.family"] = "Times New Roman"

# To define figure size
figure(num=None, figsize=(12, 6))

# Defines X-axis labels and Y-axis values
x_axis_labels = ['0', '1', '2', '3', '4', '5']
y_axis_values = [670, 520, 240, 135, 96, 567]

# Creating n-dimensional array with evenly spaced values
y_pos=np.arange(len(x_axis_labels))

# Input bar values
# Define the bar styles with width, color, and legend labels
plt.bar(y_pos + 0, y_axis_values, width=0.5, color = 'c', label='legend title')
# For Horizontal bars
# plt.barh(y_pos + 0, y_axis_values, color = 'c', label='legend title')

# Define X-axis labels
plt.xticks(y_pos, x_axis_labels)
# plt.xticks(y_pos, x_axis_labels, rotation='vertical')

# Defines best position of the legend in the figure
plt.legend(loc='best')

# Defines X and Y axis labels
plt.ylabel('This is Y-axis label')
plt.xlabel('This is X-axis label')

# Defines plot title
plt.title("This is the Graph Title")

# Show the plot
plt.show()

# To save the figure as pdf/png/jpg, use plt.savefig
# plt.savefig('Figure_name.pdf', dpi=300)
```
You can check more customized bar plots in my other post:

[Creating Bar Charts using Python Matplotlib](https://shantoroy.com/python/python-bar-chart-using-matplotlib/)

## Pie Plot
Use `matplotlib.pyplot.pie()` to create pie plots. Find out more details in the [official documentation](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.pie.html).
```python
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
labels = 'x', 'y', 'z', 'w'
sizes = [5, 10, 20, 30]
explode = (0, 0, 0, 0.1)  # is used to explode a slice

fig1, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=180)

plt.show()
```

## Scatter Plot
Use `matplotlib.pyplot.scatter()` to create scatter plots. Find out more details in the [official documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html).
```python
from matplotlib import pyplot as plt
import numpy as np

# gaussian data generation
mu_vec1 = np.array([0,0])
cov_mat1 = np.array([[2,0],[0,2]])

x1 = np.random.multivariate_normal(mu_vec1, cov_mat1, 100)
x2 = np.random.multivariate_normal(mu_vec1+0.2, cov_mat1+0.2, 100)
x3 = np.random.multivariate_normal(mu_vec1+0.4, cov_mat1+0.4, 100)

plt.figure(figsize=(8,6))
  
plt.scatter(x1[:,0], x1[:,1], marker='^', 
            color='blue', alpha=0.4, label='x1 data')
plt.scatter(x2[:,0], x1[:,1], marker='o', 
            color='green', alpha=0.4, label='x2 data')
plt.scatter(x3[:,0], x1[:,1], marker='x', 
            color='red', alpha=0.4, label='x3 data')
plt.ylabel('put your y-label')
plt.xlabel('put your x-label')
plt.legend(loc='best') # leave empty for best, default = `best`

plt.show()
```

## Box Plot
Use `matplotlib.pyplot.boxplot()` to create box plots. Find out more details in the [official documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html).
```python
all_data = [np.random.normal(0, std, 100) for std in range(1, 4)]

fig = plt.figure(figsize=(8,6))

plt.boxplot(all_data, 
            notch=False, # box instead of notch shape 
            sym='rs',    # red squares for outliers
            vert=True)   # False means horizontal

plt.xticks([y+1 for y in range(len(all_data))], ['x1', 'x2', 'x3'])
plt.xlabel('put your x-label')
plt.show()
```


## Histogram
You can plot `histogram` using the `matplotlib.pyplot.hist()` method. Find out more details in the [official documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html).
```python
import random

data1 = [random.gauss(15,10) for i in range(500)]  
data2 = [random.gauss(5,15) for i in range(500)]  
bins = np.arange(-40, 40, 1.5)
plt.xlim([min(data1+data2)-5, max(data1+data2)+5])

plt.hist(data1, bins=bins, alpha=0.2, label='class a')
plt.hist(data2, bins=bins, alpha=0.2, label='class b')
plt.title('Random Gaussian data for Example Histogram')
plt.xlabel('put your x-label')
plt.ylabel('put your y-label')
plt.legend()
plt.show()
```

That's it for now. In the later posts, I will include code snippets for stylish data visualization using `seaborn` and interactive visualization using `plotly` modules.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc2MDgyNjc2OCwyMTM2MzY1NDQyXX0=
-->