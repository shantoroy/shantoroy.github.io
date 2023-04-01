---
layout: single
title: "How to SSH Remote Login without Password in Linux/Mac"
excerpt:  "If you're tired of constantly entering your password when logging into a remote server via SSH, there is a better way. In this blog post, I'll show you how to set up SSH key authentication, so you can log in to your remote server without typing in your password every time."
seo_title:  "How to SSH Remote Login without Password in Linux/Mac"
seo_description:  Learn how to set up SSH key authentication to log in to your remote server without a password in Linux and Mac, and streamline your remote server access. Say goodbye to the hassle of typing in your password every time with this simple SSH setup guide.
header:
  image: "https://live.staticflickr.com/65535/49853015493_7ff7d6881c_z.jpg"
  teaser: "https://live.staticflickr.com/65535/49853015493_7ff7d6881c_z.jpg"
categories:
  - System Administration
tags:
  - Tutorial
  - System Administration
  - ssh
  - remote login
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


When we access a machine, it prompts for password for the corresponding user. However, it is tiresome, if need to access frequently, and each time we have to type the password.

In this post, we will learn how to ssh login to a remote computer without typing password each time we access later.

Let's take a look how we need to configure key-pairs in both- local and remote machines.

## Local Machine
Usually, in the user home directory, there is a hidden directory named **`.ssh`**. We will generate key-pairs in that directory. If there is no such directory, create one using the command `mkdir .ssh`

### Generate Key-pair
Now, generate key-pair using the command **`ssh-keygen`** and set a name for the key files. Here, I have chosen the name as `rsa`. 
```bash
<user@local>:~$ cd .ssh
<user@local>:~$ ssh-keygen -t rsa
```

Follow the instructions and then two files will be created named as- `rsa` and `rsa.pub`. 

### Add Key to the Keychain 
Now, let's add the key to the authentication agent using the command **`ssh-add`**.
```bash
<user@local>:~$ ssh-add ~/.ssh/rsa
```
We can check if the key has been added in the authentication agent.
```bash
<user@local>:~$ ssh-add -l
```

## Remote Machine
All we need to do in a remote machine is to add the generated public key in the `~/.ssh/authorized_keys` file. Create the file if there is none.

### Add public key
Copy the contents of the public key (`.pub`) from your local machine.
```bash
<user@local>:~$ cat ~/.ssh/rsa.pub
Output>
	ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCre9snImDkV6SflHBMhNYMaKty+ADpeKAs5cJi3z/SGIwuH/eWOkVIFCkZye/BdKurtuX8rtXYXudQCXZ8arzHdaeTwP135e8fefDDZ9cMqyyCf0IlCkLw0ydrInfPzpsu2L2pqlqUiM2Urjpo0AVF4XuBbo/RBcXe49l91AFkjvrBSFIaxlRCV36R5NYBGmLqSEDTDSpmspxjaa2bbwT0X/oS+WQkp6FHHX0x67YeoEjf1qP5DMmbWKeiyqJeMkdhmeVjlnuFLkpZrS+m2vuchmuCHrGkNov6FjLTalE2Koe1YxzI13GpDMFZglFWoz7CfJWHtv9ZD5oQgAssNTwj mrx@mrx-Inspiron-5548
```

Now, append the key content in the `authorized_keys` file of your remote machine.
```bash
<user@remote>:~$ sudo nano ~/.ssh/authorized_keys
```

Now, you can ssh to the device without password. Suppose the IP address of the remote device is `192.168.1.5`. So, you can ssh now using the following command:
```bash
<user@local>:~$ ssh remote_user@192.168.1.5
```

That's all!!!


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMxODc2NjU2NSw5MTc3MjY2MzMsLTUxOD
c1MzIxNiwtMjU2MjkyNzQzLDE4MDMzMDc2MDZdfQ==
-->