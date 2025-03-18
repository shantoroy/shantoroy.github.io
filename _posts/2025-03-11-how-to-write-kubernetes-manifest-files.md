---
layout: single
title: "#100DaysOfSRE (Day 31): How to Write Kubernetes Manifest Files: Kubernetes vs Docker-Compose"
excerpt: "Learn how to convert a Docker-Compose setup into Kubernetes manifest files. We will deploy a Python-based frontend, backend, and PostgreSQL database on Minikube."
seo_title: "How to Write Kubernetes Manifest Files: Kubernetes vs Docker-Compose"
seo_description: "A hands-on guide to writing Kubernetes manifest files from a Docker-Compose setup. Deploy a Python-based frontend, backend, and PostgreSQL database using Minikube."
header:
  image: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
  teaser: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
categories:
  - Kubernetes
tags:
  - Kubernetes
  - Docker-Compose
  - DevOps
  - SRE
  - Minikube
toc: true
toc_label: "Table of Contents"
toc_icon: "rocket"
---



Many developers start their containerized applications using **Docker-Compose**, but for **scalability and production readiness**, Kubernetes is the better choice. In this tutorial, we will:

✅ Define a **Docker-Compose setup** with a Python **backend, frontend, and PostgreSQL**  
✅ Convert it into **Kubernetes manifests** (YAML files)  
✅ Deploy the **Kubernetes setup on Minikube**  

---

##  Step 1: Docker-Compose Setup

Here’s how you would define your **docker-compose.yml** for a simple Python backend, frontend, and a PostgreSQL database.

### **docker-compose.yml**
```yaml
version: "3.8"

services:
  db:
    image: postgres:15
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"

  backend:
    image: python:3.10
    container_name: backend
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/mydatabase
    ports:
      - "5000:5000"
    command: ["python", "-m", "http.server", "5000"]

  frontend:
    image: node:18
    container_name: frontend
    depends_on:
      - backend
    ports:
      - "3000:3000"
    command: ["npx", "http-server", "-p", "3000"]
```



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NzIwNzY1ODRdfQ==
-->