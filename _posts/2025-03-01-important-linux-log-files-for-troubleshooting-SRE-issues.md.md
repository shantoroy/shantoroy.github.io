``---
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

### **Find all logs related to a specific service (e.g., `nginx`)**
```bash
grep 'nginx' /var/log/syslog
``` 

### **Find logs generated in the last hour**

```bash
`awk '$0 ~ strftime("%b %d %H", systime()-3600)' /var/log/syslog` 

----------

## 2. `/var/log/auth.log` (or `/var/log/secure` in RHEL-based distros)

This log tracks authentication-related events, including SSH login attempts and sudo usage.

### **Find all failed SSH login attempts**

bash

CopyEdit

`grep 'Failed password' /var/log/auth.log` 

### **List all unique users who have logged in**

bash

CopyEdit

`awk '/session opened/ {print $NF}' /var/log/auth.log | sort | uniq` 

----------

## 3. `/var/log/kern.log`

This log captures kernel-related events, which can be useful when diagnosing hardware or kernel-related issues.

### **Find kernel-related errors**

bash

CopyEdit

`grep -i 'error' /var/log/kern.log` 

### **Extract all timestamps of kernel panics**

bash

CopyEdit

`grep 'Kernel panic' /var/log/kern.log | awk '{print $1, $2, $3}'` 

----------

## 4. `/var/log/dmesg`

The `dmesg` log provides system boot logs and hardware-related messages.

### **Check for disk-related issues**

bash

CopyEdit

`dmesg | grep -i 'disk'` 

### **Find out when the system last rebooted**

bash

CopyEdit

`dmesg | grep -i 'systemd' | head -n 5` 

----------

## 5. `/var/log/httpd/access.log` (or `/var/log/nginx/access.log`)

This log captures all HTTP requests for Apache or Nginx web servers.

### **Find the most requested URLs**

bash

CopyEdit

`awk '{print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -nr | head -10` 

### **Find all requests from a specific IP**

bash

CopyEdit

`grep '192.168.1.100' /var/log/nginx/access.log` 

----------

## 6. `/var/log/httpd/error.log` (or `/var/log/nginx/error.log`)

This log records web server errors and can be helpful for debugging.

### **Find all 500 Internal Server Errors**

bash

CopyEdit

`grep '500' /var/log/nginx/error.log` 

### **Extract timestamps of the last 10 errors**

bash

CopyEdit

`grep -i 'error' /var/log/nginx/error.log | tail -n 10 | awk '{print $1, $2}'` 

----------

## 7. `/var/log/maillog` (or `/var/log/mail.log`)

This log captures email-related activities, useful when troubleshooting mail servers.

### **Find all emails sent to a specific recipient**

bash

CopyEdit

`grep 'to=<user@example.com>' /var/log/maillog` 

### **Check for email delivery failures**

bash

CopyEdit

`grep -i 'failed' /var/log/maillog` 

----------

## Conclusion

The `/var/log/` directory is a goldmine of information that can help SREs quickly diagnose and resolve issues. By using tools like `grep`, `sed`, and `awk`, you can efficiently parse log files and extract valuable insights.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwOTE4NTU3NjVdfQ==
-->