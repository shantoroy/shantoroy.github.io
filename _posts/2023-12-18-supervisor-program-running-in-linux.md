---
layout: single
title: "#100daysofSRE (Day 21): How to use Supervisor to manage a script on Linux"
excerpt: "Managing and automating scripts on Linux systems is crucial for ensuring smooth operations. One effective solution for this is Supervisor, which is a powerful process control system. In this comprehensive guide, learn how to use Supervisor to effortlessly manage scripts, ensure their continuous execution, and maintain system stability."
seo_title: "How to use Supervisor to manage a script on Linux"
seo_description: "Learn how to utilize Supervisor, a robust process control system on Linux, to effectively manage and automate scripts for enhanced system stability. This post covers the installation, configuration, and practical usage of Supervisor so that you can seamlessly maintain your scripts' execution for optimized performance."
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

I ran a program (python API) a few months ago, and I did not need to check it in the meantime. Then one day, some other developers who were using that API told me they no longer had access to it.

I was a bit shocked to learn that, as I did run it in the background on an AWS EC2 instance. Now, the question arises: can this happen again? We need a solution.

`Supervisor` is an excellent program that can do the job quite well. It can monitor if a particular process is continuously running or not. If stopped, it will automatically invoke the process again.

In this post, I will go through how to configure Supervisor on a Linux machine. In this scenario, I did it on my EC2 Ubuntu instance.

### Step 1: Set Up Supervisor Configuration

1.  **Create a Supervisor Configuration File**: Navigate to the Supervisor configuration directory (usually `/etc/supervisor/conf.d/`) and create a `.conf` file for your Python script. For example, let's name it `my_script.conf`.

    ```bash
    $ sudo nano /etc/supervisor/conf.d/my_script.conf
    ``` 
    
2.  **Add Configuration Details**: Inside `my_script.conf`, define the configuration details for your Python script.
    

	```bash
	[program:my_python_script]
	command=/path/to/your/virtualenv/bin/python /path/to/your/script.py
	directory=/path/to/your/script/directory
	user=your_username
	autostart=true
	autorestart=true
	stderr_logfile=/var/log/my_python_script.err.log
	stdout_logfile=/var/log/my_python_script.out.log
	```

-   Replace `/path/to/your/virtualenv` with the path to your virtual environment.
   -   Replace `/path/to/your/script.py` with the path to your Python script.
   -   Update `directory` with the directory path where your script resides.
   -   Set `user` to your Ubuntu username.
   -   Modify log file paths (`stderr_logfile` and `stdout_logfile`) to your preferred locations.

### Step 2: Update Supervisor and Start/Restart the Service

1.  **Update Supervisor**: After making changes to the configuration, update Supervisor.
    
    
    ```bash
    $ sudo supervisorctl reread
    $ sudo supervisorctl update
    ``` 
    
2.  **Start/Restart Service**: Start or restart Supervisor service.

    ```bash
    $ sudo systemctl restart supervisor
    ``` 
    

### Notes

-   Ensure that Supervisor is installed and running on your Ubuntu system.
-   Replace placeholders like `/path/to/your/` and `your_username` with your actual paths and username.
-   Activate your virtual environment before adding the Python script to Supervisor.
-   Monitor logs in the specified log files to troubleshoot issues (`/var/log/my_python_script.err.log` and `/var/log/my_python_script.out.log`).

This setup will ensure that your Python script runs continuously in the background and restarts automatically if it crashes or the system reboots. Adjust the configuration as needed for your specific use case.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExOTQ4NjU5M119
-->