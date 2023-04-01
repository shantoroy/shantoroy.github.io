---
layout: single
title: "Useful Functions of Python Itertools Module"
excerpt:  "Python itertools module is a powerful library to create fast and efficient iterators. It provides a set of functions for working with iterators and can be used to simplify complex problems into smaller, manageable chunks. In this blog post, I will explore some of the most useful functions of the Python itertools module." 
seo_title: "Mastering Python Iterators with itertools Module: A Comprehensive Guide"
seo_description:  "Discover the power of the Python itertools module and learn how to create fast and efficient iterators. Explore some of the most useful functions of the itertools module to simplify complex problems into smaller, manageable chunks."
header:
  image: "https://live.staticflickr.com/65535/51665428921_00a40a1374_b.jpg"
  teaser: "https://live.staticflickr.com/65535/51665428921_00a40a1374_b.jpg"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Itertools
  - iterator
  - python functions
  - python modules
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



Python `itertools` module provide memory-efficient solutions for producing complex iterators. It is quite useful in different situations where it provides functionalities for faster programs along with efficient memory usage.

In this post, we will take a look at some basic functions of this module.

1. `zip_longest()` fills-up zip list for uneven lengths of lists. It fills the empty spaces in pairs with a given value. Typically, the basic syntax is `itertools.zip_longest(*iterables, fillvalue=None)`.
	```python
	mylist = ["a","b","c"]
	index_items = list(zip(range(1,10),mylist))
	print(index_items)
	index_future_items = list(it.zip_longest(range(1,10),mylist))
	print(index_future_items)
	# [(1, 'a'), (2, 'b'), (3, 'c')]
	# [(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None), (6, None), (7, None), (8, None), (9, None)]
	```

2. `cycle` creates a copy of an iterable and start iterating over the copied version when the previous iterator is exhausted. Typically, the basic syntax is`itertools.cycle(iterable)`.
This function is useful for writing the simplest round-robin function in just two lines. 
	```python
	mylist = ["a","b","c"]
	my_list_cycle = it.cycle(mylist)
	new_list = [next(my_list_cycle) for _ in range(5)]
	print(new_list)
	# ['a', 'b', 'c', 'a', 'b']
	```

3. `combinations` and `permutations` provides the mathematical combination and permutation over a iterable. Typically, the syntax are `itertools.combinations(iterable, r)` and `itertools.permutations(iterable, r)`.
	```python
	mylist = ["a","b","c"]
	combination = list(it.combinations(mylist,2))
	permutation = list(it.permutations(mylist,2))
	print(combination)
	print(permutation)
	# [('a', 'b'), ('a', 'c'), ('b', 'c')]
	# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
	```

