---
layout: single
title: "Learning Web Application Vulnerabilities: Installing Damn Vulnerable Web Application (DVWA)"
excerpt:  "If you're interested in learning web application vulnerabilities, installing Damn Vulnerable Web Application (DVWA) is a great way to get started. DVWA is a PHP/MySQL web application that contains multiple vulnerabilities intentionally placed to help users learn and practice identifying and exploiting them. In this article, I'll walk you through the installation process of DVWA on your local machine and show you how to use it to improve your understanding of web application security."
seo_title:  Your  meta  title  
seo_description:  Your  meta  description
header:
  image: "https://live.staticflickr.com/65535/52007423566_8be9641575_o.png"
  teaser: "https://live.staticflickr.com/65535/52007423566_8be9641575_o.png"
categories:
  - Security
tags:
  - DVWA
  - Tutorial
  - Web Security
  - Web Vulnerabilities 
  - XSS
  - SQL Injection
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

I will post a series tutorial of web application vulnerabilities and how to learn about these vulnerabilities through practice. Throughout the series we will learn about the common vulnerabilities including Cross-site scripting, SQL injections, etc.

In this post, we will install a vulnerable platform named `Damn Vulnerable Web Application (DVWA)`.

### What DVWA offers
DVWA includes some most popular vulnerabilities including:

-   Brute Force
-   Command Injection
-   CSRF
-   File Inclusion/Upload
-   Insecure CAPTCHA
-   SQL Injection
-   XSS (DOM/Reflected/Stored)

### Install XAMPP
First, we need to install XAMPP. XAMPP includes Apache web server along with MariaDB, PHP and Perl. Download it from the [Official Site](https://www.apachefriends.org/download.html) and install on your machine. 

If you are running a macOS like me, you will not find it after installing if you search using the keyword `XAMPP`. You will have to use `manager-osx` to start the XAMPP control panel.


### Install DVWA
First, download DVWA from [the official site](https://dvwa.co.uk/).

Now, copy it to the `htdocs` folder under the `/Applications/XAMPP` directory.

Do the following to the `config.inc.php` file located under the `config` folder:

```
$_DVWA[ 'db_user' ] = 'root';
$_DVWA[ 'db_password' ] = '';
```

Then go the browser `localhost/dvwa/setup.php` and click on the `create/reset database` button.

it will redirect to the login page where the default
* username: admin
* password: password

That's all for today. I will post the next tutorials as early as possible.

Till then, cheers!!!
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk4MTMxNDMyNCw0NTU1MjE2NDldfQ==
-->