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
```

### 📌 **Step 2: Create the `docker-compose.yml` File**

Create a directory for the lab:

```bash
mkdir hacking-lab && cd hacking-lab
``` 

Create a `docker-compose.yml` file:

```yaml
services:
  kali:
    image: kalilinux/kali-rolling
    container_name: kali
    tty: true
    stdin_open: true
    networks:
      hacknet:
        ipv4_address: 192.168.1.100
    command: ["/bin/bash"]

  metasploitable:
    image: tleemcjr/metasploitable2
    container_name: metasploitable
    restart: always
    networks:
      hacknet:
        ipv4_address: 192.168.1.101

  dvwa:
    image: vulnerables/web-dvwa
    container_name: dvwa
    restart: always
    ports:
      - "8081:80"
    environment:
      MYSQL_ALLOW_EMPTY_PASSWORD: "yes"
    networks:
      hacknet:
        ipv4_address: 192.168.1.102

  juice-shop:
    image: bkimminich/juice-shop
    container_name: juice-shop
    restart: always
    ports:
      - "3000:3000"
    networks:
      hacknet:
        ipv4_address: 192.168.1.103

networks:
  hacknet:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.1.0/24
``` 

----------

## Running the Hacking Lab

###  **1. Start All Containers**

Run:

```bash
docker-compose up -d
``` 

### **2. Verify Running Containers**

```bash
docker ps
``` 

Expected output:

```text
CONTAINER ID   IMAGE                      PORTS                   NAMES
abc12345       kalilinux/kali-rolling      -                      kali
xyz67890       tleemcjr/metasploitable2    -                      metasploitable
mno45678       vulnerables/web-dvwa       0.0.0.0:8081->80/tcp    dvwa
pqr98765       bkimminich/juice-shop      0.0.0.0:3000->3000/tcp  juice-shop
``` 

----------

## 🛠 Testing the Hacking Lab

### **1. Access the Kali Linux Container**

Run:

```bash
docker exec -it kali /bin/bash
``` 

Now you're inside a **fully functional Kali Linux** environment.

Install tools:

```bash
apt update && apt install -y nmap metasploit-framework sqlmap
``` 

### **2. Scan Metasploitable2 with Nmap**

From inside the Kali container, run:

```bash
nmap -A 192.168.1.101
``` 

This will reveal open ports and services.

### **3. Test DVWA**

Open **http://localhost:8081** in your browser.  
Use:

-   **Username**: `admin`
-   **Password**: `password`

###  **4. Test OWASP Juice Shop**

Open **http://localhost:3000** in your browser.

----------

## Stopping and Cleaning Up

###  Stop the lab

```bash
docker-compose down
``` 

### Remove volumes and images

```bash
docker-compose down -v
docker system prune -a
``` 

----------

## Conclusion

Docker Compose makes **creating a penetration testing lab** easy, fast, and repeatable.  
✅ **No need for VirtualBox or VMWare**  
✅ **Easily add/remove services**  
✅ **Networking is automatically configured**

<!--stackedit_data:
eyJoaXN0b3J5IjpbMzQxMjM1ODE5XX0=
-->