---
layout: single
title: "Common Files Typically Included in Python Projects: A Comprehensive Guide"
excerpt: "When you start a new Python project, you'll quickly realize that it includes many different files, each with its own purpose. Understanding these files and their roles is critical to the success of your project. This post goes over the most common files that you're likely to encounter in Python projects, including requirements.txt, setup.py, config.py, LICENSE, dockerfile, etc. and more. By the end of this guide, you'll have a better understanding of what each file does and how it fits into your Python project."
seo_title: "Common Files Typically Included in Python Projects: A Comprehensive Guide"
seo_description: "Python projects often include a variety of files that are critical to their functioning. In this blog post, we explore the most common files you'll encounter in Python projects, such as requirements.txt, setup.py, config.py, LICENSE, dockerfile, etc. and their significance."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - Python
tags:
  - python
  - requirements.txt
  - unittest
  - git
  - docker
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Python is a popular programming language used by developers for building different types of applications such as web applications, desktop applications, and mobile applications. 

When starting a new Python project, it's important to have certain files in place to ensure that the project is organized, maintainable, and can be easily shared with others.

## Common Files
Here are some common files that are typically included in a Python project:

### `README.md`
 A file containing information about the project and its usage. If placed in GitHub or GitLab, it's usually the first file someone will see when visiting the project's repository.

This file contains information about the project such as its purpose, installation instructions, usage instructions, and other relevant details. An example may look like as follows:

```markdown
# Project Name

This project does X, Y, and Z.

## Installation

To install the project, do the following:

1. Clone the repository using `git clone https://<github_URL>`
2. Install the dependencies using `pip install -r requirements.txt`
3. Run the project using `python app.py`
```

    
###  `requirements.txt`
A file listing all the dependencies required for the project to run. This file is often used in combination with package managers like pip.

This file contains a list of dependencies and their versions that the project requires to run. You can generate this file using the `pip freeze > requirements.txt` command. A typical file looks like as follows.

```
click==8.1.3
Flask==2.2.3
Flask-MQTT==1.1.1
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
paho-mqtt==1.6.1
postgres==4.0
psycopg2-binary==2.9.6
psycopg2-pool==1.1
PyJWT==2.6.0
pytz==2023.3
Werkzeug==2.2.3
```
	
   This example is based on a Flask-based API for MQTT device authentication and data response. 

###  `setup.py`
A file used to define the project, its metadata, and dependencies for building and distributing the project. Example contents may include:

```py
from setuptools import setup, find_packages

setup(
    name='<project_name>',
    version='v1',
    author='<your_name>',
    author_email='<your_email>@example.com',
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0.2',
        'SQLAlchemy>=1.4.23',
        'PyJWT>=2.0.0',
        'psycopg2-pool>=1.0',
        'pytest>=6.2.5',
    ],
)
```
    
###  `LICENSE`
A file specifying the license under which the project is distributed. An example file may include the following contents:
```
MIT License

Copyright (c) [year] [author]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

	In this example, the license is the MIT License, which is a permissive license that allows others to use, copy, modify, and distribute the software. The license also includes a warranty disclaimer and liability limitation clause.
    
###  `main.py`
A file containing the main code for the project. Or if it's an app, the file name could be `app.py`. A typical structure is as follows:
```py
import custom_class

def main():
	custom_obj = custom_class()
    # Your code here...

if __name__ == '__main__':
    main()
```
    
### `config.py`
A file containing configuration variables for the project. A typical file looks like as follows:
```py
import os

# Database configuration
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'mydatabase')
DB_USER = os.getenv('DB_USER', 'myuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'mypassword')

# API keys
API_KEY_1 = 'myapikey1'
API_KEY_2 = os.getenv('API_KEY_2')

# Other settings
DEBUG = True
SECRET_KEY = 'mysupersecretkey'
```
	The reason for using this file is to hide sensitive information from the scripts and it is a good practice to use this file.
    
###  `utils.py`
A file containing utility functions (or classes) that can be used across the project. For example,
```py
import hashlib

def hash_password(password):
    """Hashes a password using the SHA-256 algorithm."""
    salt = 'mysalt'  # TODO: Generate a unique salt for each user
    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    return hashlib.sha256(password + salt).hexdigest()

class Timer:
    """A simple timer that can be used to measure the time taken by a block of code."""

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f'Time taken: {self.elapsed_time:.2f} seconds')
```
    
11.  `test/`: A directory containing unit tests for the project. For example, a unit test for a function could be as follows:
	```py
	import unittest

	# example function
	def add_numbers(x, y):
	    """Adds two numbers together."""
	    return x + y

	class TestAddNumbers(unittest.TestCase):

	    def test_add_numbers(self):
	        self.assertEqual(add_numbers(2, 3), 5)
	        self.assertEqual(add_numbers(-1, 1), 0)
	        self.assertEqual(add_numbers(0, 0), 0)

	    def test_add_numbers_type_error(self):
	        with self.assertRaises(TypeError):
	            add_numbers('2', 3)

	if __name__ == '__main__':
	    unittest.main()
	```
    
12.  `.gitignore`: A file specifying files and directories that should be ignored by Git. 

	Example contents
	```git
	venv/
	__pycache__/
	.DS_Store
	**/__pycache__/
	.*
	!/.gitignore
	```
13.  `docs/`: A directory containing documentation for the project.
    
