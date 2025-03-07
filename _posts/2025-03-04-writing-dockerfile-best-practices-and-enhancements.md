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

## 🚀 The Improved Dockerfile

Here’s a **structured Dockerfile** that follows best practices:

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

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NzUwNzAxOTZdfQ==
-->