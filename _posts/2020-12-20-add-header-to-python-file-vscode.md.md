---
layout: single
title: "Add Custom Headers to Python Files in Seconds using VSCode Editor"
excerpt: "Adding custom headers to your Python files is an excellent way to provide critical information about your code, such as author name, creation date, and copyright information. But typing these headers manually in every file can be a tedious task. In this blog post, I'll show you how to add custom headers to your Python files quickly using the VSCode editor."
seo_title:  "Add Custom Headers to Python Files in Seconds using VSCode Editor"
seo_description:  "Learn how to add custom headers to your Python files in seconds using the VSCode editor. Adding headers to your code provides important information such as author name, creation date, and copyright information. Stop manually typing headers in every file and simplify the process with this quick tutorial."
header:
  image: "https://live.staticflickr.com/65535/51234195440_2488a7d7f5_w.jpg"
  teaser: "https://live.staticflickr.com/65535/51234195440_2488a7d7f5_w.jpg"
categories:
  - Tutorial
tags:
  - VSCode
  - Tutorial
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


We often need to add custom header to our code files. Here is how to add that header as a template in seconds.

## Example Code Header
Here is an example code header for python.
```python
#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   <file_name>.py
@Time    :   2021/05/16 18:38:01
@Author  :   <author_name>
@Version :   1.0
@Contact :   <author_email>
@License :   (C)Copyright 2020-2021, <author/company>
@Desc    :   <awaiting description>
'''
```

## Steps to Create User Snippet
1. Select Code $\rightarrow$ Preferences $\rightarrow$ User Snippet
<figure>
  <a href="https://live.staticflickr.com/65535/51233320303_c3d38717ab_w.jpg"><img src="https://live.staticflickr.com/65535/51233320303_c3d38717ab_w.jpg"></a>
</figure>

2. Select `python.json` from the search box

<figure>
  <a href="https://live.staticflickr.com/65535/51233876469_58081a88ca_w.jpg"><img src="https://live.staticflickr.com/65535/51233876469_58081a88ca_w.jpg"></a>
</figure>

3. Add the following to the file (Modify based on your information)

```json
{
	"HEADER":{
		"prefix": "header",
		"body": [
		"#!/usr/bin/env python",
		"# -*-coding:utf-8 -*-", 
		"'''",
		"@File    :   $TM_FILENAME",
		"@Time    :   $CURRENT_YEAR/$CURRENT_MONTH/$CURRENT_DATE $CURRENT_HOUR:$CURRENT_MINUTE:$CURRENT_SECOND",
		"@Author  :   Shanto Roy ",
		"@Version :   1.0",
		"@Contact :   sroy10@uh.edu",
		"@License :   (C)Copyright 2020-2021, Shanto Roy",
		"@Desc    :   None",
		
		"'''",
		"$0"
	],
	}
}
```

## Usage
In a python file, start typing `header` and the whole snippet will appear. Press enter and you are good to go.

<figure>
  <a href="https://live.staticflickr.com/65535/51232407132_1e82bbe26c_w.jpg"><img src="https://live.staticflickr.com/65535/51232407132_1e82bbe26c_w.jpg"></a>
</figure>

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MDM5NDQ1NSwtMTM0NTg1NDk4LDE1ND
U5NDEwMTJdfQ==
-->