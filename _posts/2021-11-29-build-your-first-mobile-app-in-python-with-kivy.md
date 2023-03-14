---
layout: single
title: "Build Your First Mobile App in Python with Kivy: A Simple Hello World Program"
excerpt:  "Building a mobile app in Python has never been easier with the Kivy framework. This open-source Python library allows developers to create beautiful and functional mobile apps for Android and iOS platforms. In this tutorial, I will walk us through building our first mobile app with Kivy by creating a simple Hello World program."
seo_title:  "Build Your First Mobile App in Python with Kivy: A Step-by-Step Guide"
seo_description:  "Ready to create your first mobile app with Python? Check out this step-by-step guide to building a "Hello World" app with the Kivy framework. Learn how to design and code a simple app that runs on Android and iOS devices."
header:
  image: "https://live.staticflickr.com/65535/51713840278_c17951a974_o.png"
  teaser: "https://live.staticflickr.com/65535/51713840278_c17951a974_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Mobile App
  - Kivy
  - Android
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


If you know python and are interested in building mobile applications, but do not have knowledge about Android or IOS application development, this post is for you.

`kivy` is an excellent mobile application development platform for python programmers. In this tutorial, we will learn to build our first mobile application by printing out `Hello World` on our first application, which is written in python with `kivy` module.

## Install `kivy`
### Creating Virtual Environment
Let's first create a virtual environment for `kivy` using `conda`. If you do not know, how to setup conda for your machine, check out my other tutorial.

[# Data Science Work Environment setup on Linux/Mac](https://shantoroy.com/data%20science/data-science-environment-python-r-julia/)

Now, let's create an enviornment named `kivy` (or whatever name you prefer) based on python `3.7` (or whatever version you prefer).
```bash
$ conda create --name kivy python=3.7
```

### Installing Dependencies
We have to install the following dependencies for `macOS`.
```bash
$ brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
```
or for `Ubuntu`
```bash
sudo apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev
```
or for fedora-alike OS
```bash
sudo dnf install -y ffmpeg-libs SDL2-devel SDL2_image-devel SDL2_mixer-devel \
SDL2_ttf-devel portmidi-devel libavdevice libavc1394-devel zlibrary-devel ccache \
mesa-libGL mesa-libGL-devel
```

### Install Kivy
1. **Conda**
Now, let's install `kivy` using conda
	```bash
	$ conda install kivy -c conda-forge
	```


2. **Pip Wheel**
or you can install `kivy` using `pip`
	```bash
	$ python -m pip install kivy
	```

	stable version
	```bash
	$ python -m pip install kivy[base] kivy_examples --no-binary kivy
	```
	latest version
	```bash
	$ python -m pip install "kivy[base] @ https://github.com/kivy/kivy/archive/master.zip"
	```





## Creating First App
Now let's follow the steps to build our first app
### Step-by-step Guide
First, we will import the `kivy` module. We will also import the `App` class that features all the necessary underlying work for our app. And, because we will only print in a label, we will import `Label`. For other features (e.g., button), we can import those manually.
```python
import kivy
from kivy.app import App
from kivy.uix.label import Label			
```

Now, let's create a class that inherits properties from the `App` class. We need to have `build` method that returns whatever we want to show while running the program. In this instance, we create a label with our `hello world!` text.
```python
# Defining a class
class HelloWorldKivyApp(App):
	# our primary widget
	def build(self):
		# Label with our text
		return Label(text ="Hello World!")		
```

Now, we can run the program using the inherited method `run()`.
```python
# running the app
if __name__=="__main__":
	HelloWorldKivyApp().run()			
```

### Full Code
Here' is the full code:
```python
import kivy
from kivy.app import App
from kivy.uix.label import Label

# Defining a class
class HelloWorldKivyApp(App):
	# our primary widget
	def build(self):
		# Label with our text
		return Label(text ="Hello World!")		


# running the app
if __name__=="__main__":
	HelloWorldKivyApp().run()			
```

create a new file 
```bash
$ nano myfirstapp.py
```
copy and paste the above program and run
```bash
$ python myfirstapp.py
```

You will see the following output:

<figure>
  <a href="https://live.staticflickr.com/65535/51713574716_f46e93a1fb_o.png"><img src="https://live.staticflickr.com/65535/51713574716_f46e93a1fb_o.png"></a>
</figure>
<br/>




## References
1. [Getting StartedGetting Started »  Installing Kivy](https://kivy.org/doc/stable/gettingstarted/installation.html#kivy-source-install)
2. [Kivy Installation on Linux](https://kivy.org/doc/stable/installation/installation-linux.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MTAxMTAyNDksNzYwNTg3MzcyLDE5ND
A0OTE4MjJdfQ==
-->