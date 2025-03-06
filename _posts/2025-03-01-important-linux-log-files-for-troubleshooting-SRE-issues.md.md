---
layout: single
title: "#100daysofSRE (Day 22): Essential `/var/log` Files for SREs and How to Analyze Them"
excerpt: "As a Site Reliability Engineer, logs are your best friend when troubleshooting issues. The `/var/log/` directory stores critical system and application logs that help diagnose performance bottlenecks, security incidents, and failures. In this post, we'll explore key log files and show how to extract important insights using `grep`, `sed`, and `awk`."
seo_title: "Essential `/var/log` Files for SREs and How to Analyze Them"
seo_description: "Learn about the most important log files under `/var/log` that help Site Reliability Engineers (SREs) troubleshoot system and application issues. Discover practical `grep`, `sed`, and `awk` commands to extract valuable insights."
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

## Introduction

As an SRE, logs are often your first line of defense when diagnosing issues. The `/var/log/` directory contains numerous log files that capture system and application activities. Understanding which log files to check and how to extract relevant information efficiently can save hours of troubleshooting time.

In this post, we'll cover essential log files and provide useful `grep`, `sed`, and `awk` commands to analyze them effectively.

## `/var/log/syslog` (or `/var/log/messages`)

This is the most comprehensive system log, capturing general system events, startup logs, kernel messages, and more.

1. **Find all logs related to a specific service (e.g., `nginx`)**
	```bash
	grep 'nginx' /var/log/syslog
	``` 

2. **Find logs generated in the last hour**

	```bash
	awk '$0 ~ strftime("%b %d %H", systime()-3600)' /var/log/syslog
	``` 

----------

## `/var/log/auth.log` (or `/var/log/secure` in RHEL-based distros)

This log tracks authentication-related events, including SSH login attempts and sudo usage.

1. **Find all failed SSH login attempts**

	```bash
	grep 'Failed password' /var/log/auth.log
	``` 

2. **List all unique users who have logged in**

	```bash
	awk '/session opened/ {print $NF}' /var/log/auth.log | sort | uniq
	``` 

----------

## `/var/log/kern.log`

This log captures kernel-related events, which can be useful when diagnosing hardware or kernel-related issues.

1. **Find kernel-related errors**

	```bash
	grep -i 'error' /var/log/kern.log
	``` 

2. **Extract all timestamps of kernel panics**

	```bash
	grep 'Kernel panic' /var/log/kern.log | awk '{print $1, $2, $3}'
	``` 

----------

## `/var/log/dmesg`

The `dmesg` log provides system boot logs and hardware-related messages.

1. **Check for disk-related issues**

	```bash
	dmesg | grep -i 'disk'
	``` 

2. **Find out when the system last rebooted**

	```bash
	dmesg | grep -i 'systemd' | head -n 5
	``` 

----------

## `/var/log/httpd/access.log` (or `/var/log/nginx/access.log`)

This log captures all HTTP requests for Apache or Nginx web servers.

1. **Find the most requested URLs**

	```bash
	awk '{print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -nr | head -10
	``` 

2. **Find all requests from a specific IP**

	```bash
	grep '192.168.1.100' /var/log/nginx/access.log
	``` 

----------

## `/var/log/httpd/error.log` (or `/var/log/nginx/error.log`)

This log records web server errors and can be helpful for debugging.

1. **Find all 500 Internal Server Errors**

	```bash
	grep '500' /var/log/nginx/error.log
	``` 

2. **Extract timestamps of the last 10 errors**

	```bash
	grep -i 'error' /var/log/nginx/error.log | tail -n 10 | awk '{print $1, $2}'
	``` 

----------

## `/var/log/maillog` (or `/var/log/mail.log`)

This log captures email-related activities, useful when troubleshooting mail servers.

1. **Find all emails sent to a specific recipient**

	```bash
	grep 'to=<user@example.com>' /var/log/maillog
	``` 

2. **Check for email delivery failures**

	```bash
	grep -i 'failed' /var/log/maillog
	``` 

----------

## Conclusion

The `/var/log/` directory is a good source of information that can help SREs quickly diagnose and resolve issues. 

If there are 3rd party tools or agents that are running on the host, there are separate log files for these tools as well.

By using tools like `grep`, `sed`, and `awk`, we can efficiently parse log files and extract valuable insights.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNjA2OTY4OTgsMTI3Mzk1NjQ2XX0=
-->