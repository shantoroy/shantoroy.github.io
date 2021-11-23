---
layout: single
title: "Hash Tables Concept and Implementation in Python"
header:
  image: "https://live.staticflickr.com/65535/51653692227_af82a634a0_b.jpg"
  teaser: "https://live.staticflickr.com/65535/51653692227_af82a634a0_b.jpg"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Hashtable
  - Dictionary
  - Algorithm
  - Data Structure
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



Hashtables are widely used to store and search data in a optimized manner. Hashtable or hashmap is a typical data structure that maps keys to values. While storing and searching for target data, the procudure hashes the key and the resulting key indicates the position to store or look up.

In this post, we will discuss the basics of hashtables and then take a look at simple implementations in python.

### Complexity
The most well-known searching methods have the following complexities.
* Linear Search $\rightarrow$ O(n)
* Binary Search $\rightarrow$ O(logn)

We know, the worst scenario for binary search is way better than the worst scenario for linear search. However, using hashtable, our target is to have constant time complexity for lookup.

* Our target is $\rightarrow$ O(1)

### Initial Idea
The initial idea was to store keys as the indices of an array. However, that leaves a lot of spaces be wasted.


There comes the idea of a function.
* Problem: One-to-one function $\rightarrow h(x) = x$
* Solution: Many-to-one function $\rightarrow h(x) = x\ \% \ size\_of\_array$

Now, in the solution, there is a chance of collision. That means two keys may have the same indices. For example, if the size of an array is $10$, then $5$ and $15$ will have the same indices.

There are several solutions to this issue:

* **Chaining:** This problem can be solved by chaining. In terms of data structure, we can use the `linked list`. So, if there is a collision, the pointer of the linked list directs the particular index that contains the second value and so on for the later ones. However, th
* **Linear Probing:** Here, we store the value received by calculating $h(x) = x\ \% \ size\_of\_array$, to the immediate next index. Therefore, we modify the function for later use as:
		$h'(x) = [h(x) + f(i)]\ \% \ size\_of\_array$
		where, $f(i)=i$ and $i=0,1,2,....$
		
	so, basically, if the array size is $10$, and we need to store values for keys $5$ and $15$, then we get $5$ for each, right? (using $h(x) = x\ \% \ size\_of\_array$)

	now, when we look for $5$, it is just the index $5$. But when we look for $15$, we calculate like this:
	$h'(15) = [h(15) + f(0)] \% 10 = 5$
	$h'(15) = [h(15) + f(1)] \% 10 = 6$
	so, index $6$ is our target to look for.

	if there is another collision, then we use $i=2,3,...$ and so on. Now, if there is a item $6$ to be searched for, and we already stored $15$ there, then we store $6$ in the immediate next empty location. So, while storing for an item, we keep going next until we reach an empty space to store the key. Also, similarly, while searching, we keep going next until an empty space is found and we declare the item is not present there.

* **Quadratic Probing:** A better approach is to modify the same equation as:
	$h'(x) = [h(x) + f(i)]\ \% \ size\_of\_array$
		where, $f(i)=i^2$ and $i=0,1,2,....$
		the only change is the function $f(i)$.


## Python Implementation

Python already has an advanced data type named `Dictionay` where you can directly store items as key-value pairs. Python dictionaries are an efficient implementation of a hashtable. An example dictionary is:

```python
my_hash_table = {
	2: "cat",
	22: "dog",
	32: "parrot"
}
```

You can simply search for a value using a key like this:
```python
>>> my_hash_table[22]
>>> dog
```

You can check a list of Dictionary Methods [here](https://www.w3schools.com/python/python_ref_dictionary.asp).

However, if you want to create a class of hashtable, here is a [simple implementation](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable/4_HashTable.ipynb) from [codebasics github](https://github.com/codebasics).

```python
class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
```

Now, input two data and then check the whole array to find where the data has been stored.
```python
if __name__=="__main__":
	t  =  HashTable()  
	t["march 6"]  =  310  
	t["march 7"]  =  420
	print(t.arr)
```


You can also take a look at some examples of `distributed hash table` where the same concept is implemented in distributed fashion which is more common scenario in cloud computing.

* kademlia: https://github.com/bmuller/kademlia
* Bittorrent DHT: https://github.com/nitmir/btdht

There are a few drawbacks of hashtables as well. An efficient algorithm has to ensure a good hashing technique (which are typically costly) to avoid possible collisions. However, considering scaling, hashtables work way better than other search methods.

This is all for today. Feel free to let me know if I have missed anything to include in this post.


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ2MDU2OTEwNSwtNDM5NTQyMzQ3XX0=
-->