---
layout: single
title: "Python Logging: Basic Tutorial and Template"
header:
  image: "https://live.staticflickr.com/65535/52691302312_5b85827f90_o.png"
  teaser: "https://live.staticflickr.com/65535/52691302312_5b85827f90_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Logging
  - Debug
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "Logging is a critical component of any Python project, and here, I write a simple tutorial and example templates to use that will help you to have a head start. With practical examples and insights, you'll learn about implementing effective logging in your Python programs or applications."
---


The python `logging` module enables developers to track and troubleshoot program issues. When developing a software application, it's essential to have a way to track issues and errors that may take place throughout the application development procedure. 

The `logging` module provides a way to record events and messages from a particular code, allowing us to track down issues and troubleshoot problems as they arise.

In summary, the `logging` module aids the following:

-   Recording events and messages from code
-   Setting different levels of logging $\rightarrow$ DEBUG, INFO, WARNING, and ERROR
-   Customizing the format of log messages
-   Stores log messages to a file, console, or network socket


## Basic Logging with `basicConfig()`
The simplest way to use the logging module is to call the `basicConfig()` function. Here's an example template we can use in a code:

```python
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
```

This configurations sets the logging level to `DEBUG`, which means that all log messages at the `DEBUG` level or higher will be recorded. The `format` parameter specifies the predefined format of the log messages. In this example, we record the timestamp, level name, and message.

Here's how we can use different levels of log messages:
```python
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

While using the `basicConfig()` function is the simplest way to use the logging module, it has some limitations. One major issue may arise when we import another file that includes `logging.basicConfig()` as well. 

## Logging with Loggers, Handlers, and Formatters

We can use loggers, handlers, and formatters to overcome the limitations of `basicConfig()`. This allows us to separate different parts of our working code into distinct logging namespaces, direct log messages to different destinations (files), and customize the formatting of log messages.

First, we need to use the `getLogger()` function, which takes a string name as its argument:

```python
import logging
logger = logging.getLogger(__name__)
```

Plz, note that, the logger's name should match the name of the module or class it represents.

### Handlers

A handler is an object that sends log messages to a specific destination, such as a file, console, or network socket. We can use handlers to direct log messages to different destinations.

We can use `StreamHandler`, `FileHandler`, or `SocketHandler`, depending on the type of destination we want to send the log messages to. Most of the time we use `FileHandler`. For example,

```python
import  logging

file_handler = logging.FileHandler('demo_logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
```

### Formatters

A formatter is an object that specifies the format of log messages. We can use formatters to customize the format of log messages. here's an example,

```python
import logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
```

### Full Examples
Here's an example for stream handler:

```python
import logging

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)
```

An example from [Corey Schafer's Code Snippet](https://github.com/CoreyMSchafer/code_snippets/blob/master/Logging-Advanced/log-sample.py) that includes both file and stream handler:
```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('demo_logs.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
```

In this tutorial, we've explored how to use the Python `logging` module to add logging capabilities to our code. We've covered the basics of logging with `basicConfig()`, as well as the more advanced techniques of loggers, handlers, and formatters.

That's all for today! Have a good day, cheers!!! 😎
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzOTQ1NDMzNzcsLTE5ODg2ODg1NjJdfQ
==
-->