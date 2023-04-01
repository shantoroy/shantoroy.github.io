---
layout: single
title: "Python Programming: Useful Tips and Tricks with Short Code Snippets"
excerpt:  "Are you looking for some useful Python tips and tricks that can help you write better code? Look no further! In this post, we have compiled a list of some of the most useful Python tips and tricks along with short code snippets to help you improve your Python programming skills. From creating generators and using the `with` statement to unpacking sequences and manipulating strings, these tips and tricks will save you time and help you write more efficient Python code."
seo_title:  "Python Programming: Useful Tips and Tricks with Short Code Snippets"
seo_description:  "Want to improve your Python programming skills? Check out these useful tips and tricks with short code snippets to help you write better and more efficient Python code, including creating generators, using the `with` statement, unpacking sequences, and manipulating strings."
header:
  image: "https://live.staticflickr.com/65535/51647090362_457bcd966b_b.jpg"
  teaser: "https://live.staticflickr.com/65535/51647090362_457bcd966b_b.jpg"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - tips and tricks
  - code snippets
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

In this post, we will learn to use some basic tips and tricks of Python.

1. Swap Two Numbers
	```python
	>>> x, y = 5, 10
	>>> x, y = y, x
	>>> x
	10
	>>> y
	5
	```
2. Reversing String
	```python
	>>> x = "hello"
	>>> x[::-1]
	'olleh'
	```
3. Sort a list
	```python
	>>> a = [5,2,8,3,1]
	>>> sorted(a)
	[1, 2, 3, 5, 8]
	>>> sorted(a,reverse=True)
	[8, 5, 3, 2, 1]
	```
4. Reversing a List
	```python
	>>> a = [5,2,8,3,1]
	>>> a[::-1]
	[1, 3, 8, 2, 5]
	```
5. Split data and assign values to variables
	```python
	>>> (age, income) = "35,150000".split(',')
	>>> age
	35
	```
7. Access Key and Value from a list using for loop
	```python
	mydict = {
		"a":"cat",
		"b":"dog"
	}
	
	for key,val in mydict.items():
		print("key:", key, "value:", val)
	```
8. Access items of two lists of same sizes at the same time
	```python
	a = [4,5,6]
	b = [1,2,3]
	for i,j in zip(a,b):
		print(i+j)
	# output
	# 5 7 9
	```
9. Create a string from the elements in list and Vice-versa
	```python
	mylist = ["hi", "there", "!"]
	string1 = " ".join(mylist)
	string2 = "".join(mylist)
	print(string1)
	print(string2)
	# output
	# hi there !
	# hithere!
	```
    ```python
	newlist = string1.split(" ")
	print(newlist)
	# output
	# ["hi", "there", "!"]
	```

10. List comprehension makes the code shorter
	```python
	myint = [2,4,6]
	mysquare = []
	for i in myint:
	    mysquare.append(i*i)
	print(mysquare)
	# output: [4, 16, 36]
	```
	same thing can be done in one line
	```python
	myint = [2,4,6]
	mysquare = [i*i for i in myint]
	print(mysquare)
	# output: [4, 16, 36]
	```
11. Get arguments from the terminal and put in a list
	```python
	import sys
	args = [int(arg) for arg in sys.argv[1:]]
	print(sum(args))
	``` 
	now, save the code in a file (here, `test.py`) and run like this
	```bash
	$ python test.py 2 4 6 8
	20
	```
12. Single line function using Python Lambda
	```python
	# an example function using def
	def testfunc(a,b):
	    return a**2 + b**2, a**3 + b**3

	x,y = testfunc(2,3)
	print(x,y)
	# output: 13 35
	```
	now, let's create the above function using lambda
	```python
	testfunc = lambda a,b: (a**2 + b**2, a**3 + b**3)
	x,y = testfunc(2,3)
	print(x,y)
	# output: 13 35
	```
13. map, filter, reduce 
	```python
	a = [1,2,3,4,5]

	square = map(lambda x:x**2, a)
	print(list(square))

	even = filter(lambda x:x%2==0, a)
	print(list(even))

	from functools import reduce
	summ = reduce(lambda x,y:x+y,a)
	print(summ)
	
	# output
	# [1, 4, 9, 16, 25]
	# [2, 4]
	# 15 
	```
14. Create a dictionary from two lists using dictionary comprehension
	```python
	a = [1,2,3,4,5]
	b = ["a", "b", "c", "d", "e"]
	mydict = {i:j for i, j in zip(a,b)}
	print(mydict)
	# output: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
	```
15. Sort a Dictionary by value
```python
sorted_dict = {k:v for k,v in sorted(my_dict.items(), key=lambda item: item[1])}
```

16. List edges of a graph using nested comprehension
	```python
	G = {
	    "a": ["b","c"],
	    "b": ["d", "e"],
	    "c": ["d", "e"],
	    "d": ["e"],
	    "e": ["f"]
	}

	def edgelist(graph):
	    edges = [(key,i) for key,val in graph.items() for i in val]
	    return edges

	print(edgelist(G))
	# output: [('a', 'b'), ('a', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'd'), ('c', 'e'), ('d', 'e'), ('e', 'f')]
	```
17. Flattening a list using `itertools`
	```python
	from itertools import chain
	print(list(chain.from_iterable([[1, 2], [3], [4], [5, 6]])))
	# output: [1, 2, 3, 4, 5, 6]
	```
18. use of arguments and keyword arguments in functions
	```python
	from functools import reduce
	def mysum(first, second, *args, kw1, **kwargs):
	    summ = first + second + reduce(lambda x,y:x+y, [i for i in args]) + kw1 + kwargs["end"]
	    return summ
	print(mysum(3, 4, 5, 6, 7, kw1=8, end=10))
	```
19. returning function from a function
	```python
	def myfunc():
	    def new():
	        print('hi there!')
	    return new

	a = myfunc()
	a()
	# output: hi there!
	```
20. Use of continue and break in loops
	```python
	for i in range(10):
	    if (i is 1):
	        continue
	    if (i > 5):
	        break
	    print(i)
	# output: 0 2 3 4 5
	```
21. Calculate runtime of a function using decorator
	```python
	from functools import wraps
	from time import time

	def runtime(func):
	    @wraps(func)
	    def wrapper(*args, **kw):
	        start = time()
	        result = func(*args, **kw)
	        end = time()
	        print('runtime: %2.4f sec' %(end-start))
	        return result
	    return wrapper

	@runtime
	def mysum(myrange):
	    summ = 0
	    for i in range(myrange+1):
	        summ += i
	    print("sum =", summ)

	mysum(5)
	# sum = 15
	# runtime: 0.0002 sec
	```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MjI0MTMxMjgsLTc3MTg4NDg4OCwyMT
Y1MjUwNDEsODQ5NDYxMTY5XX0=
-->