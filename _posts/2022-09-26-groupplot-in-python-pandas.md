---
layout: single
title: "How to Plot Group-plots in Python"
excerpt:  "Learn how to create beautiful group-plots in Python with this step-by-step guide. With examples using Matplotlib and Pandas, you can master the art of visualizing complex data sets from dataframes in no time."
seo_title:  "How to Plot Group-Plots in Python: A Step-by-Step Guide"
seo_description:  "Discover how to create suitable group-plots in Python using Matplotlib and Pandas. Follow the tutorial and learn how to visualize complex data sets with ease. Here, the example includes visualizing CPU usage data based on PIDs."
header:
  image: "https://live.staticflickr.com/65535/52479338640_f66fd4ee41_o.png"
  teaser: "https://live.staticflickr.com/65535/52479338640_f66fd4ee41_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - groupplot
  - Pandas
  - Numpy
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
---

In this post, I will show how to create groupplots in Python. For that, we need to use Numpy, Pandas, and Matplotlib modules.

## Initials
Let's first import necessary modules and read the target file. Here, I was using a log file that has CPU usage over time.
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv("syrupy_20220616132420.ps.log",delimiter=r"\s*")
df.columns
```

## Creating Group
Now, let's create group for a certain column. Here, I have used the **PID** column for grouping. I had a lot of records for each PID and thus the group ensures the plot to have different line for each PID.
```python
fig, ax = plt.subplots(figsize=(8,6))
df.groupby('PID').plot(x='TIME', y='CPU', ax=ax, label=PID)
```

## Different Scales
It's not necessary unless you need two different scales for different PIDs. I had a few PIDs having values ranging around 90s and a few other ranging around 5. 

Since, the lines in the plot look almost straight parallel lines, I had to use different scales to make the slightest changes visible.
```python
df1 = df.loc[df['PID'].isin(['15503','15505','15509'])]
df2 = df.loc[df['PID'].isin(['14399','15507','15510','15512'])]
```


## Add legends
The following code is adapted to my need and was found in this [Stackoverflow thread](https://stackoverflow.com/questions/39902522/pandas-groupby-object-in-legend-on-plot).
```python
# https://stackoverflow.com/questions/39902522/pandas-groupby-object-in-legend-on-plot

fig, ax = plt.subplots(figsize=(8,6))
# df.groupby('PID').plot(x='TIME', y='CPU', ax=ax, label=PID)

for name, group in df1.groupby('PID'):
    group.plot(x='TIME', y='CPU', ax=ax, label=name)
    
for name, group in df2.groupby('PID'):
    group.plot(x='TIME', y='CPU', secondary_y=True, ax=ax, label=name)
```

Now, only one label is shown from the right axis.
I found solution in another [Stackoverflow thread](https://stackoverflow.com/questions/60448943/secondary-y-in-pandas-histogram-plot-legend-is-gone-missing)

Therefore, I needed to add this snippet
```python
# source: https://stackoverflow.com/questions/60448943/secondary-y-in-pandas-histogram-plot-legend-is-gone-missing
handles,labels = [],[]
for ax in fig.axes:
    for h,l in zip(*ax.get_legend_handles_labels()):
        handles.append(h)
        labels.append(l)
```
 and  I had to hide `pandas plot legend`.

So, now, the entire code now looks like

```python
fig, ax = plt.subplots(figsize=(8,6))
# df.groupby('PID').plot(x='TIME', y='CPU', ax=ax, label=PID)

for name, group in df1.groupby('PID'):
    group.plot(x='TIME', y='CPU', ax=ax, label=name, legend=False)
    
for name, group in df2.groupby('PID'):
    group.plot(x='TIME', y='CPU', secondary_y=True, ax=ax, label=name, legend=False)

handles,labels = [],[]
for ax in fig.axes:
    for h,l in zip(*ax.get_legend_handles_labels()):
        handles.append(h)
        labels.append(l)

plt.legend(handles,labels,loc='center right')
    
plt.show()
``` 

Now, to let the reader know that the other four PIDs are plotted based on right axis, I did this

```python
for name, group in df2.groupby('PID'):
    group.plot(x='TIME', y='CPU', secondary_y=True, ax=ax, label=str(name)+"(right)", legend=False)
```

## Full Final Code

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
%matplotlib inline

# Defines the chart font style
font = {'family' : 'Times New Roman',
        'weight' : 'bold',
        'size'   : 14}

# includes the chart font style
plt.rc('font', **font)

# You can also define like this
# plt.rcParams["font.family"] = "Times New Roman"

# To define figure size
figure(num=None, figsize=(12, 6))

df = pd.read_csv("syrupy_20220616132420.ps.log",delimiter=r"\s*")
df.columns

df1 = df.loc[df['PID'].isin(['15503','15505','15509'])]
df2 = df.loc[df['PID'].isin(['14399','15507','15510','15512'])]

fig, ax = plt.subplots(figsize=(8,6))
# df.groupby('PID').plot(x='TIME', y='CPU', ax=ax, label=PID)

for name, group in df1.groupby('PID'):
    group.plot(x='TIME', y='CPU', ax=ax, label=name, legend=False, rot=45)
    
for name, group in df2.groupby('PID'):
    group.plot(x='TIME', y='CPU', secondary_y=True, ax=ax, label=str(name)+"(right)", legend=False, rot=45)

plt.xticks(rotation=90)
    
# https://stackoverflow.com/questions/39902522/pandas-groupby-object-in-legend-on-plot
handles,labels = [],[]
for ax in fig.axes:
    for h,l in zip(*ax.get_legend_handles_labels()):
        handles.append(h)
        labels.append(l)

# used 'bbox_to_anchor' to put the legend outside
# used `ncol` to create horizontal legendbox
plt.legend(handles,labels,bbox_to_anchor=(.5, 1.2),loc='upper center',ncol=4)

# Show the plot
# plt.show()
    
# To save the figure as pdf/png/jpg, use plt.savefig
plt.savefig('CPU_log.pdf', dpi=300)
```

That's all for today! Cheers!!!
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MDMxMjE3NjUsMTU1MTEwODAyNSwxNz
Y1NTMyNzEwXX0=
-->