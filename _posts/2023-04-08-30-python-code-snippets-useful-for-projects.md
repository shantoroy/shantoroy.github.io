---
layout: single
title: "Top 30 Useful Python Snippets that are Useful for Your Next Project"
excerpt: "Discover 30 Python code snippets that can save you valuable time and help you get your next project up and running quickly. These code snippets include time-saving tricks, file management, string manipulation, and data analysis, as well as other useful tips and tricks. Whether you're a beginner or an experienced Python developer, these code snippets will help you become more efficient and productive."
seo_title: "Top 30 Useful Python Snippets to Improve Your Workflow"
seo_description: "Boost your productivity with these 30 useful Python code snippets. Learn time-saving tricks, file management, string manipulation, and data analysis, and list comprehension techniques that can help you get your next project up and running quickly. Whether you're a beginner or an experienced Python developer, these snippets will help you become more efficient and productive."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Snippets
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

1.  Check if a string is empty:

    ```py
    if not my_string:
        print("String is empty")
    ``` 
    
2.  Sort a dictionary by value:

    ```py
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    ``` 
    
3.  Merge two dictionaries:

    ```py
    my_dict_1.update(my_dict_2)
    ``` 
    
4.  Flatten a list of lists:

    ```py
    flattened_list = [item for sublist in my_list for item in sublist]
    ``` 
    
5.  Check if a list contains duplicates:

    ```py
    if len(my_list) != len(set(my_list)):
        print("List contains duplicates")
    ``` 
    
6.  Reverse a string:

    ```py
    reversed_string = my_string[::-1]
    ``` 
    
7.  Get the current date and time:

    ```py
    import datetime
    now = datetime.datetime.now()
    ``` 
    
8.  Get the file extension from a file path:

    ```py
    file_extension = os.path.splitext(file_path)[1]
    ``` 
    
9.  Convert a string to a boolean:

    ```py
    my_bool = my_string.lower() in ['true', 't', 'yes', 'y', '1']
    ``` 
    
10.  Remove duplicates from a list while preserving order
	   ```py
	   seen = set()
	   unique_list = [x for x in my_list if x not in seen and not seen.add(x)]
	   ```
    
11.  Convert a list of strings to a single string:

	   ```py
	   my_string = ' '.join(my_list)
	   ``` 
    
12.  Generate a random number:

	   ```py
	   import random
	   random_number = random.randint(min_value, max_value)
	   ``` 
    
13.  Get the size of a file:

	   ```py
	   file_size = os.path.getsize(file_path)
	   ``` 
    
14.  Replace all occurrences of a substring in a string:

	   ```py
	   new_string = my_string.replace(substring, new_substring)
	   ``` 
    
15.  Get the last N elements of a list:

	   ```py
	   last_n_elements = my_list[-n:]
	   ``` 
    
16.  Filter a list based on a condition:

	   ```py
	   filtered_list = [x for x in my_list if condition(x)]
	   ``` 
    
17.  Check if a file exists:

	   ```py
	   if os.path.isfile(file_path):
	       print("File exists")
	   ``` 
    
18.  Read a file line by line:

	   ```py
	   with open(file_path) as f:
	       for line in f:
	           print(line)
	   ``` 
    
19.  Get the current working directory:

	   ```py
	   current_directory = os.getcwd()
	   ``` 
    
20.  Create a directory if it does not exist:
    
	   ```py
	   if not os.path.exists(directory_path):
	       os.makedirs(directory_path)
	   ```

1.  Creating a dictionary from two lists:

    ```py
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    my_dict = dict(zip(keys, values))
    ``` 
    
2.  Checking if a file exists:

    ```py
    import os
    if os.path.exists('/path/to/file.txt'):
        # do something
    ``` 
    
3.  Getting the current date and time:

    ```py
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ``` 
    
4.  Reversing a string:

    ```py
    my_string = "Hello, world!"
    reversed_string = my_string[::-1]
    ``` 
    
5.  Generating a random number:

    ```py
    import random
    my_number = random.randint(1, 100)
    ``` 
    
6.  Converting a string to a list:

    ```py
    my_string = "apple,banana,orange"
    my_list = my_string.split(",")
    ``` 
    
7.  Sorting a list of dictionaries by a specific key:

    ```py
    my_list = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 20}]
    sorted_list = sorted(my_list, key=lambda x: x['age'])
    ``` 
    
8.  Removing duplicates from a list:

    ```py
    my_list = [1, 2, 3, 2, 1]
    my_list = list(set(my_list))
    ``` 
    
9.  Checking if a string contains a substring:

    ```py
    my_string = "Hello, world!"
    if "world" in my_string:
        # do something
    ``` 
    
10.  Joining a list of strings into a single string:

	   ```py
	   my_list = ['apple', 'banana', 'orange']
	   my_string = ', '.join(my_list)
	   ```

That's all for today! Cheers!!!

You can also read my other posts in python:
1. [Machine Learning: Multiclass Classification Template for any Classification Dataset](https://shantoroy.com/machine-learning/machine-learning-multiclass-classification-template/)
2. [Cyber Security (in Python) Books, Codes, and other Resource Collection available on GitHub](https://shantoroy.com/security/python-for-cybersecurity-books-and-codes/)
3. [Write a Reverse Proxy Server in Python: Part 1 (Reverse Proxy Server)](https://shantoroy.com/network/write-a-reverse-proxy-server-in-python/)
4. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNTI4OTU2ODIsODIzOTU3MDU5XX0=
-->