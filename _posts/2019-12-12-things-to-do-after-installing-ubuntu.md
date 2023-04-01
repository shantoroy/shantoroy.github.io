---
layout: single
title: "Things to do after installing Ubuntu for a Computer Science Students"
excerpt:  "Are you a computer science student who just installed Ubuntu on your machine? Here are some essential things you should do to set up your development environment, customize your system, and get the most out of your Ubuntu experience."
seo_title:  "Essential Things to Do After Installing Ubuntu for Computer Science Students"
seo_description:  "If you're a computer science student who has just installed Ubuntu, don't miss out on these essential steps to set up your system for optimal performance. Learn how to customize your environment, install necessary tools, and more in this guide."
header:
  image: "https://live.staticflickr.com/65535/49211373302_5b79643345_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49211373302_5b79643345_h.jpg"
categories:
  - Linux
tags:
  - Linux
  - Ubuntu
  - To-do list
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

As a Computer Science student/researcher, it is wise to install and use `Linux` ([Ubuntu](https://ubuntu.com/download/desktop) Preferable) Operating System. You can install `Ubuntu` as a standalone one (Unless you are a computer gamer) or alongside your `Windows` OS (Dual Boot). You can also have taste of different distributions of Linux in [Virtualbox](https://www.virtualbox.org/) or in [VMware Workstation](https://www.vmware.com/products/workstation-pro.html). However, using Linux as a virtual machine is not efficient. In my own Dell machine, I have dual boot (Ubuntu and Windows). Earlier, I was used to working in Windows platform. However now-a-days, I do not usually use Windows and prefer working in Ubuntu all the time.

I will share a to-do list in this post that includes what softwares/ applications you need to install and what other tuning operations you should perform.

## Prerequisite
* Download Ubuntu ISO image from the official site
* Make a bootable media using [Rufus](https://rufus.ie/) or [Unetbootin](https://unetbootin.github.io/)
* Follow the installation instructions after booting your PC from bootable media
* Partitioning instructions:
	* `swap` --> 2*RAM size
	* `/` --> 20-25 GB
	* `/tmp` --> 5-8 GB (You can skip it)
	* `/home` --> Rest of the empty space

## First thing first
* Update your Ubuntu. Press `ctrl+alt+t` to open a terminal. Then run the following command: 
	```bash
	$ sudo apt update
	```
* If the result shows that packages are upgradable, then run:
	```bash
	$ sudo apt full-upgrade -y
	```
* Install and customize `gnome-tweak tool` for more desktop friendly experience
	```bash
	$ sudo apt install gnome-tweak-tool -y
	```
* Install `Synaptic Package Manager`
	```bash
	$ sudo apt install synaptic -y
	```
* Install media codecs other multimedia support
	```bash
	$ sudo apt install ubuntu-restricted-extras
	```
* For Battery efficiency
	```bash
	$ sudo apt install tlp tlp-rdw
	$ sudo tlp start
	```

## Install useful softwares
### Install Chrome Browser
`Chrome` is the most popular browser and if you are not fan of `Mozilla Firefox`, the default one comes with installation, then you need to install `Google Chrome`. Follow the steps to install Chrome:
* Install `gdebi` (a tool to install `.deb` files)
	```bash
	$ sudo apt install gdebi-core
	```
* Download Chrome installation file. As later it will be no longer needed, I download it in the `/tmp` directory. It will be automatically deleted later.
	```bash
	$ cd /tmp
	$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
	```
* Now install with `gdebi`
	```bash
	$ sudo gdebi google-chrome-stable_current_amd64.deb
	```
### Install F-Search
F-Search is a great alternative to the popular `Windows` based search tool [Everything](https://www.voidtools.com/). It will help you to find any files within seconds. Download and Install F-Search with the following commands:
* Add the `fsearch` repository
	```bash
	$ sudo add-apt-repository ppa:christian-boxdoerfer/fsearch-daily
	```
* Update `apt` manager and install `fsearch`
	```bash
	$ sudo apt update && sudo apt install fsearch-trunk -y
	```

### Install VLC Media Player
Unfortunately, in Ubuntu, you cannot run `KMPlayer` or `Pot Player`. The only good alternative is the `VLC` media player. You can install `VLC Player` directly from the `Ubuntu Software Center`. Otherwise, install it with the following command:
```bash
$ sudo apt-get install vlc -y
```

### Install Systemback
* Add repository
	```bash
	$ sudo add-apt-repository "deb http://ppa.launchpad.net/nemh/systemback/ubuntu xenial main"
	```
* Add GPG signing key for verification
	```bash
	$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 382003C2C8B7B4AB813E915B14E4942973C62A1B
	```
* Update and Install
	```bash
	$ sudo apt update
	$ sudo apt install systemback
	```

### Install `bat` command
`bat` is an excellent alternative to the preinstalled `cat` command and is actually far more better than the traditional `cat` command. `bat` comes with syntax highlighting that makes codes quite readable in the terminal. Install it with following steps:
* Download the `.deb` file
	```bash
	$ cd /tmp
	$ wget https://github.com/sharkdp/bat/releases/download/v0.8.0/bat_0.8.0_amd64.deb
	```
* Install using `dpkg`
	```bash
	$ sudo dpkg -i bat_0.8.0_amd64.deb
	```

### Install Skype
You can install `Skype` directly from the `Ubuntu Software Center`. Otherwise, download and install Skype with the following steps:
*  Download Skype in `\tmp` directory using `wget`. 
	```bash
	$ cd /tmp
	$ wget https://go.skype.com/skypeforlinux-64.deb
	```
* Install Skype from the `.deb` file
	```bash
	$ sudo apt install ./skypeforlinux-64.deb
	```

## Install Development Tools
### Install `git`
* Install git and check the version
	```bash
	$ sudo apt install git
	$ git --version
	```
* Configure `git` with your `usearname` and `email`
	```bash
	$ git config --global user.name "User Name"
	$ git config --global user.email "useremail@yourdomain.com"
	```
* New configuration will be available in the `~/.gitconfig` file. You can also verify using the following command:
	```bash
	git config --list
	```

### Install Miniconda and Jupyter Notebook
Miniconda is the minimal version of `Anaconda`
Read my other post:
[# Data Science Work Environment setup on Linux/Mac](http://shantoroy.com/data%20science/data-science-environment-python-r-julia/)

### Install PyCharm
* Install Java
	```bash
	$ sudo apt install -y openjdk-8-jre-headless
	```
* Add repository
	```bash
	$ sudo add-apt-repository -y ppa:ubuntu-desktop/ubuntu-make
	```
* Update
	```bash
	$ sudo apt update
	```
* Install Umake
	```bash
	$ sudo apt install -y ubuntu-make
	```
* Insatll `PyCharm Professional`
	```bash
	$ umake ide pycharm-professional
	```

### Install VSCode
`VSCode` is a full featured editor that supports all types of programming/scripting language with the help of extensions. I prefer VSCode if I need to code in any other language apart from `Python`. Install VSCode using the following commands:
* Update package index and install dependencies
	 ```bash
	sudo apt update
	sudo apt install software-properties-common apt-transport-https wget
	```
* Import Microsoft GPG key for server verification
	```bash
	wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
	```
* Add VSCode repository
	```bash
	sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main
	```
* Update package index and then install
	```bash
	sudo apt update
	sudo apt install code
	```

### Install Docker
`Docker` is a container and suitable for running and testing application with isolation. Docker is more efficient than `Virtualbox` or `VMWare` as because the isolation is achieved in software level, not hardware level. Install Docker using the following steps:
* Prerequisite packages
	```bash
	$ sudo apt install \
	    apt-transport-https \
	    ca-certificates \
	    curl \
	    gnupg-agent \
	    software-properties-common
	```
* Add docker's official GPG key
	```bash
	$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	```
* Verify key with fingerprint for the key `9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88`. Check last 8 characters
	```bash
	$ sudo apt-key fingerprint 0EBFCD88
	```
* Set up stable repository
	```bash
	$ sudo add-apt-repository \
	   "deb [arch=arm64] https://download.docker.com/linux/ubuntu \
	   $(lsb_release -cs) \
	   stable"
	```
* Update and install docker community
	```bash
	$ sudo apt update
	$ sudo apt install docker-ce docker-ce-cli containerd.io
	```

### Install Virtualbox
Install Virtualbox to have taste of different other Operating Systems or Linux distributions. Install it with the following steps:
* Add GPG keys
	```bash
	$ wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
	$ wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
	```
* Add repository
	```bash
	sudo add-apt-repository "deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib"
	```
* Update and Install `Virtualbox`
	```bash
	$ sudo apt update
	$ sudo apt install virtualbox-6.0
	```
* Install the `Extension Pack`
	```bash
	wget https://download.virtualbox.org/virtualbox/6.0.0/Oracle_VM_VirtualBox_Extension_Pack-6.0.0.vbox-extpack
	```
* Add the extension pack manually or using the following command. It will ask if you agree to the `terms and conditions`. Press `'y'` and it will be done.
	```bash
	sudo VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-6.0.0.vbox-extpack
	```

### Install Postman
If you are working on `REST API` based application, `Postman` is a good tool to test the applications. It is available in the default `Ubuntu Software Center`. Or you can install it using the command line:
```bash
$ sudo snap install postman
```

## Tools you need not to install
For other needs, it is wise to use online tools. Most of the tools are available online these days and you need not to install those making the OS heavy. For example, you can read my other post:
[# Best Cloud-based Tools for Authors/ Scientific Content Writers](http://shantoroy.com/article/best-tools-for-authors/)



<!--stackedit_data:
eyJoaXN0b3J5IjpbNDA2MTcyNDMsMTEyNjY0MjAwMiwxNzYyMT
cwMTQ0LC01MDc1NjA2NTQsMTE1MDQ2ODg4OSwtMzc3ODI1MTc0
LC03NTEzNTUxNDcsLTE4ODUwMDA2MzYsMTc4ODkzMDI4OCwyOT
E5ODc2NTIsMTIxNTMzNTU0MywxMzg0Nzc4MTQ1LC0yNzEyNDYz
MzYsLTE0MjUwNjkzMDksNTU5NDk3MjAwLDEyMDczMzc3NDgsMT
c5MzE3OTk2MywxMDU5MzI1NDY0LDE2MTA0MDc2MjMsLTYzMTk0
MTE2MF19
-->