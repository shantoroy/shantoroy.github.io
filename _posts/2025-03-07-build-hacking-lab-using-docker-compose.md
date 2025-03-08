---
layout: single
title: "#100daysofSRE (Day 27): Building a Hacking Lab with Docker Compose"
excerpt: "Want to practice ethical hacking, penetration testing, or security research? With Docker Compose, you can quickly set up a self-contained hacking lab, including Kali Linux and multiple vulnerable machines. This post will guide you through building your own hacking playground."
seo_title: "Docker Compose Hacking Lab: Kali Linux & Vulnerable Machines"
seo_description: "Learn how to use Docker Compose to create a hacking lab with Kali Linux and vulnerable applications for security research and ethical hacking practice."
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
  - docker
  - security
  - penetration-testing
  - ethical-hacking
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

As an **SRE**, **DevOps Engineer**, or **Security Enthusiast**, having a **safe, controlled hacking lab** is crucial for **security research**, **penetration testing**, and **learning ethical hacking**.

Using **Docker Compose**, we can quickly spin up:
- ✅ **Kali Linux** for penetration testing
- ✅ **Metasploitable2** – A vulnerable OS to practice attacks
- ✅ **DVWA (Damn Vulnerable Web App)** – A web-based application with security flaws
- ✅ **OWASP Juice Shop** – Another web app designed for security testing

---

##  Why Use Docker Compose for a Hacking Lab?

- **Fast & Repeatable** – No need to install multiple VMs manually
- **Lightweight** – Runs efficiently on any system with Docker installed
- **Isolated Environment** – No risk to your main system
- **Networking Made Easy** – All machines can communicate within a virtual network

---

##  Setting Up the Hacking Lab

###  **Step 1: Install Docker & Docker Compose**
Ensure you have **Docker** and **Docker Compose** installed.

Test if Docker is working:
```bash
docker --version
docker-compose --version

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzOTIyODc4NTBdfQ==
-->