---
layout: single
title: "Introduction to Data Science in Python: Numpy Module"
header:
  image: "https://live.staticflickr.com/65535/51652426627_4e5afafd1f_b.jpg"
  teaser: "https://live.staticflickr.com/65535/51652426627_4e5afafd1f_b.jpg"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Numpy
  - Pandas
  - Matplotlib
  - Data Science
  - Machine Learning
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Numpy is a popular python module that provides fast and efficient operations on n-dimensional arrays of homogeneous data. It has variety of functions that can perform high-end scientific and numerical operations.

In this post, we will see some basic common usages of the module.

First, we have to import the module. Usually, we import like this-
```python
import numpy as np
```

Now, let's checkout some basic operations.

## Creating Numpy Arrays

### From Python Lists
We can simply, use `np.array()` function to convert a python list into array.
```python
>>> a = [1,2,3,4,5]
>>> np.array(a)
array([1, 2, 3, 4, 5])
```

```python
>>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
>>> np.array(matrix)
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9]])
```

### Built-in Methods
1. `np.arrange()` works exactly like python `range()`. Let's look at some examples. The first example has start and ending value while the second one has another parameter for step difference.
	```python
	>>> np.arange(0,10)
	array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9])
	```

	```python
	>>> np.arange(9,21,2)
	array([ 9, 11, 13, 15, 17, 19])
	```

2. If we want to create n-dimensional arrays (matrix) using only zeros or ones, we can use `np.zeros()` and `np.ones()` respectively.
	```python
	>>> np.zeros(5)
	array([0., 0., 0., 0., 0.])
	```
	we can also define the size $m \times n$ where m is the number of rows and n is the number of columns
	```python
	>>> np.zeros((4,3))
	array([[0., 0., 0.],
	       [0., 0., 0.],
	       [0., 0., 0.],
	       [0., 0., 0.]])
	```

	```python
	>>> np.ones((2,3))
	array([[1., 1., 1.],
	       [1., 1., 1.]])
	```

3. We can use `np.linspace()` to return evenly spaced numbers over a specified interval

	```python
	>>> np.linspace(0,10,3)
	array([ 0.,  5., 10.])
	```

4. `np.eye()` can be used to create an identity matrix. The following example creates an identity matrix of size $4 \times 4$
```python
>>> np.eye(4)
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])
```

5. `np.random.rand()` can be used to create random samples from a uniform distribution over [0, 1).
```python
>>> np.random.rand(5)
array([0.26107011, 0.39744656, 0.30421456, 0.33464264, 0.00952929])
```

```python
>>> np.random.rand(5,5)
array([[0.06062392, 0.50044789, 0.16726052],
       [0.22518242, 0.6768908 , 0.34212198],
       [0.81288987, 0.71675748, 0.65559496]])
```
for creating a matrix of random samples from a normal distribution we use `np.random.randn()` method
```python
>>> np.random.randn(5)
array([-0.4356041 ,  3.21925889, -1.95362245, -1.11175927, -0.61676613])
```
array of random integer can be created using `np.random.randint()` method. the following example creates an array of $10$ random integers ranged between $1$ and $100$.
```python
>>> np.random.randint(1,100,10)
array([61, 73, 57, 15, 13, 61, 50, 14, 47, 44])
```
also, we can use `np.random.choice()` method. Here, we create an array of $10$ random numbers ranged between $0$ and $19$. The `replace=False` ensures no duplicate value is included.
```python
>>> np.random.choice(range(20), 10, replace=False)
array([ 8,  0,  6, 10,  3,  7,  2,  4,  1, 16])
```
same thing can be done using `random.sample()` method too. But you need to convert it to numpy array if you want it to perform numpy operations.
```python
>>> import random
>>> random.sample(range(100), 10)
[18, 99, 98, 92, 63, 30, 5, 20, 60, 47]
```

## `max/min` and `argmax/argmin`
in numpy, `array_variable.max()` and `array_variable.min()` are used to return the maximum/minimum values respectively. `array_variable.argmax()` and `array_variable.argmin()` are used to return the indices of maximum/minimum values respectively. 

```python
>>> test = np.random.randint(1,100,9)
>>> test.reshape(3,3)
>>> test
array([[34, 12, 22],
       [69, 36, 27],
       [26, 57, 53]])
>>> test.max()
69
>>> test.min()
12
>>> test.argmax()
3
>>> test.argmin()
1
```

## Numpy Operations
We can use the itemwise addition, subtraction, multiplications, and divisions as follows. Square and logs can be calculated using `np.sqrt()` and `np.log()` methods.
```python
>>> test + test
[[ 68  24  44]
 [138  72  54]
 [ 52 114 106]]
>>>
>>> test - test
[[0 0 0]
 [0 0 0]
 [0 0 0]]
>>>
>>> test * test
[[1156  144  484]
 [4761 1296  729]
 [ 676 3249 2809]]
>>>
>>> test / test
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
>>>
>>> test ** 2
[[1156  144  484]
 [4761 1296  729]
 [ 676 3249 2809]]
>>>
>>> np.sqrt(test)
array([[5.83095189, 3.46410162, 4.69041576],
       [8.30662386, 6.        , 5.19615242],
       [5.09901951, 7.54983444, 7.28010989]])
>>> 
>>> np.log(test)
array([[3.52636052, 2.48490665, 3.09104245],
       [4.2341065 , 3.58351894, 3.29583687],
       [3.25809654, 4.04305127, 3.97029191]])
```


## Indexing in Numpy Array
Indexing is similar to the regular python list.
```python
>>> test[2]
array([26, 57, 53])
```

```python
>>> test[1:]
array([[69, 36, 27],
       [26, 57, 53]])
```

```python
>>> test[1][1]
36
>>>
>>> test[:2,1:]
array([[12, 22],
       [36, 27]])
```

## Mapping/Filtering
Numpy offers direct filtering/mapping options. Let's take a look at the examples:
```python
>>> test > 30
array([[ True, False, False],
       [ True,  True, False],
       [False,  True,  True]])
```

which is normally done using python map
```python
>>> a = [5, 6, 78, 34, 56]
>>> list(map(lambda x: x>15, a))
[False, False, True, True, True]
```

I hope, the above-mentioned methods are enough for the basic. We will go through more advanced operations later in another post. Till then, cheers!

For accessing all `data science in python` related posts, check this post:

[Collection of  `Data Science in Python`  Posts in my Blog](https://shantoroy.com/python/data-science-in-python-posts-in-my-blog/).

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI3OTQ0MjMxMSwtMTQ5MDk1MDMzNCwxMj
kyODg0NDQwXX0=
-->