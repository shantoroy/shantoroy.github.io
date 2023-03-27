---
layout: single
title: "Software Defined Network: Mininet with Ryu Controller"
header:
  image: "https://live.staticflickr.com/65535/49150212507_036b060f54_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49150212507_036b060f54_h.jpg"
categories:
  - SDN
tags:
  - SDN
  - Tutorial
  - Ryu
  - Mininet
  - Simulation
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

## Installation of Ryu Controller and Mininet

I prefer installing both in a virtual machine. For that, first, we need to install [Virtualbox](https://www.virtualbox.org/wiki/Downloads) or [VMWare Workstation](https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html). Then we can download a [Ubuntu Server](https://ubuntu.com/download/server) and install it in virtualbox.

### Initialize Ubuntu Server

```sh
$ sudo apt update
$ sudo apt full-upgrade -y
```

### Install Ryu Controller

I tried installing using `pip`. But, somehow, it created problem. Therefore, I switched to `pip3` and now it is working fine.

```sh
$ sudo apt install python3-pip
$ sudo pip3 install ryu
$ ryu-manager --version
```

### Install Mininet

```sh
$ git clone git://github.com/mininet/mininet
$ cd mininet
$ git tag
$ git checkout -b 2.2.2 2.2.2
$ mkdir my_mininet
```

While installing mininet, I faced the following issue:
```
E: Package 'iproute' has no installation candidate
```

To fix the problem, edit the `install.sh` file using nano/vim.

* `nano ./util/install.sh`
* press `ctrl+w` to find string `iproute`
* replace it with `iproute2`
* press `ctrl+x` -> `yes` to save and exit

Now run the `install.sh` to install mininet.

```sh
$ ./util/install.sh -s ./my_mininet/ -a
```

## Simulation test

### Run Ryu Controller

```sh
$ ryu-manager ryu.app.simple_switch
```

### Run Mininet topology

```sh
$ sudo mn --topo single,3 --mac --switch ovsk --controller remote
```

### Check simulation

```sh
mininet> pingall
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUxMDU2ODcyNF19
-->