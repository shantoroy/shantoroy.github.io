---
layout: single
title: "#100daysofSRE (Day 19): Simplifying Log Analysis with Linux Sed Command: Basic and Templates"
excerpt: "In site reliability engineering, log analysis is a crucial aspect of maintaining system availability and identifying potential issues. However, analyzing logs manually can be time-consuming and error-prone. In this post, we explore how to simplify log analysis with the Linux sed command. We cover the basics of the sed command and provide templates for common use cases in SRE, such as filtering logs, searching for specific patterns, and extracting relevant information."
seo_title: "Simplifying Log Analysis with Linux Sed Command: Basic and Templates"
seo_description: "In this post, we explore how to simplify log analysis with the Linux sed command. We cover the basics of the sed command and provide templates for common use cases in site reliability engineering."
header:
  image: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
  teaser: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
categories:
  - SRE
tags:
  - SRE
  - 100daysofsre
  - 100daychallenge
  - devops
  - sysadmin
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

---
Hi there!!! 👋

It's the 19th day of the `#100dayschallenge`, and today I will discuss  the usage of a popular linux command `sed` for log extraction and analysis in SRE.

Log files are critical to system and application monitoring, allowing admins to quickly identify and troubleshoot issues. However, these logs can be overwhelming and challenging to analyze, especially when dealing with large-scale environments. 

