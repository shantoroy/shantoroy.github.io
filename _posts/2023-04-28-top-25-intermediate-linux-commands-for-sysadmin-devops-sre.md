---
layout: single
title: "#100daysofSRE (Day 18): 25 Intermediate-level Linux Commands useful for SysAdmin, DevOps, and SRE"
excerpt: "Your blog post excerpt"
seo_title: "Your meta title"
seo_description: "Your meta description"
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
  - linux
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


---
Hi there!!! 👋

It's the 18th day of the `#100dayschallenge`, and today I will list 25 useful Linux commands that are handy for SysAdmins, DevOps, and SRE.

So, I have planned the  [contents for next 100 days](https://medium.com/@shantoroy/learning-about-site-reliability-engineering-with-the-100daysofsre-challenge-66380323c0d1), and I will be posting one blog post each and everyday under the hashtag  `#100daysofSRE`. ✌️

I hope you tag along and share valuable feedback as I grow my knowledge and share my findings. 🙌


## Linux Commands

Linux terminal is a powerful tool that enables system administrators, DevOps engineers, and SREs to manage servers and applications efficiently. In this blog post, we will cover 25 advanced Linux terminal commands with options and arguments that are typically used by sysadmins, DevOps, and SREs.

1.  `grep`: grep is a powerful command-line tool that allows you to search for a specific pattern or string in a file or directory. You can use the `-r` option to search recursively, `-i` option to ignore case, and `-n` option to print line numbers. For example:`grep -rni "error" /var/log`

2.  `sed`: sed is a stream editor that allows you to perform text transformations on an input stream. You can use sed to replace, delete, or insert text in a file or stream. Example usage is as follows: `sed 's/foo/bar/g' filename`

3.  `awk`: awk is a powerful text processing tool that allows you to manipulate and analyze data. We can use awk to filter, format, and transform data. For example, `awk '{print $1,$3}' filename`

4.  `tail`: tail allows you to display the last lines of a file. You can use the `-f` option to follow the file and display new lines as they are added. We can run it like this: `tail -f /var/log/messages`.

5.  `top`: top is a system monitoring tool that displays real-time information about system processes and resource usage. We can use top to identify resource-intensive processes and troubleshoot system performance issues.


6.  `htop` or `atop`: htop is an interactive process viewer that displays system processes and resource usage in a user-friendly way. You can use htop to monitor system performance and troubleshoot issues. `atop` is another command-line tool that can be used to monitor system performance. It can be used to view CPU and memory usage, disk activity, network activity, and process activity.


7.  `iostat`: iostat is a system monitoring tool that displays input/output statistics for storage devices. You can use iostat to monitor disk performance and identify performance bottlenecks. We can run it like this: `iostat -x 1`

8.  `netstat`: netstat displays network statistics for TCP, UDP, and other network protocols. You can use netstat to identify active network connections and troubleshoot network issues. Example usage is as follows: `netstat -an`

9.  `ping`: ping is a network diagnostic tool that sends ICMP packets to a remote host to check its availability and response time. You can use ping to test network connectivity and troubleshoot network issues.

10.  `traceroute`: traceroute is a network diagnostic tool that displays the route and time taken by packets to reach a remote host. You can use traceroute to troubleshoot network routing issues.

11.  `tcpdump`: tcpdump is a network packet analyzer that captures and displays network traffic. You can use tcpdump to monitor network traffic and troubleshoot network issues. Example usage is as follows:`tcpdump -i eth0 port 80`.

12.  `dig`: dig is a DNS lookup tool that displays DNS information for a domain. You can use dig to troubleshoot DNS issues and verify DNS configurations. We can run it like `dig google.com`.


14.  `ssh`: ssh is a secure shell protocol that allows you to securely connect to a remote host and execute commands. You can use ssh to manage remote servers and applications.

15.  `scp`: scp is a secure copy protocol that copies files over SSH. It is useful when remotely copy files from one machine to another.

16.  `lsof`: This command is used to list all open files and the processes that have opened them. It is useful for troubleshooting when a file cannot be deleted because it is still in use.
    
17.  `iptables`: This command is used to set up and manage firewall rules in Linux. It is essential for securing a server and controlling network traffic.
    
18.  `rsync`: This command is used to synchronize files and directories between two locations. It is useful for backups and for transferring files between servers.
    
    
22.  `tar`: This command is used to create and manipulate tar archives, which are commonly used for backups and file transfers.
    
23.  `curl`: This command is used to transfer data from or to a server using various protocols, including HTTP, FTP, and SMTP.
    

21.  `ss` - A command to monitor network connections. It can show network sockets that are in use, display network statistics, and show TCP and UDP connections.
    
22.  `strace` - A debugging tool that shows the system calls made and received by a process. It can be used to trace the behavior of an application, identify bottlenecks, and diagnose problems.
    
23.  `lsof` - A command to list open files and the processes that are using them. It can be used to find which process is using a file, check for open ports, and identify which network connections are in use.
    
    
25.  `nc` - A command-line tool that can be used for network communication. It can be used to open network connections, send and receive data over a network, and troubleshoot network problems.

    
27.  `pv` - A command-line tool that can be used to monitor the progress of data through a pipeline. It can be used to track the progress of file transfers, copy files with progress information, and monitor the output of commands.
    
    
29.  `sysdig` - A command-line tool that can be used to monitor system activity at the system call level. It can be used to diagnose problems, troubleshoot issues, and analyze system performance.
    

## Related Posts
* [How to Install Specific Version of Linux Header in a Raspberry Pi](https://shantoroy.com/raspberry%20pi/install-specific-version-of-linux-header/)
* [Things to do after installing Ubuntu for a Computer Science Students](https://shantoroy.com/linux/things-to-do-after-installing-ubuntu/)
* [How to install Open Stack cloud in Cent OS or Red Hat Linux](https://shantoroy.com/cloud/install-openstack-in-centos-redhat/)
* [Set Up Headless Kali Linux in a Raspberry Pi 4 without Monitor, Keyboard, and Mouse](https://shantoroy.com/security/install-kali-linux-in-raspberry-pi-4/)
* [How to Set Static IP Address in Linux/Raspbian OS](https://shantoroy.com/linux/set-static-hostname-linux-mac-windows-raspbian/)
* [Data Science Work Environment setup on Linux/Mac](https://shantoroy.com/data%20science/data-science-environment-python-r-julia/)
* [How to SSH Remote Login without Password in Linux/Mac](https://shantoroy.com/system%20administration/ssh-login-without-password-linux-mac/)

___

___

Thank you for reading my blog post! 🙏

If you enjoyed it and would like to stay updated on my latest content and plans for next week, be sure to subscribe to my newsletter on Substack. 👇

Once a week, I'll be sharing the latest weekly updates on my published articles, along with other news, content and resources. Enter your email below to subscribe and join the conversation for Free! ✍️

<iframe src="https://shantoroy.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

I am also writing on Medium. You can [follow me here](https://medium.com/@shantoroy).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMxMzk5MTI2NiwtNjI0OTQwNjQ2XX0=
-->