---
layout: single
title: "#100daysofSRE (Day 24): Writing a Dockerfile – Best Practices & Enhancements"
excerpt: "A well-structured Dockerfile enhances portability, security, and performance. In this post, we explore intermediate-level Dockerfile techniques like installing system dependencies, setting up environment variables, handling Python dependencies, and improving security with non-root users."
seo_title: "Intermediate Dockerfile Writing: Best Practices & Enhancements"
seo_description: "Learn intermediate-level Dockerfile techniques, including installing system dependencies, setting up environment variables, using non-root users, and optimizing Python dependency installation for better performance."
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


As we progress beyond basic Dockerfiles, it's essential to follow best practices that ensure **efficiency, security, and maintainability**.  

In this post, we'll write an **intermediate-level Dockerfile** that:
✅ Installs system dependencies  
✅ Sets up environment variables  
✅ Installs Python packages from `requirements.txt`  
✅ Downloads external resources  
✅ Uses a **non-root user** for improved security  
✅ Optimizes Docker layer caching  

---

## An Improved Dockerfile
We can define different things on dockerfile to set up and configure the perfect environment to run our application or microservices.

Here’s an example **structured Dockerfile** that follows some best practices:

```dockerfile
# Use a slim Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (e.g., build tools, libraries)
RUN apt-get update && apt-get install -y \
    build-essential \
    libmagic1 \
    file \
    unzip \
    wget \
    poppler-utils \
    tesseract-ocr \
    pandoc \
    libxml2-dev \
    libxslt1-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV NLTK_DATA=/usr/local/share/nltk_data

# Download NLTK datasets (example of external dependencies)
RUN python -m nltk.downloader -d /usr/local/share/nltk_data all

# Copy application source code
COPY src /app/src

# Create necessary directories and set permissions
RUN mkdir -p /app/data /app/logs && \
    useradd -m appuser && \
    chown -R appuser:appuser /app/data /app/logs /app/src /usr/local/share/nltk_data

# Switch to non-root user for security
USER appuser

# Expose the application port
EXPOSE 8000

# Set working directory inside the application
WORKDIR /app/src

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🔍 Breaking Down the Key Improvements

### 🛠 1. Installing System Dependencies

Many applications require external libraries (e.g., `libxml2-dev`, `libxslt1-dev`, `poppler-utils`, `tesseract-ocr`).  
We install them in a **single RUN command** to minimize the number of layers.

dockerfile

CopyEdit

`RUN apt-get update && apt-get install -y \
    build-essential \
    libmagic1 \
    file \
    unzip \
    wget \
    poppler-utils \
    tesseract-ocr \
    pandoc \
    libxml2-dev \
    libxslt1-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*` 

**Why?**  
✅ Installs all dependencies in one go to reduce image size.  
✅ Clears package lists (`rm -rf /var/lib/apt/lists/*`) to free up space.

----------

### 📦 2. Optimizing Python Dependency Installation

To leverage **Docker layer caching**, we **copy `requirements.txt` first** and install dependencies before copying the source code.

dockerfile

CopyEdit

`COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt` 

**Why?**  
✅ If `requirements.txt` doesn’t change, Docker reuses cached layers, speeding up builds.  
✅ `--no-cache-dir` prevents unnecessary storage of downloaded packages.

----------

### 🌍 3. Setting Up Environment Variables

We use environment variables to define paths for external resources.

dockerfile

CopyEdit

`ENV NLTK_DATA=/usr/local/share/nltk_data` 

**Why?**  
✅ Makes configurations flexible without modifying the code.  
✅ Improves readability and maintainability.

----------

### 📥 4. Downloading External Resources (NLTK Example)

Some applications rely on external data (e.g., NLTK datasets).

dockerfile

CopyEdit

`RUN python -m nltk.downloader -d /usr/local/share/nltk_data all` 

**Why?**  
✅ Ensures the necessary data is available inside the container.  
✅ Avoids runtime issues due to missing files.

----------

### 🔐 5. Creating Directories & Setting Permissions

Docker containers **run as root by default**, which is a security risk.  
We create directories and assign them to a **non-root user**.

dockerfile

CopyEdit

`RUN mkdir -p /app/data /app/logs && \
    useradd -m appuser && \
    chown -R appuser:appuser /app/data /app/logs /app/src /usr/local/share/nltk_data` 

Then, we **switch to the non-root user**:

dockerfile

CopyEdit

`USER appuser` 

**Why?**  
✅ Reduces the risk of privilege escalation attacks.  
✅ Prevents unauthorized modification of system files.

----------

### 🔄 6. Exposing a Port & Running the App

dockerfile

CopyEdit

`EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]` 

**Why?**  
✅ Defines the application’s network port for external access.  
✅ Uses `CMD` instead of `ENTRYPOINT` for flexibility.

----------

## 🚀 Running the Docker Container

### **1️⃣ Build the Docker Image**

bash

CopyEdit

`docker build -t myapp .` 

### **2️⃣ Run the Container**

bash

CopyEdit

`docker run -d -p 8000:8000 myapp` 

### **3️⃣ Check Logs**

bash

CopyEdit

`docker logs -f <container_id>` 

----------

## Final Thoughts

This **intermediate-level Dockerfile** follows best practices to improve **efficiency, security, and maintainability**.  
By using **layer caching, environment variables, a non-root user, and optimized dependency installation**, we build **leaner and more secure** Docker images.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNzU2NTg4NzddfQ==
-->