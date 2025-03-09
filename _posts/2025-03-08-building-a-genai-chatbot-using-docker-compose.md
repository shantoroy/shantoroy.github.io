---
layout: single
title: "#100daysofSRE (Day 28): Deploying an AI Chatbot with Docker Compose"
excerpt: "Learn how to deploy a Retrieval-Augmented Generation (RAG) Chatbot using Docker Compose. This AI-powered system leverages local LLMs for privacy, FAISS for vector search, and FastAPI for a high-performance backend."
seo_title: "Deploy an AI Chatbot using Docker Compose"
seo_description: "Explore how to containerize and deploy an AI-powered RAG Chatbot with Docker Compose, integrating FastAPI, Chainlit, and Ollama for local LLM inference."
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
  - AI
  - chatbot
  - RAG
  - LLM
toc: true
toc_label: "Table of Contents"
toc_icon: "robot"
---

**AI chatbots** have become an essential tool for businesses, developers, and researchers. They help in **automated support, knowledge retrieval, and content generation**. But running an AI chatbot efficiently requires proper deployment techniques.

In this post, we explore how **Docker Compose** simplifies the deployment of an **AI-powered Retrieval-Augmented Generation (RAG) chatbot**. This system:
- Uses **Ollama** to run **local LLMs** (no cloud dependency)
- Implements **FAISS for vector search** to retrieve documents efficiently
- Provides a **modern chat UI** using **Chainlit**
- Utilizes **FastAPI** for a high-performance backend
- Is **fully containerized**, making it easy to deploy

Since this project is quite big, I'll not go through the frontend or backend codes. I'll just go through how I utilized docker-compose to build and run the project efficiently on my macbook pro.

