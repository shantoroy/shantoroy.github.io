---
layout: single
title: "Introduction to Data Science in Python: Seaborn Module"
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/51703083776_2035716824_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Matplotlib
  - Seaborn
  - Visualization
  - Data Science
  - Machine Learning
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post includes code snippets for drawing different stylish plots using the `Seaborn` Module"
---

In the [previous post](https://shantoroy.com/python/intro-to-data-science-data-visualization-matplotlib-part-2/), we learnt how to draw different types of plots using the `matplotlib` module.

In this post, we will see basic plotting using the `seaborn` module. [Seaborn](https://seaborn.pydata.org/) is widely used for more stylish less code-oriented plots. Seaborn actually uses `matplotlib` for its underlying functionalities.

Let's install the module using `pip install seaborn` and import it as follows:
```python
import seaborn as sns
```

Here, we will use some basic datasets for plotting that seaborn module already includes in its library. We can check the datasets using the following command.
```python
sns.get_dataset_names()
```
now, we will see the following output that includes the dataset names.
```
['anagrams',
 'anscombe',
 'attention',
 'brain_networks',
 'car_crashes',
 'diamonds',
 'dots',
 'exercise',
 'flights',
 'fmri',
 'gammas',
 'geyser',
 'iris',
 'mpg',
 'penguins',
 'planets',
 'taxis',
 'tips',
 'titanic']
```

We can load a particular dataset using `seaborn.load_dataset(<dataset_name>)`. You can check first few rows using the `dataframe_obj.head()` method.
```python
data = sns.load_dataset('titanic')
data.head()
```
For additional stat, use `dataframe_obj.describe()` method.
```python
data.describe()
```

Here, I provide sample examples of different sort of plots. Feel free to play around those. You can check the code outputs in [this Google Colab](https://colab.research.google.com/drive/1qXwoQZq0XXHrU4ZhP4HNJVDu3O8Kjt1R?usp=sharing).

## Usual Plots
### Count Plot
```python
sns.countplot(x='sex',data=data)
```

### Bar Plot
```python
sns.barplot(x='sex',y='total_bill',data=data)
```
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(12,8))
sns.barplot(x='sex',y='total_bill',data=data, ax=ax)
```

### Box Plot
```python
sns.boxplot(x="day", y="total_bill", data=data, palette='rainbow')
```

```python
sns.boxplot(data=data,palette='rainbow',orient='h')
```

### Factor Plot
```python
# factorplot has been changed to catplot
sns.catplot(x='sex',y='total_bill',data=data,kind='bar')  
```
```python
sns.factorplot(x='sex',y='total_bill',data=data,kind='bar')
```

### Linear Regression Plot
```python
sns.lmplot(x='total_bill',y='tip',data=tips)
```

```python
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
```

## Distribution Plots
### Dist Plot
```python
sns.distplot(data['total_bill'])
```
```python
sns.distplot(data['total_bill'],kde=False,bins=30)
```

### Joint Plot
```python
sns.jointplot(x='total_bill',y='tip',data=data,kind='scatter')
```

```python
sns.jointplot(x='total_bill',y='size',data=data,kind='scatter')
```

```python
sns.jointplot(x='total_bill',y='tip',data=data,kind='hex')
```

```python
sns.jointplot(x='total_bill',y='tip',data=data,kind='reg')
```

### Pair Plot
```python
# plots for entire dataframe
sns.pairplot(data)
```

```python
sns.pairplot(data,hue='sex',palette='coolwarm')
```


## Matrix Plots
### Heatmap of Correlation Plot
```python
# Matrix form for correlation data
data.corr()
```

```python
sns.heatmap(data.corr())
```

```python
sns.heatmap(data.corr(),cmap='coolwarm',annot=True)
```

```python
cor = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(cor)
```

```python
sns.heatmap(cor,cmap='magma',linecolor='white',linewidths=1)
```

### Cluster Map
```python
sns.clustermap(cor)
```

```python
sns.clustermap(cor,cmap='coolwarm',standard_scale=1)
```

Once again, feel free to check the code outputs in [this Google Colab](https://colab.research.google.com/drive/1qXwoQZq0XXHrU4ZhP4HNJVDu3O8Kjt1R?usp=sharing). 

Have a good day! Cheers!!!

For accessing all `data science in python` related posts, check this post:

[Collection of  `Data Science in Python`  Posts in my Blog](https://shantoroy.com/python/data-science-in-python-posts-in-my-blog/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTA3MTYyMDM5XX0=
-->