---
layout: single
title: "Introduction to Data Science: Pandas Module (Part 01)"
header:
  image: "https://live.staticflickr.com/65535/51677928748_7cd1af1e23_o.png"
  teaser: "https://live.staticflickr.com/65535/51677928748_7cd1af1e23_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Pandas
  - Numpy
  - Data Science
  - Machine Learning
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



`pandas` is the mostly used module while analyzing data from a CSV, JSON, or Excel as the module can convert these data into dataframes and helps to analyze the data.

In this tutorial, we will see some basic usages of this module.

First thing first, let's import the module
```python
import pandas as pd
```
Now, let's take a look at some basic tips and tricks

## Series
We can create a series from a list or dictionary where for a list, the index column has index values ($0,1,2,\dots$) and for a dictionary, the index column has key values (for below example, $a,b,c$).
```python
mylist = ['a','b','c']
mynums = [1,2,3]
mydict = {'a':10,'b':20,'c':30}
print(pd.Series(data=mylist))
print(pd.Series(data=mydict))
print(pd.Series(mynums,labels))
# pd.Series(data=mynums,index=labels)
```
If we use two lists inside the `pd.Series` method, the first one's items are put in the data column, and the second list items are put in the index column.

## Dataframes
### Creating Dataframes
We can simply create a dataframe using the `pandas.Dataframe()` method. The following example creates a matrix of size $5 \times 4$ with random numbers, and then set index labels from A to E, and column labels from W to Z.
```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
```

Let's take a look at another example-
```python
import pandas as pd
data = [['X', 10], ['Y', 15], ['Z', 20]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])
```
The above example creates two columns with putting first elements from all internal lists from `data`, under the column `Name` and then second elements under the column `Age`.

If we want to create a dataframe by reading a CSV file, we can use the following:
```python
df = pd.read_csv('file_name.csv')
```

You can use a few other options described below:

1. If you want to import only a subset of columns, you can define which columns to import by using the option `usecols`
	```python
	pd.read_csv('file_name.csv', usecols= ['column_name_1','column_name_2'])
	```
	or the indices of the columns
	```python
	pd.read_csv('file_name.csv',usecols=[1,2,3])
	```

2. If your CSV file does not have column headers, set `header=None`
	```python
	df.read_csv('file_name.csv’, header=None)
	```

3. If you want to use a particular column as index, use the option `index_col`
	```python
	pd.read_csv('file_name.csv', index_col='column_name_to_set_index')
	```
4. Import a range of rows from the file. The following example reads rows $31$ to $45$. `skiprows` skips the first $30$ while reading first $45$ rows using `nrows`.
	```python
	df = pd.read_csv('file_name.csv', dtype=float, skiprows=30, nrows=45)
	```


## Dataframe Operations
1. Access a particular column
	```python
	df['target_column_name']
	```
2. Accessing multiple columns
	```python
	df[['one_column_name','another_column_name']]
	```
3. Accessing first $n$ or last $n$ number of rows
```python
df.head(5)
```
```python
df.head(5)
```
5. Creating a new column
	```python
	df['new_column_name'] = df['column_name_1'] + df['column_name_2']
	```
6. Deleting a column
	```python
	df.drop('target_column_name',axis=1)
	```
7. Deleting a row
	```python
	df.drop('row_index',axis=0)
	```
8. selecting a row using `loc` or `iloc`
	```python
	df.loc['row_index']
	```
	```python
	df.iloc[row_index]
	```
9. Accessing a single value
	```python
	df.loc['row_index','column_header']
	```
10. Accessing values from selected multiple rows and multiple columns
	```python
	df.loc[['row_index_1','row_index_2'],['column_header_1','column_header_2']]
	```
11. creating a new CSV file
	```python
	df.to_csv('file_name.csv')
	```
	exporting without index

	```python
	df.to_csv('file_name.csv', index=False)
	```
	sometimes you can get the `UnicodeEncodeError`. To avoid that

	```python
	df.to_csv('file_name.csv', encoding='utf-8')
	```
	export particular columns only
	```python
	dt.to_csv('file_name.csv',columns=['col_1','col_2'])
	```

## Dataframe Visualization (Graphs)
`pandas` module offers some direct visualizations (using `matplotlib` in the background).
1. bar plot
	```python
	df.plot.bar()
	```
	or a stacked bar plot

	```python
	df.plot.bar(stacked=True) 
	```
2. histogram
	```python
	df['column_name'].hist()
	```
3. line plot
	```python
	df.plot.line(y='column_name',figsize=(10,3),lw=1)
	```
4. scatter plot
	```python
	df.plot.scatter(x='column_1',y='column_2')
	```
	using a colormap
	```python
	df.plot.scatter(x='col_1',y='col_2',c='col_3',cmap='coolwarm')
	```
5. box plot
	```python
	df.plot.box()
	```
6. density plot
	```python
	df.plot.density()
	```

In this post, I just showed a few basic uses of the module `pandas`. In the next post, we will take a more elaborate look at the module. 

Till then, cheers!
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwODEzNzAxMDMsLTE2MjE2NTA3OF19
-->