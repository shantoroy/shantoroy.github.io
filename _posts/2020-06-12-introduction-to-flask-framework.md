---
layout: single
title: "Create your first Flask (Python) `Hello World` App in 5 minutes"
header:
  image: "https://live.staticflickr.com/65535/49993827911_e3d3c300d6_c.jpg"
  teaser: "https://live.staticflickr.com/65535/49993827911_e3d3c300d6_c.jpg"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Flask
  - Web Application
  - Framework
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

In this post, we will install Flask and will create our first app.

## Prepare Environment
### Create Directory
First, let's create a different directory for our django project.

```bash
$ mkdir first_app
$ cd first_app/
```

### Create and Activate Virtual Environment
Now, let's create a virtual environment using Miniconda/Anaconda. You can also use `pipenv`

If you do not know, how to install Miniconda/Anaconda, visit this post first:

[Data Science Work Environment setup on Linux/Mac](https://shantoroy.com/data%20science/data-science-environment-python-r-julia/)


```bash
$ conda create --name flask python=3.6
$ source activate flask
```
Now, let's install `flask` using `pip`. 
```
$ pip install flask
```


## Create First App
Just copy the first code from [Flask Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/), and paste in a file. Here, I create the file named `hello.py`, and paste the following code.
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```
Now, let's run the following two commands and the app will be launched. N.B. use `set` instead of `export` if you are using Windows opearating system.
```
$ export FLASK_APP=hello.py
$ flask run

* Serving Flask app "hello.py"
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [01/Jul/2020 12:39:56] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Jul/2020 12:39:57] "GET /favicon.ico HTTP/1.1" 404 -
```


Now open your browser and paste `http://127.0.0.1:5000/` in the URL bar. You will see the `hello world` message printed on the window. 

Note that, you can use HTML tags within the code. For example, if you want the message to be appeared as `H1` tag, change the code as follows:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'
```

Now, run the flask again and reload the browser page.
```bash
$ flask run
```





<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYzNjkzNTU4OF19
-->