4. Cartesian Product using `product()`. The syntax is `itertools.product(*iterables, repeat=1)`.
	```python
	letters = ["a","b","c"]
	numbers = [0,1,2]
	cart_product_1 = list(it.product(numbers,letters))
	cart_product_2 = list(it.product(numbers,letters, repeat=2))
	print(cart_product_1)
	print(cart_product_2)
	# [(0, 'a'), (0, 'b'), (0, 'c'), (1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]
	# [(0, 'a', 0, 'a'), (0, 'a', 0, 'b'), (0, 'a', 0, 'c'), (0, 'a', 1, 'a'), (0, 'a', 1, 'b'), (0, 'a', 1, 'c'), (0, 'a', 2, 'a'), (0, 'a', 2, 'b'), (0, 'a', 2, 'c'), (0, 'b', 0, 'a'), (0, 'b', 0, 'b'), (0, 'b', 0, 'c'), (0, 'b', 1, 'a'), (0, 'b', 1, 'b'), (0, 'b', 1, 'c'), (0, 'b', 2, 'a'), (0, 'b', 2, 'b'), (0, 'b', 2, 'c'), (0, 'c', 0, 'a'), (0, 'c', 0, 'b'), (0, 'c', 0, 'c'), (0, 'c', 1, 'a'), (0, 'c', 1, 'b'), (0, 'c', 1, 'c'), (0, 'c', 2, 'a'), (0, 'c', 2, 'b'), (0, 'c', 2, 'c'), (1, 'a', 0, 'a'), (1, 'a', 0, 'b'), (1, 'a', 0, 'c'), (1, 'a', 1, 'a'), (1, 'a', 1, 'b'), (1, 'a', 1, 'c'), (1, 'a', 2, 'a'), (1, 'a', 2, 'b'), (1, 'a', 2, 'c'), (1, 'b', 0, 'a'), (1, 'b', 0, 'b'), (1, 'b', 0, 'c'), (1, 'b', 1, 'a'), (1, 'b', 1, 'b'), (1, 'b', 1, 'c'), (1, 'b', 2, 'a'), (1, 'b', 2, 'b'), (1, 'b', 2, 'c'), (1, 'c', 0, 'a'), (1, 'c', 0, 'b'), (1, 'c', 0, 'c'), (1, 'c', 1, 'a'), (1, 'c', 1, 'b'), (1, 'c', 1, 'c'), (1, 'c', 2, 'a'), (1, 'c', 2, 'b'), (1, 'c', 2, 'c'), (2, 'a', 0, 'a'), (2, 'a', 0, 'b'), (2, 'a', 0, 'c'), (2, 'a', 1, 'a'), (2, 'a', 1, 'b'), (2, 'a', 1, 'c'), (2, 'a', 2, 'a'), (2, 'a', 2, 'b'), (2, 'a', 2, 'c'), (2, 'b', 0, 'a'), (2, 'b', 0, 'b'), (2, 'b', 0, 'c'), (2, 'b', 1, 'a'), (2, 'b', 1, 'b'), (2, 'b', 1, 'c'), (2, 'b', 2, 'a'), (2, 'b', 2, 'b'), (2, 'b', 2, 'c'), (2, 'c', 0, 'a'), (2, 'c', 0, 'b'), (2, 'c', 0, 'c'), (2, 'c', 1, 'a'), (2, 'c', 1, 'b'), (2, 'c', 1, 'c'), (2, 'c', 2, 'a'), (2, 'c', 2, 'b'), (2, 'c', 2, 'c')]
	```

5. `chain()` makes an iterator that returns sequential iterators from the sequential iterables. The syntax is `itertools.chain(*iterables)`.

	```python
	combined = list(it.chain(letters,numbers))
	print(combined)
	# ['a', 'b', 'c', 0, 1, 2]
	```

6. `compress()` works like a filter. The syntax is `itertools.compress(data, selectors)`.
	```python
	mylist = ["a","b","c"]
	my_bool = [True,False,True]
	filtered = list(it.compress(mylist,my_bool))
	print(filtered)
	# ['a', 'c']
	```

7. `accumulate()` makes an iterator that returns accumulated result of of any binary functions. The syntax is `itertools.accumulate(iterable[, func, *, initial=None])`.

	```python
	import operator as op
	acc = list(it.accumulate(numbers))
	acc_mul = list(it.accumulate(numbers, op.mul))
	acc_sub = list(it.accumulate(numbers, op.sub))
	acc_div = list(it.accumulate(numbers, op.floordiv))
	print(acc)
	print(acc_sub)
	print(acc_mul)
	print(acc_div)
	# [1, 3, 6, 10]
	# [1, -1, -4, -8]
	# [1, 2, 6, 24]
	# [1, 0, 0, 0]
	```

	or you can use customized `lambda` functions
	```python
	acc_sub = list(it.accumulate(numbers,
	lambda x, y: y - x))
	```


8. `tee()` returns $n$ number of independent copies of a single iterable. The standard syntax is `itertools.tee(iterable, n=2)`.

	```python
	numbers = [1,2,3,4]
	c1, c2, c3 = it.tee(numbers,3)
	print(list(c1), list(c2), list(c3))
	# [1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4]
	```

9. `islice()` returns selected elements from the iterable. Works similar to the `range()` function. The basic syntax is `itertools.islice(iterable, stop)` or ``itertools.``islice`(iterable, start, stop[, step])`.
 
	```python
	my_slice = list(it.islice([1, 2, 3, 4], 1, 3))
	print(my_slice)
	evenlist = list(it.islice(list(range(20)),2,15,2))
	print(evenlist)
	# [2, 3]
	# [2, 4, 6, 8, 10, 12, 14]
	``` 

There are some other useful functions too. I included only the most common ones here. For more details, checkout the [Official Documentation](https://docs.python.org/3/library/itertools.html#itertools.islice).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMTY4MDAxNTIsLTM0NDA3ODI2MF19
-->