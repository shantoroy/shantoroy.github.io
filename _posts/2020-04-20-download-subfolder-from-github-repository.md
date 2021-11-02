---
layout: single
title: "Download a Subfolder or File from a Github Repository"
header:
  image: "https://live.staticflickr.com/65535/51648277541_7c90766f9e_b.jpg"
  teaser: "https://live.staticflickr.com/65535/51648277541_7c90766f9e_b.jpg"
categories:
  - Github
tags:
  - Github
  - Tutorial
  - Tips and Tricks
  - Git
  - directory
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



Sometimes we need to download a directory/subdirectory of a [Github](https://www.github.com) repository. In that case, let's follow the easiest way:

## Download a Directory
### Using Command Line
1. Find the url of the directory. It can be something like `https://github.com/susanli2016/Machine-Learning-with-Python/tree/master/data`.
2. Now, replace the `tree/master` with `trunk`
	```
	https://github.com/susanli2016/Machine-Learning-with-Python/tree/master/data
	```
	$\rightarrow$
	```
	https://github.com/susanli2016/Machine-Learning-with-Python/trunk/data
	```
3. Now download the folder using [SVN](https://www.perforce.com/blog/vcs/svn-commands-cheat-sheet)

	```sh
	$ svn checkout https://github.com/susanli2016/Machine-Learning-with-Python/trunk/data
	```
### Using Online Tools
Checkout the following online tools
1. [Download Directory](https://download-directory.github.io/)
2. [DownGit](https://downgit.github.io/)
3. [GitZip](http://kinolien.github.io/gitzip)

## Download a Single File
The simplest way is
1. Get the URL
2. Choose the `raw` view
3. And save the file by right clicking on the mouse and selecting `save as`

Or using the command line, use `wget`
```sh
$ wget
https://raw.githubusercontent.com/jquery/jquery/master/src/ajax.js
```

Or you can use the above-mentioned online tools to download an individual file.

That's it for today! Cheers!!!

## References
1. https://stackoverflow.com/questions/7106012/download-a-single-folder-or-directory-from-a-github-repo

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAxNDQ1MTEwNV19
-->