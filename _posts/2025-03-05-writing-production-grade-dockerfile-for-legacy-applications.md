---
layout: single
title: "#100daysofSRE (Day 25): Writing a Production-Grade Dockerfile for Legacy Applications"
excerpt: "Building a robust, secure, and production-ready Dockerfile for legacy applications requires advanced techniques. This post covers multi-stage builds, minimizing attack surfaces, handling dependencies, and running services efficiently."
seo_title: "Advanced Dockerfile Writing for Production-Grade Legacy Applications"
seo_description: "Learn how to write a production-grade Dockerfile optimized for legacy applications. We cover multi-stage builds, security best practices, process management, and dependency handling to ensure high performance in production environments."
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
  - production
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


When running **legacy applications** in **production**, a standard Dockerfile won't be enough.  

We need to ensure extra features such as:  
✅ **Security** – Running non-root, minimizing attack surfaces  
✅ **Performance** – Optimized layer caching, removing unnecessary files  
✅ **Compatibility** – Handling older dependencies without breaking the system  
✅ **Reliability** – Ensuring services don’t crash, logging properly  
✅ **Multi-Stage Builds** – Reducing final image size  

In this guide, we’ll build a **production-grade Dockerfile** optimized for legacy apps.  

---

## Key Considerations for Production

### 1. **Minimize Image Size**  
Use **multi-stage builds** to install dependencies in a temporary container and copy only necessary artifacts. It also ensures optimality and additional security.

### 2. **Security Best Practices**  
- Avoid running as `root`  
- Limit unnecessary package installations  
- Remove sensitive files right after the setup  

### 3. **Dependency Handling**  
Some **legacy apps require older dependencies**. Using a compatible base image and carefully installing necessary packages is key.

### 4. **Process Management**  
Legacy apps might use multiple processes. Using **supervisord** or process managers ensures proper startup. If you want to know more about supervisor applications/processes, check my [other blog post](https://shantoroy.com/sre/supervisor-program-running-in-linux/).

---

## The Advanced Production-Ready Dockerfile

###  **Multi-Stage Build for an example Legacy Python Application**

```dockerfile
# Stage 1: Build dependencies
FROM python:3.10-slim AS builder

WORKDIR /app

# Install necessary build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies in a virtual environment
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2: Final production image
FROM python:3.10-slim

WORKDIR /app

# Install runtime dependencies (minimal install)
RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy pre-built dependencies from builder stage
COPY --from=builder /opt/venv /opt/venv

# Set environment variables for the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Copy application source code
COPY src /app/src

# Ensure non-root user execution
RUN useradd -m appuser && \
    chown -R appuser:appuser /app/src
USER appuser

# Expose the application port
EXPOSE 8080

# Use a process manager (supervisord) to run multiple services
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
```


## 🔍 Breaking Down the Key Enhancements

### 🎯 1. **Multi-Stage Build to Reduce Image Size**

In the first stage (`builder`), we:  
✅ Install build dependencies like `gcc` and `build-essential`  
✅ Install Python packages inside a **virtual environment**

In the final image, we:  
✅ Copy only the pre-built virtual environment  
✅ Install **only** required runtime dependencies (e.g., `libpq5`)

----------

### 🔒 2. **Security Best Practices**

#### **a) Non-Root User for Execution**

dockerfile

CopyEdit

`RUN useradd -m appuser && \
    chown -R appuser:appuser /app/src
USER appuser` 

✅ Prevents privilege escalation attacks

----------

#### **b) Minimal Dependency Installation**

Instead of `apt-get install -y <everything>`, we **only install what’s necessary**.

dockerfile

CopyEdit

`RUN apt-get update && apt-get install -y libpq5 \
    && rm -rf /var/lib/apt/lists/*` 

✅ Reduces image size  
✅ Limits security vulnerabilities

----------

### 🔄 3. **Using a Process Manager (Supervisord)**

Legacy apps might need **multiple services running inside one container**.  
Instead of relying on `CMD ["python", "app.py"]`, we use **supervisord** to handle multiple processes.

#### **Supervisord Configuration (`supervisord.conf`)**

ini

CopyEdit

`[supervisord]
nodaemon=true

[program:app]
command=python /app/src/main.py
autostart=true
autorestart=true
stderr_logfile=/var/log/app.err.log
stdout_logfile=/var/log/app.out.log` 

✅ Ensures app **restarts** if it crashes  
✅ Captures logs in `/var/log/app.out.log`

----------

### 📦 4. **Handling Legacy Dependencies**

Some legacy applications require **older versions of dependencies** that conflict with newer ones.

#### **Installing Python Packages in a Virtual Environment**

```dockerfile
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt
``` 

✅ Ensures dependencies don’t interfere with system packages  
✅ Keeps the final image clean

----------

## Running the Production Container

### **1️⃣ Build the Image**

```bash
docker build -t mylegacyapp .
``` 

### **2️⃣ Run the Container**

```bash
docker run -d -p 8080:8080 mylegacyapp
``` 

### **3️⃣ Check Running Processes**

```bash
docker exec -it <container_id> supervisorctl status
``` 

### **4️⃣ Tail Logs**

```bash
docker logs -f <container_id>
``` 

----------

## Conclusion
In summary, on production level images, we consider more optimal runtime and enhanced security and reliability.

Therefore, building **a production-ready Dockerfile for legacy applications** requires: 
✅ **Multi-stage builds** to reduce image size  
✅ **Minimal dependencies** to reduce attack surface  
✅ **Non-root execution** for better security  
✅ **Process managers** like `supervisord` for multi-process apps

Hope, that helps! In the upcoming days, we will learn more about containerized applications in production.

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU1MDI3OTAzMl19
-->