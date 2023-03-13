---
layout: single
title: "Cloning an entire Website and Running in the Localhost"
excerpt:  "Cloning an entire website is a great way to have a backup copy or to test new features and modifications before deploying them on the live site. In this blog post, I will share how to simply clone a website and run it in the localhost environment, step-by-step."
seo_title:  Your  meta  title  
seo_description:  Your  meta  description
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/51895732364_0b8a245ce8_o.png"
categories:
  - Security
tags:
  - Python
  - Tutorial
  - HTTrack
  - pywebcopy
  - docker
  - container
  - website cloning
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post explains how to clone a website and then run in a docker container for testing and learning purpose"
---

Sometimes, we need to copy a website for different types of testing purposes. In this tutorial, we will learn how to clone a website and then run that site on localhost.

## Cloning a Website
### Using Python
The `pywebcopy` module is a popular one to download a website or a particular webpage. It crawls through all the pages and then save the webpages in a target directory.
```python
from pywebcopy import save_website
import sys

kwargs = {'project_name': 'site-name'}

save_website(
    url='http://test-site.com',
    project_folder='test-site_folder_path',
    **kwargs
)
```

If you want to have input from the terminal while running the code, just use `sys` module to receive target arguments from the terminal.
```python
from pywebcopy import save_website
import sys

kwargs = {'project_name': 'some-fancy-name'}

save_website(
    url=str(sys.argv[1]),
    project_folder=str(sys.argv[2]),
    **kwargs
)
```

```bash
$ python clone.py "<target_website_name>" "<target_download_path>"
```

### Using HTTrack
HTTrack is a commercial website cloning tool and widely used by people. It also has a free version. Here, I am using the free version.

First install HTTrack in your operating system. You can download the GUI version of the app. Or, you can use command-line for installing it in mac.
```bash
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 2> /dev/null
$ brew install httrack
```

or in Ubuntu
```bash
$ sudo apt-get install httrack
```

Now, clone a website using the following command or following instructions in the GUI app. 
```bash
$ httrack <target_website_name> -O <target_download_path>
```


## Hosting the Website in Local Machine
Let's create the `Dockerfile` in the downloaded website folder and import a lightweight web server:
```docker
FROM nginx
COPY . /usr/share/nginx/html
```

Now, let's build and run the docker container. Just replace the `<target_name>` and `<target_folder_path>` with the name you want to set on the container and the directory path you cloned the website.
```bash
$ docker build -t <target_name> <target_folder_path>
$ docker run -it -d -p 8080:80 <target_name>
```

Now, open the browser and enter `http://localhost:8080/` in the url bar to view the downloaded site running in the localhost.

When done, just use `docker stop` to stop the container. You can find the container ID using the command `docker ps`.
```bash
$ docker ps -a -f status=running
$ docker stop -t 60 <CONTAINER_ID>
```

That's all! Cheers!!!
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzU3MTE1NTA3LDE3NjU3NTczMDRdfQ==
-->