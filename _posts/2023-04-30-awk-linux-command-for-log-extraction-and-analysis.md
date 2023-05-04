---
layout: single
title: "#100daysofSRE (Day 20): Simplifying Log Analysis with Linux `awk` Command: Basic and Templates"
excerpt: "`awk` is a versatile tool that can be used to search, filter, and manipulate text files, making it a go-to tool for site reliability engineers. In this blog post, we'll cover the basics of `awk` and provide templates to make log analysis easier and more efficient. Let's not let log analysis be a time-consuming chore - let `awk` do the heavy lifting for you."
seo_title: "Simplifying Log Analysis with Linux `awk` Command: Basic and Templates"
seo_description: "Learn how to simplify log analysis with the powerful `awk` command in Linux. In this blog post, we'll cover the basics of `awk` and provide templates to make log analysis easier and more efficient for sysadmins, devops, and site reliability engineers."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
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

It's the 20th day of the `#100dayschallenge`, and today I will discuss  the linux `awk` command for log extraction and analysis in SRE.

Log files are a critical source of information for monitoring and troubleshooting these systems. However, analyzing and extracting useful information from these logs can be a challenging and time-consuming task. This is where "awk" comes in handy. With its powerful text processing capabilities, "awk" can help you filter, extract, and manipulate log data to identify patterns, troubleshoot issues, and optimize system performance.

