---
layout: single
title: "How to git-ignore Cached Code files and all Hidden Directories Recursively in a Git Repository!"
excerpt:  "Ignoring certain files and directories in a Git repository is crucial to keep your repository clean and tidy. This post focuses on using the .gitignore file to ignore cached code files and all hidden directories recursively. By doing this, your Git repository will only contain the files that matter, and you can avoid cluttering it with files that can be generated or are irrelevant to the project."
seo_title:  "How to git-ignore Cached Code files and all Hidden Directories Recursively in a Git Repository"
seo_description:  "Learn how to ignore cached code files and all hidden directories recursively in a Git repository using the .gitignore file. Keep your repository clean and tidy by only including the files that matter, and avoid cluttering it with files that can be generated or are irrelevant to the project. This post provides a step-by-step guide to help you efficiently manage your Git repository."
header:
  image: "https://live.staticflickr.com/65535/52025139285_52e38b859f_o.png"
  teaser: "https://live.staticflickr.com/65535/52025139285_52e38b859f_o.png"
categories:
  - Git
tags:
  - Git
  - Tutorial
  - Github
  - Gitlab
  - Gitignore
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post presents a generic `.gitignore` file that ignores Cached Code files and all Hidden Directories Recursively in a Git Repository"
---


Sometimes, while coding, we forget to add a `.gitignore` file that includes list of files or directories to ignore when pushed to a remote repository. 

Then we forgetfully pushes the code and see there are unnecessary cache files or hidden directories/files present in the online repository, which causes pain for other collaborators.

If you accidentally have done so, just follow these steps, and you are good to go.

## Steps
1. Check how many hidden directories are there using the following command.
	```bash
	find . -type d -name '.[^.]*' -prune -exec echo rm -rf {} +
	```

	once you find out, and have no issue with deleting each of the listed hidden directories, remove the `echo` from the above command.
	```bash
	find . -type d -name '.[^.]*' -prune -exec rm -rf {} +
	```
	Careful if you already have a `.git` directory!

2. Delete the `__pycache__` folders from all the directories in the same way
	```bash
	find . -type d -name '__py[^.]*' -prune -exec rm -rf {} +
	```

3. Finally, create a `.gitignore` file and add the followings:
	```python
	**/__pycache__/
	.*
	!/.gitignore
	```

## Pro Tips
To avoid adding a particular named file or directory, for example., to ignore`.DS_Store` files in every subfolder for all repositories in the computer, do the following:
	```
	$ echo .DS_Store >> ~/.gitignore_global
	$ git config --global core.excludesfile ~/.gitignore_global
	```


Now, if you do `git add --all`, it will not automatically include these particular directories created again while working in the local machine.

## References
1. [How to ignore all hidden directories/files recursively in a git repository?](https://stackoverflow.com/questions/8021441/how-to-ignore-all-hidden-directories-files-recursively-in-a-git-repository)

2. [Recursively delete hidden directory & its files?](https://unix.stackexchange.com/questions/123233/recursively-delete-hidden-directory-its-files)
3. [.gitignore all the .DS_Store files in every folder and subfolder](https://stackoverflow.com/questions/18393498/gitignore-all-the-ds-store-files-in-every-folder-and-subfolder)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTUwNTM1ODcxMiwtMjAzOTkyOTE3NCwtMT
E2MTc4MDU1OCw3MjQ5MjY4XX0=
-->