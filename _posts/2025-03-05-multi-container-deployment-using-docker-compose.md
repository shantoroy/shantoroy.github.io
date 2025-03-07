---
layout: single
title: "#100daysofSRE (Day 26): Docker Compose - Simplifying Multi-Container Deployments"
excerpt: "Docker Compose is an essential tool for developers, SREs, and DevOps engineers, allowing them to define and manage multi-container applications easily. In this post, we'll explore its benefits and provide a practical example of using Docker Compose to set up a full-stack application."
seo_title: "Docker Compose - Manage Multi-Container Applications with Ease"
seo_description: "Learn how Docker Compose simplifies multi-container application deployments. We cover its key benefits, real-world use cases, and provide a hands-on example with frontend and backend services."
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
  - containers
  - docker-compose
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Managing multiple containers manually with `docker run` can become cumbersome when handling **microservices** or **multi-container applications**. This is where **Docker Compose** simplifies everything by letting you define and run your entire environment using a single YAML file.

✅ Define infrastructure as code  
✅ Manage multiple services in one place  
✅ Automate networking and dependency management  
✅ Great for **local development** and **testing microservices**  

In this guide, we'll explore **how Docker Compose works** and set up a **full-stack application** with a **frontend**, **backend**, and a **database**.

---

## ⚡ Why Docker Compose?

###  1. **Simplifies Multi-Container Management**
Instead of running multiple `docker run` commands, Compose lets you **define everything in one file** and bring up the entire stack with:
```bash
docker-compose up -d
```

###  2. **Defines Services in a Single YAML File**

Instead of running:

```bash
docker run -d -p 5000:5000 backend
docker run -d -p 3000:3000 frontend
docker run -d -p 5432:5432 postgres
``` 

We can define everything in a `docker-compose.yml` file and deploy with **one command**.

###  3. **Handles Networking Automatically**

Each service gets its own **hostname**, so instead of using **IP addresses**, services can communicate via container names. It can be automatic or manual network setup.

### 4. **Easily Scalable**

Need **more backend instances**? We have a solution and we can just scale up accordingly:

```bash
docker-compose up --scale backend=3
``` 

----------

## Example Full-Stack Application with Docker Compose

Here, we will set up: 
✅ **Frontend** (React)  
✅ **Backend** (FastAPI)  
✅ **Database** (PostgreSQL)

----------

### 📌 **Step 1: Define the Backend (FastAPI)**

#### **`backend/Dockerfile`**

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
``` 

#### **`backend/requirements.txt`**

```text
fastapi
uvicorn
psycopg2
``` 

#### **`backend/main.py`**

```python
from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}
``` 

----------

### **Step 2: Define the Frontend (React)**

#### **`frontend/Dockerfile`**

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]
``` 

----------

### **Step 3: Define the Docker Compose File**

#### **`docker-compose.yml`**

```yaml
version: "3.8"

services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/mydatabase
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
``` 

----------

##  Running the Full-Stack Application

### **1. Build and Start Services**

Run the following command to start the services in detached mode:

```bash
docker-compose up -d
``` 

### **2. Check Running Containers**

```bash
docker-compose ps
``` 

This should show:

```text
Name                    Command               State           Ports
------------------------------------------------------------------------------
myapp_backend_1     uvicorn main:app --host ...    Up       0.0.0.0:5000->5000/tcp
myapp_frontend_1    npm start                      Up       0.0.0.0:3000->3000/tcp
myapp_db_1          docker-entrypoint.sh postgres  Up       0.0.0.0:5432->5432/tcp
``` 

### **3. Test the Backend**

Run:

```bash
curl http://localhost:5000/
``` 

Expected output:

```json
{"message": "Hello from FastAPI!"}
``` 

### **4. Access the Frontend**

Open **http://localhost:3000** in your browser.

----------

## Advanced Docker Compose Features

### **1. Scaling Services**

Want **3 backend instances**?

```bash
docker-compose up --scale backend=3
``` 

### **2. Logs**

View logs for all services:

```bash
docker-compose logs -f
``` 

### **3. Stopping and Cleaning Up**

Stop services:

```bash
docker-compose down
``` 

Remove **volumes** (database data):

```bash
docker-compose down -v
``` 

----------

## Remarks

Docker Compose makes **multi-container applications** easy to manage.  
✅ **One file** to manage all services  
✅ **Handles networking & dependencies** automatically  
✅ **Great for Dev, Test, and Local Microservice Environments**

By using `docker-compose.yml`, SREs, DevOps engineers, and developers can **quickly spin up full application stacks**, making their workflow much more efficient. 

I have been building some cool multi-container applications and testing different devops/sre tools using docker-compose. You can check out my GitHub. One of those projects is a [AI Chatbot](https://github.com/shantoroy/rag-chatbot-python-fullstack-template) which utilizes RAG to retrieve information and shows on a chat when asked.

<!--stackedit_data:
eyJoaXN0b3J5IjpbNzMwNDk1NTY0XX0=
-->