Please, check out the whole project on my [Github Repository](https://github.com/shantoroy/rag-chatbot-python-fullstack-template/tree/main).


---

##  System Architecture
```
        
User ───────────────▶ Chainlit UI       Documents (txt/md/pdf)
                           │                     │
                           │                     │
                    Query  │                     │ Retrieve
                           │                     │ Documents
                           ▼                     ▼
                       FastAPI ◄───────────  RAG Model ◄─────── Local Ollama
                       Backend                   │
                           │                     │
                           └─────────────────────┘
                                Return Answer
```

The chatbot takes a user’s query, retrieves relevant information from stored documents, and generates a response using a local LLM.


--- 
##  Getting Started

###  Prerequisites

- **Docker & Docker Compose**
- **Ollama (for running local models)**
- **Python 3.10+**

--- 
###  Step 1: Install Ollama

Ollama is required to run local LLM models efficiently.

#### **MacOS**
```bash
brew install ollama
brew services start ollama
``` 

####  **Linux**

```bash
curl -fsSL https://ollama.com/install.sh | sh
``` 

####  **Windows**

Download and install Ollama from the **[official Ollama website](https://ollama.com)**.

----------

### Step 2: Download Required LLM Models

Run the following commands to ensure you have the required models:

```bash
ollama run mistral
ollama run nomic-embed-text
``` 

These models handle **document embeddings** and **language generation** for accurate responses.

----------

###  Step 3: Clone the Chatbot Repository

```bash
git clone https://github.com/shantoroy/rag-chatbot-python-fullstack-template.git
cd rag-chatbot-python-fullstack-template
``` 

----------

###  Step 4: Configure the Environment

Copy `.env.example` to `.env` and modify it as needed.

```bash
cp .env.example .env
``` 

----------

###  Step 5: Deploy with Docker Compose

**Build and start the containers:**

```bash
docker-compose build
docker-compose up -d
``` 

----------

## How It Works

Once the containers are running:

1.  Access the chatbot interface at **[http://localhost:8505](http://localhost:8505)**.
2.  Upload your documents (txt, md, pdf) to the `/documents` directory.
3.  Ask questions in **natural language**.
4.  The system retrieves relevant information and generates an AI response.

----------

## Project Structure
I wanted to have the project as structured as possible. So, you'll find the backend and frontend application/api codes on corresponding folders.

The folder `docker` includes the Dockerfiles for the backend and the frontend. Since, both backend and frontend is developed in python, there are two requirements.txt files under the folder `requirements`.

This is a RAG-based AI chatbot and I've added functionalities to add three types of files under the `documents` folder: txt files, pdf files, and markdown files.

```plaintext
rag-chatbot-python-fullstack-template/
├── backend/
│   ├── model.py          # RAG model implementation
│   └── api.py            # FastAPI backend
├── frontend/
│   └── app.py            # Chainlit chat interface
├── docker/
│   ├── backend.Dockerfile
│   └── frontend.Dockerfile
├── requirements/
│   ├── backend_requirements.txt
│   └── frontend_requirements.txt
├── documents/            # Put/organize your documents here
│   ├── test_file_1.txt 
│   └── test_file_2.md
├── .env.example          # Example file, rename to .env
├── docker-compose.yml    # Service orchestration
└── README.md
``` 

----------

## Docker Compose File
I included the backend and the frontend on the docker-compose file. Now, I was running this on my macbook pro and I heard somewhere that the ollama models cannot utilize the GPUs if run within a container.

So, here, you'll not see ollama service on the dockerfile. But, you can actually run or test it on container. Ollama is properly optimized to run on personal computers. So, shouldn't be an issue.

```dockerfile
services:

  backend:
    build:
      context: .
      dockerfile: docker/backend.Dockerfile
    environment:
      - OLLAMA_URL=http://host.docker.internal:11434
    ports:
      - "8000:8000"
    volumes:
      - ./documents:/app/documents
    user: "${UID:-1000}:${GID:-1000}"
    restart: unless-stopped

  frontend:
    build:
      context: .
      dockerfile: docker/frontend.Dockerfile
    ports:
      - "8505:8505"
    environment:
      - BACKEND_URL=http://backend:8000
      - CHAINLIT_AUTH_SECRET=${CHAINLIT_AUTH_SECRET}
    volumes:
      - ./frontend/src:/app/frontend/src
      - ./frontend/public:/app/frontend/public
    depends_on:
      - backend
    restart: unless-stopped
```

----------

## Dockerfiles

### Frontend Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements/frontend_requirements.txt .
RUN pip install --no-cache-dir -r frontend_requirements.txt

# Copy application code and Chainlit config
COPY frontend /app/frontend
COPY chainlit.md /app/chainlit.md

# Command to run the frontend
CMD ["chainlit", "run", "frontend/app.py", "--host", "0.0.0.0", "--port", "8505"]
```

### Backend Dockerfile
```dockerfile
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
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

# Copy requirements first (to leverage Docker layer caching)
COPY requirements/backend_requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r backend_requirements.txt

# Download all necessary NLTK data
RUN python -m nltk.downloader -d /usr/local/share/nltk_data all
# Alternatively, if you want to download only specific packages:
# RUN python -c "import nltk; \
#     nltk.download('punkt', download_dir='/usr/local/share/nltk_data'); \
#     nltk.download('averaged_perceptron_tagger', download_dir='/usr/local/share/nltk_data'); \
#     nltk.download('punkt_tab', download_dir='/usr/local/share/nltk_data'); \
#     nltk.download('tokenizers', download_dir='/usr/local/share/nltk_data')"

# Set environment variable for NLTK data
ENV NLTK_DATA=/usr/local/share/nltk_data

# Copy application code
COPY backend /app/backend

# Create necessary directories
RUN mkdir -p /app/documents /app/vector_store

# Set permissions for appuser
RUN useradd -m appuser && \
    chown -R appuser:appuser /app/documents && \
    chown -R appuser:appuser /app/vector_store && \
    chown -R appuser:appuser /app/backend && \
    chown -R appuser:appuser /usr/local/share/nltk_data

# Switch to non-root user
USER appuser

# Set the working directory inside backend
WORKDIR /app/backend

# Expose the port
EXPOSE 8000

# Run the backend
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```


----------

## Stopping & Cleaning Up

To stop the chatbot services:

```bash
docker-compose down
``` 

To remove all associated containers, volumes, and images:

```bash
docker-compose down -v
docker system prune -a
``` 

----------

## Remarks

Deploying an **AI Chatbot** using **Docker Compose** makes it **easier to manage, deploy, and scale**.  
💡 **No need to manually configure dependencies**  
💡 **Works on any system with Docker installed**  
💡 **Leverages local LLMs for privacy and performance**

Please, check out the whole project on my [Github Repository](https://github.com/shantoroy/rag-chatbot-python-fullstack-template/tree/main).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY1MjQxNjYwOF19
-->