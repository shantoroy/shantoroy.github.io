---
layout: single
title: "Introduction to Data Science: Pandas Module (Part 02)"
header:
  image: "https://live.staticflickr.com/65535/51677688266_10458b914a_o.png"
  teaser: "https://live.staticflickr.com/65535/51677688266_10458b914a_o.png"
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

In the [previous post](https://shantoroy.com/python/intro-to-data-science-pandas-module/), we have seen some basic usages of the `pandas` module. In this post, we will take a look at some more useful functionalities of the module.

## Conditioning
1. Show a filtered dataframe with values that satisfies the condition. The following example presents the same dataframe with values greater than zero. Values that do not satisfy conditions, are set to `np.NaN` or Null.
	```python
	df[df>0]
	```
2. Show all rows that satisfy condition for a particular column
	```python
	df[df['col_name']>0]
	```
3. Show all rows with target column values
	```python
	df[df['conditioned_col_name']>0]['target_col_name']
	```

	```python
	df[df['conditioned_col_name']>0][['target_col_name_1','target_col_name_2']]
	```
4. Use of multiple conditions using `and` and `or`
	```python
	df[(df['conditioned_col_name_1']>0) & (df['conditioned_col_name_2'] > 0)]
	```

	```python
	df[(df['conditioned_col_name_1']>0) | (df['conditioned_col_name_2'] > 0)]
	```

## Merging, Joining, and Concatenating
1. Concatenation
	```python
	pd.concat([df1,df2,df3])
	```
2. Merging/Joining
	```python
	pd.merge(df5,df6,how='inner',on='index')
	```
	```python
	df1.join(df2)
	```
	```python
	ndf1.join(df2, how='outer')
	```

## Tips and Tricks
1. Column Slicing
	```python
	df.iloc[:,start_index:ending_index].head()
	```
	or

	```python
	df.loc[:,'start_column_name':'ending_column_name'].head()
	```
2. Add row total and column total to a numerical dataframe
	```python
	df['col_total'] = df.apply(lambda x: x.sum(), axis=1)  
	df.loc['row_total'] = df.apply(lambda x: x.sum())
	```
3. Access multiple files together with same columns
	```python
	from glob import glob
	files = sorted(glob(data/file_name*.csv))
	pd.concat((pd.read_csv(file) for file in files),ignore_index=True) 
	```
4. Read dataframe from Clipboard (quickly copying from Excel or Google Sheet)
	```python
	df = pd.read_clipboard()
	```
5. Read online JSON file
	```python
	df = pd.read_json('target_url')
	```
6. Scrape tables from webpage
	```python
	pd.read_html("target_URL")
	```
7. Apply functions to columns and save modified data in new columns
	```python
	for col in df.columns:
		df[f'{col}_modified'] = df[col].apply(function_name)
	```
8. Change location of a new column
	```python
	cols = list(df.columns)
	target_loc = 3
	cols = [:target_loc] + ['new_col_name'] + cols[target_loc:-1]
	df = df[cols]
	```
9. insert a new column at a particular location
	```python
	df.insert(target_loc, 'target_col_name', df['col_name'].apply(function_name))
	``` 
10. renaming column names
	```python
	df = df.rename({'col_1':'new_col_1','col_2':'new_col_2',}, axis='columns')
	```
11. Reversing the column order
	```python
	df.loc[:,::-1]
	```
12. Reverse row order
	```python
	df.loc[::-1]
	```
13. Split names (first-last) or locations (city-state) in different columns
	```python
	df[['new_col_1','new_col_2']] = df.col_name.str.split(' ',expand=True)
	```
	use `split(',')` if the city-state format is like `Houston,TX`.

14. Select columns by data type
	```python
	df.select_dtypes(include=['number','object','category'])
	```
	```python
	df.select_dtypes(exclude=['object','category'])
	```

15. Count number of values with different data types if exist in a single column
	```python
	df.col_name.apply(type).value_counts()
	```
16. You can transpose a dataframe like a matrix
	```python
	df.T
	```

I will keep adding useful functionalities of `pandas dataframe` in this post.


## References
1. [100 pandas tricks to save you time and energy](https://www.dataschool.io/python-pandas-tips-and-tricks/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE4NzgzMzIxMiw5ODcwNzc5MzAsMTM1OT
AwNTc2OSw3NzMxNjU2MTVdfQ==
-->