14.  `scripts/`: A directory containing scripts for running common tasks such as data processing, model training, or deploying the application.
   
    
15.  `dockerfile`: A file defining the containerization of the application. An example docker file for running an API looks like as follows:

		```docker
		# Use an official Python runtime as a parent image
		FROM python:3.9-slim-buster

		# Set the working directory to /app
		WORKDIR /app

		# Copy the current directory contents into the container at /app
		COPY . /app

		# Install any needed packages specified in requirements.txt
		RUN pip install --trusted-host pypi.python.org -r requirements.txt

		# Make port 5000 available to the world outside this container
		EXPOSE 7000

		# Define environment variables
		ENV FLASK_APP=app.py
		ENV FLASK_RUN_HOST=0.0.0.0

		# Run the command to start the API
		CMD ["flask", "run"]

		# example usage
		# docker build -t my-api .
		# docker run -p 7000:7000 my-api
		```

So, that's all for today!

I hope, you get the idea of which files need to be put and how to organize files for your next python projects.

Cheers!



## Python-related Other Posts
### General


1. [Add Custom Headers to Python Files in Seconds using VSCode Editor](https://shantoroy.com/tutorial/add-header-to-python-file-vscode.md/)
2. [Python ZeroMQ Module: A Simple Publisher-Subscriber Chat Application](https://shantoroy.com/python/simple-chat-application-using-python-zeromq/)
3. [Python Logging: Basic Tutorial and Template](https://shantoroy.com/python/python-logging-module-basic-tutorial-and-template/)
4. [Creating and Reading QR Code in Python: A Simple Python Class using  `qrcode`  and  `opencv`  module](https://shantoroy.com/python/creating-and-reading-qrcode-in-python/)
5. [A Curated list of Python Cheatsheets Collections](https://shantoroy.com/python/best-python-cheatsheet-collection/)
6. [Useful Functions of Python Itertools Module](https://shantoroy.com/python/python-itertools-useful-functions/)
7. [How to Convert Python Matplotlib Plots to Latex Plots (Easiest Way) for Academic Papers](https://shantoroy.com/latex/convert-matplotlib-plot-to-latex-plot/)


### Data Science/ML
1. [Machine Learning: Multiclass Classification Template for any Classification Dataset](https://shantoroy.com/machine-learning/machine-learning-multiclass-classification-template/)
2. [How to Plot Group-plots in Python](https://shantoroy.com/python/groupplot-in-python-pandas/)
3. [Creating Bar Charts using Python Matplotlib](https://shantoroy.com/python/python-bar-chart-using-matplotlib/)
4. [Collection of  `Data Science in Python`  Posts in my Blog](https://shantoroy.com/python/data-science-in-python-posts-in-my-blog/)
5. [Matrix Operations in Python Numpy](https://shantoroy.com/python/matrix-operations-in-python/)
6. [Introduction to Deep Learning in Python (Keras and Tensorflow) using the MNIST Dataset](https://shantoroy.com/machine-learning/intro-to-deep-learning-with-mnist-data-prediction/)
7. [How to Draw Multiple Axis in Matplotlib with different Scales (Value Range)](https://shantoroy.com/python/draw-multiple-axis-in-matplotlib-with-different-scales/)
8. [Introduction to Reinforcement Learning (Part 03: Q-Learning in Python)](https://shantoroy.com/reinforcement-learning/intro-to-reinforcement-learning-part3-RL-types/)
9. [Data Science Work Environment setup on Linux/Mac](https://shantoroy.com/data%20science/data-science-environment-python-r-julia/)


### Security
1. [Cyber Security (in Python) Books, Codes, and other Resource Collection available on GitHub](https://shantoroy.com/security/python-for-cybersecurity-books-and-codes/)
2. [Write a Simple Worm (Malware) in Python](https://shantoroy.com/security/write-a-worm-malware-in-python/)
3. [Write A Basic Keylogger in Python](https://shantoroy.com/security/a-simple-keylogger-in-python/)
4. [Symmetric and Asymmetric Key Cryptography Concept in Python](https://shantoroy.com/security/symmetric-public-key-cryptography-in-python/)
5. [Write a Simple Virus in Python](https://shantoroy.com/security/write-a-virus-in-python/)
6. [Password Cracking through Dictionary Attack in Python](https://shantoroy.com/security/password-cracking-through-dictionary-attack-in-python/)
7. [Write a Simple Backdoor in Python](https://shantoroy.com/security/simple-backdoor-using-python/)


### Dev/Ops/SRE
1. [Write a Reverse Proxy Server in Python: Part 1 (Reverse Proxy Server)](https://shantoroy.com/network/write-a-reverse-proxy-server-in-python/)
2. [How to Write a RESTful API using Python Flask to fetch data from PostgreSQL Database](https://shantoroy.com/python/python-api-using-flask-to-run-postgresql-query/)
3. [Create your first Flask (Python)  `Hello World`  App in 5 minutes](https://shantoroy.com/python/introduction-to-flask-framework/)
4. [Introduction to django with Creating a Simple  `helloworld`  App](https://shantoroy.com/python/introduction-to-django/)


### Automation
1. [How to write a Twitter Data Scrapper in Python](https://shantoroy.com/python/build-a-twitter-scrapper-in-python/) 
2. [Cloning an entire Website and Running in the Localhost](https://shantoroy.com/security/website-cloning-and-rerunning-in-localhost/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk1OTg3MDIxMV19
-->