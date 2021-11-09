---
layout: single
title: "Matrix Operations in Python Numpy"
header:
  image: "https://live.staticflickr.com/65535/51665439656_9c1e063572_b.jpg"
  teaser: "https://live.staticflickr.com/65535/51665439656_9c1e063572_b.jpg"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - numpy
  - matrix operations
  - python modules
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

We often perform matrix operations in python. In this post, we will take a look at the simple matrix operations in Python.

First, let's import the module as follows:
```python
import numpy as np
```
Now, let's check out the matrix creation and operation procedures.

## Creating Matrix
1. Creating Matrix from list of lists
```python
>>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
>>> np.array(matrix)
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9]])
```
2. Creating matrix using `np.arrange()` and `np.reshape(array,(m,n))` where $m \times n$ is the size of the matrix.
```python
>>> import numpy as np
>>> nums = np.arange(0,16)
>>> matrix = np.reshape(nums,(4,4))
>>> matrix
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
```

3. Zero Matrix using `np.zeros()`
```python
>>> np.zeros((4,3))
array([[0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.]])
```

4. One matrix using `np.ones()`

```python
>>> np.ones((2,3))
array([[1., 1., 1.],
        [1., 1., 1.]])
```
5. Identity matrix using `np.eye(m)` where $m \times m$ is the size of matrix

```python
>>> np.eye(4)
array([[1., 0., 0., 0.],
    [0., 1., 0., 0.],
    [0., 0., 1., 0.],
    [0., 0., 0., 1.]])
```
6. Transpose matrix
```python
>>> matrix.T
array([[ 0,  4,  8, 12],
       [ 1,  5,  9, 13],
       [ 2,  6, 10, 14],
       [ 3,  7, 11, 15]])
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

## Accessing Values
```python
matrix = np.reshape(np.arange(0,16),(4,4))
print(matrix[0]) # first row
print(matrix[1][2]) # third element of second row
print(matrix[:,1]) # second column
print(matrix[:,-1]) # last column
# [0 1 2 3]
# 6
# [ 1  5  9 13]
# [ 3  7 11 15]
```

## Slicing of Matrix
```python
print(matrix[:3, :2])  # three rows, two columns
print(matrix[:2,])  # two rows, all columns
print(matrix[:,3])  # all rows, third column
print(matrix[:, 1:3])  # all rows, second to the third column
```

## Element-wise Addition, Subtraction, and Division
```python
>>> print(np.add(matrix,matrix))
[[ 0  2  4  6]
 [ 8 10 12 14]
 [16 18 20 22]
 [24 26 28 30]]
>>>
>>> print(np.subtract(matrix,matrix))
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
>>>
>>> print(np.divide(matrix,matrix))
[[nan  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]]
```

## Multiplication
1. Element-wise Multiplication (Hadamard Product)
	```python
	>>> print(np.multiply(matrix,matrix))
	[[  0   1   4   9]
	 [ 16  25  36  49]
	 [ 64  81 100 121]
	 [144 169 196 225]]
	```

2. Dot Product
	```python
	>>> print(np.dot(matrix,matrix))
	[[ 56  62  68  74]
	 [152 174 196 218]
	 [248 286 324 362]
	 [344 398 452 506]]
	```

## Other Notable Operations
1. Axis-wise Addition
```python
>>> np.sum(matrix,axis=0)  # column sum
array([24, 28, 32, 36])
>>>
>>> np.sum(matrix,axis=1)  # row sum
array([ 6, 22, 38, 54])
```

2. Matrix rank
```python
>>> np.linalg.matrix_rank(matrix)
2
```
3. Determinant of a square matrix
```python
>>> np.linalg.det(np.eye(5))
1.0
```
4. Numpy offers direct filtering/mapping options. Let's take a look at the examples:
```python
>>> test > 30
array([[ True, False, False],
       [ True,  True, False],
       [False,  True,  True]])
```

## Input a Matrix from a Input File
Let's create a input file named `T.txt` that contains the following input
```
1,0,2,0,0,0,0
1,1,2,2,0,0,1
2,2,1,1,0,0,2
1,1,2,1,0,2,1
```

Now, in the python script, do the following
```python
with  open('T.txt', 'r') as  f:
T = [[int(num) for  num  in  line.split(',')] for  line  in  f]
print(T)
```

## References
1. [Python Matrices and NumPy Arrays](https://www.programiz.com/python-programming/matrix)
2. [Matrix manipulation in Python](https://www.geeksforgeeks.org/matrix-manipulation-python/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMyOTE1MTU3NCwxNjE3NzQyOTFdfQ==
-->