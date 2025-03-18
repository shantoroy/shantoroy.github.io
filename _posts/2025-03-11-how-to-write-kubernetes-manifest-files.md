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

📌 **How to run this?**

sh

CopyEdit

`docker-compose up -d` 

This works great in development, but **for production, we need Kubernetes**.

----------

## 📌 Step 2: Convert Docker-Compose to Kubernetes Manifest Files

We need to create **Kubernetes YAML files** for each component:

✅ **Deployments** (for backend, frontend, database)  
✅ **Services** (to expose them inside Kubernetes)  
✅ **Persistent Volume for PostgreSQL**

### **Project Structure**

cpp

CopyEdit

`k8s-app/
│── db/
│   ├── db-deployment.yaml
│   ├── db-service.yaml
│── backend/
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│── frontend/
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│── namespace.yaml` 

----------

### **Database Deployment (PostgreSQL)**

📌 **db/db-deployment.yaml**

yaml

CopyEdit

`apiVersion:  apps/v1  kind:  Deployment  metadata:  name:  postgres  namespace:  myapp  spec:  replicas:  1  selector:  matchLabels:  app:  postgres  template:  metadata:  labels:  app:  postgres  spec:  containers:  -  name:  postgres  image:  postgres:15  env:  -  name:  POSTGRES_USER  value:  "user"  -  name:  POSTGRES_PASSWORD  value:  "password"  -  name:  POSTGRES_DB  value:  "mydatabase"  ports:  -  containerPort:  5432` 

📌 **db/db-service.yaml**

yaml

CopyEdit

`apiVersion:  v1  kind:  Service  metadata:  name:  postgres  namespace:  myapp  spec:  selector:  app:  postgres  ports:  -  protocol:  TCP  port:  5432  targetPort:  5432` 

----------

### **Backend Deployment**

📌 **backend/backend-deployment.yaml**

yaml

CopyEdit

`apiVersion:  apps/v1  kind:  Deployment  metadata:  name:  backend  namespace:  myapp  spec:  replicas:  1  selector:  matchLabels:  app:  backend  template:  metadata:  labels:  app:  backend  spec:  containers:  -  name:  backend  image:  python:3.10  env:  -  name:  DATABASE_URL  value:  "postgresql://user:password@postgres:5432/mydatabase"  ports:  -  containerPort:  5000  command: ["python", "-m", "http.server", "5000"]` 

📌 **backend/backend-service.yaml**

yaml

CopyEdit

`apiVersion:  v1  kind:  Service  metadata:  name:  backend  namespace:  myapp  spec:  selector:  app:  backend  ports:  -  protocol:  TCP  port:  5000  targetPort:  5000` 

----------

### **Frontend Deployment**

📌 **frontend/frontend-deployment.yaml**

```yaml
apiVersion:  apps/v1  kind:  Deployment  metadata:  name:  frontend  namespace:  myapp  spec:  replicas:  1  selector:  matchLabels:  app:  frontend  template:  metadata:  labels:  app:  frontend  spec:  containers:  -  name:  frontend  image:  node:18  ports:  -  containerPort:  3000  command: ["npx", "http-server", "-p", "3000"]
``` 

 **frontend/frontend-service.yaml**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend
  namespace: myapp
spec:
  selector:
    app: frontend
  ports:
    - protocol: TCP
      port: 3000
      targetPort: 3000
  type: NodePort

``` 

----------

### **Namespace File**

 **namespace.yaml**

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: myapp
``` 

----------

##  Step 3: Deploy the Application on Minikube

1️⃣ **Start Minikube**

```sh
minikube start
``` 

2️⃣ **Apply Kubernetes manifests**

```sh
kubectl apply -f namespace.yaml
kubectl apply -f db/db-deployment.yaml
kubectl apply -f db/db-service.yaml
kubectl apply -f backend/backend-deployment.yaml
kubectl apply -f backend/backend-service.yaml
kubectl apply -f frontend/frontend-deployment.yaml
kubectl apply -f frontend/frontend-service.yaml
``` 

3️⃣ **Check the status**

```sh
kubectl get all -n myapp
``` 

4️⃣ **Get frontend service URL**

```sh
minikube service frontend -n myapp
``` 

**Now you have deployed your full-stack app on Minikube!**

----------

## Remarks

 **Key Takeaways**  
✅ **Docker-Compose** is great for local development.  
✅ **Kubernetes manifests** provide scalability, high availability, and production readiness.  
✅ Minikube helps you **test Kubernetes locally** before deploying to the cloud.

**Next Steps**

-   Add a **Kubernetes Ingress Controller**
-   Implement **ConfigMaps & Secrets** for better security
-   Use **Helm Charts** to manage deployment configurations

<!--stackedit_data:
eyJoaXN0b3J5IjpbNzIyNTI3ODk5XX0=
-->