So, I have planned the  [contents for next 100 days](https://medium.com/@shantoroy/learning-about-site-reliability-engineering-with-the-100daysofsre-challenge-66380323c0d1), and I will be posting one blog post each and everyday under the hashtag  `#100daysofSRE`. ✌️

I hope you tag along and share valuable feedback as I grow my knowledge and share my findings. 🙌

## Basic Usage
1.  Print a specific column of a file: Use awk to print a specific column of a file. For example, to print the second column of a space-separated file, use the following command
	```bash
	$ awk '{print $2}' file.txt
	```
2.  Print lines that match a specific pattern: Use awk to print only the lines that match a specific pattern. For example, to print only the lines that contain the word "error"
	```bash
	$ awk '/error/ {print}' file.txt
	```
3.  Print lines that do not match a specific pattern: Use awk to print only the lines that do not match a specific pattern. For example, to print only the lines that do not contain the word "error" 
	```bash
	$ awk '!/error/ {print}' file.txt
	```
4.  Sum a specific file column: Use awk to sum a specific file column. For example, to sum the values in the third column of a space-separated file
	```bash
	$ awk '{sum += $3} END {print sum}' file.txt.
	```
5.  Compute the average of a specific file column: Use awk to compute the average of a specific file column. For example, to compute the average values in the third column of a space-separated file
	```bash
	$ awk '{sum += $3; n++} END {print sum / n}' file.txt
	```
6.  Count the number of lines in a file: Use awk to count the number of lines in a file. For example, to count the number of lines in a file
	```bash
	$ awk 'END {print NR}' file.txt
	```
7.  Extract a specific range of lines from a file: Use awk to extract a specific range of lines. For example, to extract lines 10 to 20 from a file
	```bash
	$ awk 'NR>=10 && NR<=20 {print}' file.txt
	```
8.  Print the longest line in a file: Use awk to print the longest line in a file. For example, to print the longest line in a file
	```bash
	$ awk '{ if (length > max) {max = length; longest = $0}} END {print longest}' file.txt
	```
9.  Merge two files based on a common field: Use awk to merge two files based on a common field. For example, to merge two space-separated files based on the common field in the first column
	```bash
	$  awk 'FNR==NR {a[$1]=$2; next} {print $0, a[$1]}' file1.txt file2.txt
	```
10.  Replace a specific field in a file: Use awk to replace a specific field in a file. For example, to replace the third field in a space-separated file with a new value
		```bash
		$ awk '{$3="new_value"} {print}' file.txt
		```

## Log extraction and Analysis
1.  Extracting a specific field from a log file:

	```bash
	$ awk '{print $1}' /var/log/syslog
	``` 

This command prints the first field of each line in the syslog file.

2.  Filtering out specific lines from a log file:

	```bash
	$ awk '!/error/' /var/log/syslog
	``` 

This command prints all lines from the syslog file except those that contain the word "error".

3.  Counting the number of occurrences of a specific pattern in a log file:

	```bash
	$ awk '/error/{count++} END{print count}' /var/log/syslog
	``` 

This command counts the number of lines in the syslog file that contain the word "error".

4.  Summing a specific field in a log file:

	```bash
	$ awk '{sum+=$1} END{print sum}' /var/log/syslog
	``` 

This command sums up the first field of each line in the syslog file and prints the total.

5.  Filtering based on a range of values:

	```bash
	$ awk '$1 >= 100 && $1 <= 200 {print}' /var/log/syslog
	``` 

This command prints all lines from the syslog file where the first field is between 100 and 200.

6.  Formatting output:

	```bash
	$ awk '{printf "IP Address: %s, Port: %s\n", $1, $2}' /var/log/apache/access.log
	``` 

This command prints the IP address and port number from the Apache access log file in a formatted way.

7.  Calculating the average of a field:

	```bash
	$ awk '{sum+=$1} END{print sum/NR}' /var/log/syslog
	``` 

This command calculates the average of the first field in the syslog file.

8.  Sorting based on a specific field:

	```bash
	$ awk '{print $2, $1}' /var/log/auth.log | sort
	``` 

This command prints the second and first fields of each line in the auth log file and sorts them alphabetically by the second field.

9.  Joining log files based on a common field:

	```bash
	$ awk 'NR==FNR{a[$1]=$2 FS $3; next}{print $0, a[$1]}' file1 file2
	``` 

This command joins two log files based on a common field (the first field in this example).

10.  Extracting unique values from a specific field:

		```bash
		$ awk '{print $1}' /var/log/syslog | sort | uniq
		``` 
11.  Count the number of requests by status code

		```bash
		$ awk '{print $9} | sort | uniq -c' logfile.txt
		```

		This command will count the number of requests by status code. The `awk` command first extracts the status code from each line in the log file. The `sort` command sorts the status codes in ascending order, and the `uniq -c` command counts the number of times each status code appears.

2.  Get the top 10 most popular URLs

	```bash
	$ awk '{print $5} | sort | uniq -c | sort -nr | head -10' logfile.txt
	```

	This command will get the top 10 most popular URLs. The `awk` command first extracts the URL from each line in the log file. The `sort` command sorts the URLs in ascending order, and the `uniq -c` command counts the number of times each URL appears. The `sort -nr` command sorts the URLs in descending order by the number of requests, and the `head -10` command prints the first 10 lines.

3.  Get the list of all errors

	```bash
	$ awk '$9 ~ /ERROR/' logfile.txt
	```

	This command will get the list of all errors. The `awk` command uses the `~` operator to match the status code `ERROR`.

4.  Get the list of all warnings

	```bash
	$ awk '$9 ~ /WARNING/' logfile.txt
	```


	This command is similar to the previous command, but it gets the list of all warnings.

5.  Get the list of all successful requests

	```bash
	$ awk '$9 ~ /200 OK/' logfile.txt
	```

6.  Get the list of all requests that took longer than 1 second

	```bash
	$ awk '$8 > 1' logfile.txt
	```

	This command will get the list of all requests that took longer than 1 second. The `awk` command uses the `>` operator to compare the value of the `8th` field to 1.

7.  Get the list of all requests from a specific IP address

	```bash
	$ awk '$1 == "192.168.1.1"' logfile.txt
	```

	This command will get the list of all requests from the IP address `192.168.1.1`. The `awk` command uses the `==` operator to compare the value of the `1st` field to `192.168.1.1`.

8.  Get the list of all requests that were made on a specific date

	```bash
	$ awk '$4 == "2023-03-08"' logfile.txt
	```

	This command will get the list of all requests that were made on the date `2023-03-08`. The `awk` command uses the `==` operator to compare the value of the `4th` field to `2023-03-08`.

9.  Get the list of all requests that were made between two dates

	```bash
	$ awk '$4 >= "2023-03-08" && $4 <= "2023-03-10"' logfile.txt
	```


	This command will get the list of all requests that were made between the dates `2023-03-08` and `2023-03-10`. The `awk` command uses the `>==` and `<==` operators to compare the value of the `4th` field to the two dates.

10.  Get the list of all requests that were made by a specific user

		```bash
		$ awk '$3 == "johndoe"' logfile.txt
		```

		This command prints the first field of each line in the syslog file, sorts them, and then outputs only the unique values.

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
eyJoaXN0b3J5IjpbMTU1Njc4MDk2NSwxMjM5Nzg4NTY5LDE5Mj
g2ODQ1OTNdfQ==
-->