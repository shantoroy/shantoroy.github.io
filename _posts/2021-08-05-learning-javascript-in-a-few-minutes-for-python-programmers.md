---
layout: single
title: "Learning JavaScript Basic Syntax in a few minutes for Python Programmers"
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/51710532826_e84ae3159c_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Javascript
  - Syntax
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post introduces Javascript basic syntax to the Python Programmers in a few minutes"
---


If you know how to code in Python, this post will help you learning the basic syntax differences within a few minutes.

In this post, I provided examples for both `Python` and `Javascript` for the same problems.

## Running JS in the Terminal
Let's first install `NodeJS` if we want to run JS like python script on the terminal.

If you are a MacOS user, install via `brew`
```bash
$ brew install node
```

If you are a Linux user, use following steps to install NodeJS. Remember, `apt` is used for Debian-alike distributions (e.g., Ubuntu). You need to use `yum` if you are using rpm-based distributions (e.g., Red Hat, Cent OS, etc.).
```bash
$ sudo apt install nodejs
$ sudo apt install npm
```

Create a JS file where we will copy and paste the example programs provided in this post.
```bash
$ nano test.js
```
Now, we can run the script using `node`
```bash
$ node test.js
```


## Comment
This is how we use single- and multi-line comments in `python`
```py
# this is a single-line comment 

"""
This is
multi-line
comments
"""
```

This is how we use single- and multi-line comments in `javascript`
```js
// this is a single-line comment 

/*
This is
Multi-line
Comment
*/
```

## Variable/Constants
In python we can directly use a variable by assigning value to it. There is no fixed constant type variable in python. That's why we put constants in a different file (module) and then import constants via module.
```py
# python variable
x = "variable/constant doesn't matter."
```

In Javascript, we can denote variable using `let` and constants using `const` keyword.
```js
// JS variable and constant
let x = "variable"
const PI = 3.1416
```

## List/Dictionary Data
### Array vs List
Python List and JavaScript Array have the same structure.
```py
# python list
my_list = ["a", "b"]
```

```js
// Javascript array
let my_list = ["a", "b"];
```

### Dictionary
Javascript has a dictionary-alike data type which is called object.
```py
# initiating a Dictionary in Python
my_dict_1 = {}
my_dict_2 = dict()
```

```js
// initiating an object data in javascript
let my_dict_1 = {};
let my_dict_2 = new Object();
```

## Boolean
Javascript requires `Boolean()` to generate a boolean value (`true`/`false`).
```py
# python boolean
def check_even(num):
	return num % 2 == 0

print(check_even(8))
```

```js
// JS boolean
function check_even(num)
	{
		return Boolean(num % 2==0);
	}

console.log(check_even(8))
```

## Loop
This is how we use a simple `for-loop` in python
```py
# python for-loop
for count in range(5):
    print(f"count: {count}")
```

Javascript `for-loop` looks alike `C-lang` loops.
```js
// JS for-loop
for(count = 0; count < 5; count++) 
  {
    console.log(`count: ${count}`);
  } 
```

This is how we use `in` keyword within a `for-loop` in python
```py
# python for-loop
num_list = [3,4,5]
for num in num_list:
	print(f"item: {num}")
```
JavaScript also provides similar feature, however, accessing the index rather than the value itself.
```js
// JS for-loop
let num_list = [3,4,5]
for(idx in num_list) 
  {
    console.log(`item: ${num_list[idx]}`)
  } 
```

## Conditions and Functions
### General Function
this is a simple example of function and condition in JavaScript. JS used braces for anything that we use indentation in case of python.
```js
// JS function and condition
function fib(n)
{
	if (n > 1) 
	{
		return fib(n-2) + fib(n-1);
	}
	return 1;
}

console.log(fib(4))
```

### Shortcut
JS also provides shortcut options for functions alike python. Let's take a look at the same example in shorter versions for both languages.
```py
# python function
def fib(n):
    return fib(n-2) + fib(n-1) if n > 1 else 1

print(fib(5))
```

```js
// JS function
function fib(n)
{
	return (n > 1) ? fib(n-2) + fib(n-1) : 1;
}

console.log(fib(5))
```

### Lambda (Python) vs Arrow (JS) Functions
Python features a one-line function called the `lambda`-function.
```py
add = lambda a,b: a+b
print(add(4,5))
```

JS also features a one-line function named as the `arrow`-function.
```js
let add = (a,b) => a + b; 
console.log(add(4,5))
``` 

## Class 
This is how we create and use `class` in python.
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        print(f'Name is {self.name}.')
        print(f'Age is {self.age}.')


roy = Person("Mr. X", 30)
roy.person_info()
```

JS uses a `constructor` method that works alike `__init__` method in python. Both are initializer methods. JS does not use an additional argument `self` like python. JS simply uses `this` instead of `self` while using class variables.

```js
class Person {
  constructor(name,age) {
    this.name = name;
    this.age = age;
  }
  person_info() {
    console.log(`Name is ${this.name}.`);
    console.log(`Age is ${this.age}.`);
  }
}

mrx = new Person("Mr. X", 30);
mrx.person_info();
```

That's it. There are a lot of other functionalities in both languages. This post was written just intended to provide some basic introduction to JS syntax for python coders. 

So, if you are a python programmer, it will take only a couple of minutes to get introduced to JS syntax structure.

Have a good day, chill!!! :sunglasses:
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg0MTgwNzgyMl19
-->