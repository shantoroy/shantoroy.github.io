---
layout: single
title: "Short Introduction to Git Commands and Github for Beginners"
header:
  image: "https://live.staticflickr.com/65535/51233648279_e97dd9a2b8_w.jpg"
  teaser: "https://live.staticflickr.com/65535/51233648279_e97dd9a2b8_w.jpg"
categories:
  - github
tags:
  - Github
  - Git
  - Git Commands
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



`Git` is a popular version control tool and `Github` provides a cloud platform for storing your code, data, and history of commits (records of addition, modification, or deletion).

In this short tutorial, we will take a look at the necessary `git commands` that are enough to know for a beginner user (I will skip some basic items that are not necessary at least for the very first steps).

A github repository typically looks like
```
https://github.com/<user_name>/<project_name>.git
```

For example, if I create a repository named `hello_world`, and my user name is `shantoroy`, the repository should look like
```
https://github.com/shantoroy/hello_world.git
```

## Prerequisite
###  Installation
* Ubuntu: 
	```
	$ sudo apt update
	$ sudo apt install git
	```
* Red Hat/Cent OS
	```
	$ sudo yum upgrade
	$ sudo yum install git
	```
* macOS (using Homebrew)
	```
	$ brew install git
	```
	if Homebrew is not installed, install it using the following command
	```
	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	```
	or 
	```
	$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
	$ brew doctor
	```
* Windows installation: 
Install from the [git for windows - link](https://gitforwindows.org/). It provides both command-line tool and Graphical User Interface.

### Create a GitHub Account
Create an account in [Github](https://github.com/). If you have accounts in social medias (e.g., Facebook or Instagram), you actually know how to open an account anywhere. :zany_face:

### Initial Configuration
In your local machine, you need to configure your `username` and `email` using the following commands. The user name and email refers to your Github account.

```console
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

Check all of your settings 
```
$ git config --list
```

or individually (e.g., to check the user name),

```console
$ git config user.name
```

Now, you are all setup. Let's create a new repository and start using Github using the git commands.

## New Repository
A repository typically contains all commits (records of file addition, modification, or deletion) in a particular local machine directory. What you are doing with Github is, keeping the same copy in a cloud storage where you have more tools for better user experience.

Now, let's create a repository in Github, create a local directory where we will keep our files, and then sync the directory in the Github repository.

### Create a Repository in Github
* Click on `Create a repository` option which can be found by clicking on the `+` sign from the right top corner of your github homepage.
<figure>
  <a href="https://live.staticflickr.com/65535/51232116102_5bdf10f7ef_w.jpg"><img src="https://live.staticflickr.com/65535/51232116102_5bdf10f7ef_w.jpg"></a>
</figure>

* Write your repository name (does not need to be the same as your directory name you are using in your local machine). Then select `public` or `private` based on what you want (you can change later). Now, click on the green button `Create repository`.
<figure>
  <a href="https://live.staticflickr.com/65535/51233030128_008d10a5f2_w.jpg"><img src="https://live.staticflickr.com/65535/51233030128_008d10a5f2_w.jpg"></a>
</figure>

* The basic commands are suggested here that we are going to use in our local machine.

<figure>
  <a href="https://live.staticflickr.com/65535/51232820531_20178f3e7e_w.jpg"><img src="https://live.staticflickr.com/65535/51232820531_20178f3e7e_w.jpg"></a>
</figure>


## Local Machine
1. Create a directory (does not need to be same as the online repository name)
	```sh
	$ mkdir hello_world
	```
2. Go to the directory
	```sh
	$ cd hello_world
	```
3. Initialize your git repository (initializing will add basic hidden config files inside the directory)
	```sh
	$ git init
	```
	the output will look like
	```
	Initialized empty Git repository in /Users/roy/github/github_mrx/hello_world/.git/
	```
4. Create a new file(s) and write something, for example we will write "hello" in a file named `test.txt`
	```sh
	$ echo "hello" > test.txt
	```
5. Check status
	```sh
	$ git status
	```
	the output will look like
	```
	On branch master

	No commits yet

	Untracked files:
	  (use "git add <file>..." to include in what will be committed)
			test.txt

	nothing added to commit but untracked files present (use "git add" to track)
	```
	the output says you have added a file which is yet to be added and committed (added as a record).
6. Add file to a `commit` (record history)
	```sh
	$ git add test.txt
	```
	you can individually add a file(s) to a commit or the whole directory at once. in that case use 
	```sh
	$ git add .
	```
	or 
	```sh
	$ git add --all
	```
7. Commit (add changes to the record)
	```sh
	$ git commit -m "add your message"
	```
	for example, we can write like
	```sh
	$ git commit -m "file: added test.txt"
	```
	point is write a message that can be tracked back later what you have done on this commit (with time). After committing you can check the status again to be sure if the right file(s) has been committed. The output should look like

	```
	On branch master
	nothing to commit, working tree clean
	```

8. Now we will add our remote repository address in the local git configuration. The command has already been suggested after the completion of online repository creation (see the last figure)
	```sh
	$ git remote add origin https://github.com/shantoroy/hello_world.git
	```

9. The final step is to push the commit to the online repository (sync local directory with GitHub)
		
	```sh
	$ git push origin master
	```
	Enter your username and password, and you are all done. Just reload the page again and you will see your file in the Github repo.

## Notes
* Step no. 3 and 8 in local machine is only required for the first time before you push something to the online repository. Next time just do step 6, 7, and 9 after you create/add file(s) in the local directory.
`git add => git commit => git push`
* If you made some changes in the Github using Github editor, you can then update your local directory (it is called `git pull`) using the command
	```
	$ git pull origin master
	```
* You will need username and password when you enter the `git push` command. If you want to avoid entering username and password each time you push, you should add SSH key (I will describe that process in a seperate post).






<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcxOTY5NjAzNCwzNzIxMzQ4MTNdfQ==
-->