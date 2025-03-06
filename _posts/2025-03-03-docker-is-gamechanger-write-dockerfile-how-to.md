---
layout: single
title: "#100daysofSRE (Day 23): Modernize and Containerize your Application"
excerpt: "Docker has revolutionized the way we deploy and manage applications by providing lightweight, portable containers. In this post, we'll explore why Docker is better than traditional VMs and walk through how to write a `Dockerfile` to containerize applications efficiently."
seo_title: "Why Docker is Better Than VMs & Writing Your First Dockerfile"
seo_description: "Learn why Docker is a game-changer compared to traditional virtual machines and how to write a Dockerfile with practical examples. Ideal for SREs, DevOps, and developers looking to simplify deployments."
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
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Docker has transformed how applications are packaged, shipped, and run by introducing **containers**—lightweight, portable environments that encapsulate everything an application needs to run. 

It also solves the major issue of running an application on different machines. Docker provides the same portability option so that you can run your application on Linux, Windows, or whatever platform you want to!

But how does Docker compare to traditional Virtual Machines (VMs), and why should SREs and DevOps engineers prefer it?

In this post, we'll discuss **why Docker is better than VMs**, and then we'll **write a Dockerfile from scratch** to containerize a simple application.

---

## 🚀 Why Docker is Better Than Virtual Machines

| Feature          | Docker 🐳  | Virtual Machines 💻 |
|-----------------|------------|------------------|
| **Startup Time** | Seconds   | Minutes         |
| **Performance** | Lightweight, shares host OS | Heavy, each VM runs its own OS |
| **Resource Usage** | Low (efficient memory & CPU usage) | High (entire OS per VM) |
| **Portability** | Runs anywhere (on any OS, cloud, on-prem) | Tied to specific infrastructure |
| **Scalability** | Easily scales with orchestration (Kubernetes) | Scaling requires provisioning full VMs |
| **Isolation** | Process-level isolation | Full OS-level isolation |

### ✅ Key Advantages of Docker:
- **Fast Deployment:** Containers spin up in seconds.
- **Less Overhead:** No need for an entire OS per application.
- **Consistent Environments:** Works the same on any system.
- **Easy to Scale:** Works seamlessly with Kubernetes and cloud providers.

---

## 🛠 Writing Your First Dockerfile

A `Dockerfile` is a script containing a set of instructions to build a Docker image. Let's create a simple **Python Flask application** inside a Docker container.

### **Step 1: Create a Simple Flask App**
Create a directory and add the following Python script as `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### **Step 2: Create a Dockerfile**

Inside the same directory, create a file named `Dockerfile` (no file extension) and add the following:

```docker
# Use the official Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY app.py .

# Install Flask (required to run the app)
RUN pip install flask

# Expose port 5000 to the host
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

```


### **Step 3: Build and Run the Docker Container**

1️⃣ **Build the Docker image**

```bash
docker build -t flask-app .
```

2️⃣ **Run the container**

```bash
docker run -d -p 5000:5000 flask-app
``` 

3️⃣ **Access the application**  
Open your browser and visit:  
```
👉 http://localhost:5000
```  
You should see `"Hello, Docker!"` displayed.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU0Mjg0ODY5NiwxNjIzMTM3NDg5XX0=
-->