So, I have planned the  [contents for next 100 days](https://medium.com/@shantoroy/learning-about-site-reliability-engineering-with-the-100daysofsre-challenge-66380323c0d1), and I will be posting one blog post each and everyday under the hashtag  `#100daysofSRE`. ✌️

I hope you tag along and share valuable feedback as I grow my knowledge and share my findings. 🙌

## Basic Usage
### Text substitution
`sed` can be used to substitute text in a file or stream. For example, to replace all occurrences of "apple" with "orange" in a file, you can use the following command:

```bash
$ sed 's/apple/orange/g' file.txt
``` 
    
### Printing lines 
`sed` can be used to print specific lines from a file or stream. For example, to print the first 10 lines of a file, you can use the following command:

```bash
$ sed -n '1,10p' file.txt
``` 
    
###  Deleting lines
`sed` can be used to delete specific lines from a file or stream. For example, to delete all lines containing the word "apple" in a file, you can use the following command:

```bash
$ sed '/apple/d' file.txt
``` 
    
### Search and replace
`sed` can be used to search for a pattern and replace it with another string. For example, to replace all occurrences of "apple" with "orange" only on lines containing the word "fruit", you can use the following command:

```bash
$ sed '/fruit/s/apple/orange/g' file.txt
``` 
    
### Multiple commands
`sed` can be used to execute multiple commands on a file or stream. For example, to print the first 10 lines of a file and delete all lines containing the word "apple", you can use the following command:

```bash
$ sed -e '1,10p' -e '/apple/d' file.txt
```


## Utilizing `sed` to extract inf from log files

1.  Extracting specific lines from a log file:

	```bash
	$ sed -n '5,10p' log_file
	``` 

	This command will print lines 5 through 10 from the `log_file`.

2.  Removing blank lines from a log file:

	```bash
	$ sed '/^$/d' log_file
	``` 

	This command will remove all blank lines from the `log_file`.

3.  Extracting lines that match a specific pattern:

	```bash
	$ sed -n '/pattern/p' log_file
	``` 

	This command will print all lines from `log_file` that contain the specified pattern.

4.  Extracting lines that don't match a specific pattern:

	```bash
	$ sed -n '/pattern/!p' log_file
	``` 

	This command will print all lines from `log_file` that do not contain the specified pattern.

5.  Replacing a specific string in a log file:

	```bash
	$ sed 's/old_string/new_string/g' log_file
	```

	This command will replace all occurrences of `old_string` with `new_string` in the `log_file`.

6.  Extracting the last 10 lines of a log file:

	```bash
	$ sed -n '$-10,$p' log_file
	```

	This command will print the last 10 lines of the `log_file`.

7.  Extracting the first 10 lines of a log file:

	```bash
	$ sed -n '1,10p' log_file
	``` 

	This command will print the first 10 lines of the `log_file`.

8.  Extracting lines that match multiple patterns:

	```bash
	$ sed -n '/pattern1/p; /pattern2/p' log_file
	``` 

	This command will print all lines from `log_file` that contain either `pattern1` or `pattern2`.

9.  Counting the number of lines that match a pattern:

	```bash
	$ sed -n '/pattern/=' log_file | wc -l
	``` 

	This command will count the number of lines in `log_file` that contain `pattern`.

10.  Extracting lines between two patterns:

		```bash
		$ sed -n '/start_pattern/,/end_pattern/p' log_file
		```

		This command will print all lines from `log_file` that are between `start_pattern` and `end_pattern`.


## Useful Templates
1.  Using `awk` and `sed` to extract the most frequent HTTP response codes:

	```bash
	cat access.log | awk '{print $9}' | sed 's/\.[0-9]*//g' | sort | uniq -c | sort -nr | head
	``` 

	This command first extracts the HTTP response code from the log file using `awk`, then removes any decimal places using `sed`. It then sorts the codes, counts the number of occurrences of each code, and sorts them in descending order to show the most frequent ones using `sort`, `uniq`, and `head`.

2.  Using `grep`, `sed`, and `awk` to extract the top 10 IP addresses with the most requests:

	```bash
	$ cat access.log | grep -v "127.0.0.1" | awk '{print $1}' | sort | uniq -c | sort -nr | head -n 10 | sed 's/^ *//'
	``` 

	This command first removes requests from localhost using `grep`, then extracts the IP address from the log file using `awk`. It then sorts the IP addresses, counts the number of requests from each IP, and sorts them in descending order to show the top 10 using `sort`, `uniq`, and `head`. Finally, `sed` is used to remove any leading spaces.

3.  Using `sed` and `cut` to extract the top 5 most frequently requested URLs:

	```bash
	$ cat access.log | cut -d'"' -f2 | cut -d' ' -f2 | sort | uniq -c | sort -rn | head -n 5 | sed 's/^ *//'
	``` 

	This command first extracts the URLs from the log file using `cut`, then sorts them, counts the number of occurrences of each URL, and sorts them in descending order to show the top 5 using `sort`, `uniq`, and `head`. Finally, `sed` is used to remove any leading spaces.

4.  Using `sed` and `grep` to extract the number of requests by hour:

	```bash
	$ cat access.log | grep -v 'spider' | sed -e 's/\[//g' -e 's/\]//g' | cut -d: -f2 | sort | uniq -c | awk '{print $2,$1}' | sort -n
	``` 

	This command first removes requests from spiders using `grep`, then removes the square brackets around the timestamp using `sed`, and extracts the hour from the timestamp using `cut`. It then sorts the hours, counts the number of requests in each hour, and sorts them in ascending order to show the number of requests by hour using `sort`, `uniq`, `awk`, and `sort`.

5.  Using `sed` and `awk` to extract the top 5 most frequent user agents:

	```bash
	$ cat access.log | awk -F'"' '{print $6}' | sort | uniq -c | sort -rn | head -n 5 | sed 's/^ *//'
	``` 

	This command first extracts the user agents from the log file using `awk`, then sorts them, counts the number of occurrences of each user agent, and sorts them in descending order to show the top 5 using `sort`, `uniq`, and `head`. Finally, `sed` is used to remove any leading spaces.

6.  Using `sed`, `awk`, and `cut` to extract the number of requests by day:

	```bash
	$ cat access.log | awk '{print $4}' | cut -d
	```

7.  Extracting IP Addresses from Log Files
	```bash
	$ sed -nr 's/.*([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*/\1/p' access.log
	``` 

	This command extracts IP addresses from an Apache access log file using a regular expression pattern.

2.  Replacing a Specific String in a File

	```bash
	$ sed -i 's/old_string/new_string/g' file.txt
	``` 

	This command replaces all occurrences of 'old_string' with 'new_string' in the 'file.txt' file.

3.  Removing Blank Lines from a File

	```bash
	$ sed '/^$/d' file.txt
	``` 

	This command removes all blank lines from a file.

4.  Extracting Specific Lines from a File

	```bash
	$ sed -n '5,10p' file.txt
	``` 

	This command prints lines 5-10 from the 'file.txt' file.

5.  Reversing the Order of Lines in a File

	```bash
	$ sed '1!G;h;$!d' file.txt
	``` 

	This command reverses the order of lines in the 'file.txt' file.

6.  Removing Lines That Match a Pattern

	```bash
	$ sed '/pattern/d' file.txt
	``` 

	This command removes all lines that match the specified pattern from the 'file.txt' file.

7.  Searching for a Pattern in Multiple Files

	```bash
	$ grep 'pattern' *.txt | sed 's/:.*//g' | sort | uniq
	``` 

	This command searches for a pattern in all .txt files in the current directory, removes the filename from the output, sorts the output, and removes duplicate lines.

14.  Count the number of lines in a log file
		```bash
		$ sed -n '$=' logfile.txt
		```
		This command will print the number of lines in the log file `logfile.txt`.

2.  Get the date and time of the first and last log entry:

	```bash
	$ sed -n '1p;$p' logfile.txt
	```

	This command will print the first and last lines of the log file, which will contain the date and time of the corresponding log entry.

3.  Get the IP address of the client that made the most requests

	```bash
	$ sed -n '/^\[.*\]/ {print $1} | sort | uniq -c | sort -nr | head -1' logfile.txt
	```

	This command will print the IP address of the client that made the most requests. The `sed` command first extracts all lines that start with `[`, which are the lines that contain log entries. The `sort` command sorts the IP addresses in ascending order, and the `uniq -c` command counts the number of times each IP address appears. The `sort -nr` command sorts the IP addresses in descending order by the number of requests, and the `head -1` command prints the first line, which is the IP address of the client that made the most requests.

4.  Get the top 10 most popular URLs

	```bash
	$ sed -n '/^\[.*\]/ {print $2} | sort | uniq -c | sort -nr | head -10' logfile.txt
	```

	This command is similar to the previous command, but it prints the top 10 most popular URLs. The only difference is that the `sed` command is now extracting the second column, which contains the URL.

5.  Get the list of all errors

	```bash
	$ sed -n '/ERROR/p' logfile.txt
	```

	This command will print all lines in the log file that contain the word "ERROR".

6.  Get the list of all warnings

	```bash
	$ sed -n '/WARNING/p' logfile.txt
	```

	This command is similar to the previous command, but it prints all lines in the log file that contain the word "WARNING".

7.  Get the list of all successful requests

	```bash
	$ sed -n '/200 OK/p' logfile.txt
	```


	This command will print all lines in the log file that contain the status code "200 OK", which indicates a successful request.

## Concluding Remarks
In this blog post, we've explored the basics of the `sed` command and how it can extract meaningful information from log files. We've also looked at some templates that can simplify log analysis for system, application, and performance monitoring. 

## References
* [OpenAI ChatGPT](https://chat.openai.com/)
* [Google Bard](https://bard.google.com/)
* [Perplexity AI](https://www.perplexity.ai/)


___

___

Thank you for reading my blog post! 🙏

If you enjoyed it and would like to stay updated on my latest content and plans for next week, be sure to subscribe to my newsletter on Substack. 👇

Once a week, I'll be sharing the latest weekly updates on my published articles, along with other news, content and resources. Enter your email below to subscribe and join the conversation for Free! ✍️

<iframe src="https://shantoroy.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

I am also writing on Medium. You can [follow me here](https://medium.com/@shantoroy).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3OTYzOTMxNzcsNDcyOTA3NDM1XX0=
-->