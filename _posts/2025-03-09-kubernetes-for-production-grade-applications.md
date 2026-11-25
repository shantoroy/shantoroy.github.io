---
layout: single
title: "#100daysofSRE (Day 29): Kubernetes over Docker-compose – Why It’s Better for Production"
excerpt: "Learn why Kubernetes is the go-to solution for production deployments, replacing Docker Compose with enterprise-grade scalability, reliability, and automation."
seo_title: "Introduction to Kubernetes – Why It’s Better for Production"
seo_description: "Discover why Kubernetes is preferred over Docker Compose for enterprise deployments. Learn how it enhances scalability, fault tolerance, and automation."
header:
  image: "https://live.staticflickr.com/65535/55672381423_3128d9aaf7_b.jpg"
  teaser: "https://live.staticflickr.com/65535/55672381423_3128d9aaf7_b.jpg"
categories:
  - SRE
tags:
  - SRE
  - 100daysofsre
  - 100daychallenge
  - devops
  - docker
  - kubernetes
  - containers
  - cloud
toc: true
toc_label: "Table of Contents"
toc_icon: "cloud"
---
So far until now, we have learned how docker-compose can be a go-to tool for deploying and testing containerized applications locally. However, when it comes to enterprise production, we don't use docker-compose. In this post we will learn how Kubernetes replaces docker-compose for enterprise-level production-grade deployment.

Kubernetes (K8s) is an **open-source container orchestration platform** designed to **automate the deployment, scaling, and management of containerized applications**.

It helps organizations **deploy applications at scale**, handle **failures gracefully**, and manage **hundreds or thousands of containers** efficiently.

### Key Features of Kubernetes:
✅ **Self-healing** – Restarts failed containers automatically  
✅ **Auto-scaling** – Adjusts resources based on real-time demand  
✅ **Service discovery & load balancing** – Built-in traffic management  
✅ **Rolling updates & rollbacks** – Ensures zero-downtime deployments  
✅ **Multi-cloud & hybrid-cloud support** – Runs on AWS, GCP, Azure, on-prem, etc.  

---

## 🐳 Kubernetes vs. Docker Compose – Why Kubernetes for Production?

While **Docker Compose** is great for local development, **Kubernetes** is the preferred solution for **enterprise production deployments**.

| Feature              | Docker Compose 🐳  | Kubernetes ☸️  |
|----------------------|------------------|---------------|
| **Scalability**      | Manual scaling  | Auto-scaling based on demand |
| **Load Balancing**   | No built-in support | Integrated Service Load Balancer |
| **Self-Healing**     | Containers crash without auto-restart | Automatically restarts failed pods |
| **High Availability** | Single-node setup | Multi-node cluster setup |
| **Rolling Updates**  | Requires manual intervention | Seamless rolling updates & rollbacks |
| **Cloud-Native**     | Limited to local development | Runs on AWS, GCP, Azure, on-prem |
| **Networking**       | Limited to local Docker network | Advanced networking with Service Mesh (Istio, Cilium) |
| **Storage**         | Simple volume management | Persistent storage across multiple nodes |

💡 **TL;DR:** Docker Compose is great for testing and development, but **Kubernetes is the industry standard for production** because it provides **better automation, scalability, resilience, and multi-cloud support**.

---

## Why Enterprises Choose Kubernetes

### **1️⃣ Handles Large-Scale Deployments**
For companies running **thousands of microservices**, Kubernetes makes scaling effortless with **Horizontal Pod Autoscaling (HPA)**.

Example:
- **[Netflix](https://netflixtechblog.com/kubernetes-and-kernel-panics-ed620b9c6225), [Uber](https://www.uber.com/blog/odin-stateful-platform/), and [Airbnb](https://medium.com/airbnb-engineering/apache-flink-on-kubernetes-84425d66ee11)** use Kubernetes to manage **thousands of microservices** across cloud regions.

### **2️⃣ Built-In High Availability**
Kubernetes runs applications in **multiple replicas** across different nodes, ensuring **zero downtime** even if a node fails.

### **3️⃣ Cloud-Native & Multi-Cloud Ready**
With **AWS EKS, GCP GKE, and Azure AKS**, enterprises can **deploy Kubernetes clusters** without vendor lock-in.

Example:
- **Spotify** migrated from on-prem servers to **Google Kubernetes Engine (GKE)** for better cloud scalability.

### **4️⃣ DevOps & GitOps Friendly**
Kubernetes integrates seamlessly with **CI/CD pipelines** using **ArgoCD, GitHub Actions, and Jenkins** for automated deployments.

Example:
- **Adobe** uses Kubernetes with **ArgoCD for GitOps**, ensuring **secure and automated deployments**.

### **5️⃣ Secure & Policy-Driven**
With tools like **Kubernetes RBAC (Role-Based Access Control), Istio (Service Mesh), and Open Policy Agent (OPA)**, enterprises can enforce **strict security policies**.

---

## Getting Started with Kubernetes Locally
### Option 01: Running Minikube on Host

You can install a lightweight Kubernetes cluster on your local machine using **Minikube** or **Kind**.

* **Install Minikube**
```bash
$ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
$ sudo install minikube-linux-amd64 /usr/local/bin/minikube
$ minikube start
```

* **Deploy a Sample Application**

```bash
$ kubectl create deployment my-app --image=nginx
$ kubectl expose deployment my-app --type=LoadBalancer --port=80
$ minikube service my-app
``` 

### Option 02: Testing Minikube inside docker
Running **Minikube** inside a **Docker container** is not straightforward because Minikube itself requires a virtualization layer (such as Docker, VirtualBox, or KVM) to create a Kubernetes cluster. However, you can run Minikube inside a Docker container using the **none** driver, which runs Kubernetes components directly on the host.

Here's a **Dockerfile** that sets up a containerized environment to run Minikube using Docker as the driver:

----------

#### **Dockerfile for Running Minikube**

```dockerfile
FROM ubuntu:22.04

# Set environment variables
ENV KUBECTL_VERSION=v1.27.3 \
    MINIKUBE_VERSION=v1.30.1

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    conntrack \
    iptables \
    socat \
    ebtables \
    ethtool \
    sudo \
    docker.io \
    && apt-get clean

# Install kubectl
RUN curl -Lo /usr/local/bin/kubectl https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
    chmod +x /usr/local/bin/kubectl

# Install Minikube
RUN curl -Lo /usr/local/bin/minikube https://storage.googleapis.com/minikube/releases/${MINIKUBE_VERSION}/minikube-linux-amd64 && \
    chmod +x /usr/local/bin/minikube

# Create a non-root user
RUN useradd -m minikube && echo "minikube:minikube" | chpasswd && adduser minikube sudo
USER minikube
WORKDIR /home/minikube

# Start Minikube inside the container
CMD ["minikube", "start", "--driver=docker"]
``` 

----------

#### **Build & Run Instructions**

1.  **Build the Docker image**
    
    ```sh
    docker build -t minikube-container .
    ``` 
    
2.  **Run the container with proper privileges**
    
    ```sh
    docker run --privileged -v /var/run/docker.sock:/var/run/docker.sock -it minikube-container
    ``` 
    


#### **Explanation**

-   **Installs Minikube and kubectl**: Necessary for running Kubernetes.
-   **Uses Docker as a driver**: Minikube will run its Kubernetes cluster inside Docker.
-   **Non-root user setup**: Helps prevent permission issues.
-   **Maps Docker socket (`/var/run/docker.sock`)**: Allows Minikube to create Docker containers inside the host.

----------

## When Should You Use Kubernetes?

| Scenario                  | Use Docker Compose 🐳 | Use Kubernetes ☸️ |
|---------------------------|----------------------|------------------|
| **Local Development**     | ✅ Yes              | ❌ No            |
| **Small-Scale Apps**      | ✅ Yes              | ⚠️ Maybe         |
| **Enterprise Production** | ❌ No               | ✅ Yes           |
| **Multi-Cloud Deployments** | ❌ No            | ✅ Yes           |
| **High Availability Needed** | ❌ No          | ✅ Yes           |
| **Auto-Scaling Required** | ❌ No               | ✅ Yes           |

---

## How Kubernetes is Replacing Traditional Infrastructure  

Kubernetes is **revolutionizing IT infrastructure** by shifting organizations from traditional **physical servers and IaaS (Infrastructure-as-a-Service) to modern, container-based deployments**. Here’s how:

1️⃣ **From Monolith to Microservices**:  
   - Legacy applications are being **refactored into microservices** using Kubernetes, allowing **faster development, deployment, and scaling**.

2️⃣ **Replacing Physical Servers & VMs**:  
   - Instead of managing **dedicated physical servers or virtual machines (VMs)**, companies are deploying applications in **lightweight, scalable Kubernetes pods**.

3️⃣ **Auto-Scaling & Dynamic Resource Allocation**:  
   - Unlike traditional IaaS where **resources are statically allocated**, Kubernetes uses **Horizontal Pod Autoscaling (HPA)** to adjust based on demand, optimizing costs.

4️⃣ **Cloud-Agnostic Deployments**:  
   - Kubernetes abstracts the underlying infrastructure, enabling **seamless workload portability** across **AWS, GCP, Azure, and on-prem**.

5️⃣ **Modernizing Legacy Apps Without Rewriting**:  
   - Using Kubernetes and **containerization (Docker)**, enterprises can **package legacy applications** into containers, **eliminating dependencies on outdated OS or hardware**.

6️⃣ **Enhanced Reliability & Zero Downtime Deployments**:  
   - Kubernetes' **rolling updates, automatic failover, and self-healing capabilities** ensure applications remain available **without manual intervention**.

💡 **The Future**: Traditional infrastructure is being phased out as Kubernetes becomes the **de facto standard** for managing **cloud-native, scalable, and resilient applications** in **modern enterprises**.

----------

## Remarks

**Docker Compose** is great for **local development and small projects**, but **Kubernetes** is the **best choice for production**, especially for **enterprise-scale applications**.

✅ **Kubernetes is built for automation, scalability, and reliability.**  
✅ **It’s cloud-native and supports multi-cloud & hybrid-cloud deployments.**  
✅ **Enterprises trust Kubernetes for mission-critical workloads.**

When I first develop a backend or frontend, docker-compose is my go-to solution. You will find many docker-compose projects on my [GitHub](https://github.com/shantoroy). However, when it comes to production, we definitely need to use Kubernetes. I have collected some templates from high-starred github repos and putting in one on [Kubernetes Template Collections](https://github.com/shantoroy/kubernetes-yaml-templates). 

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI1MzMzNTg1NywxNTI5MjYwNDE1LDE3MD
c2NzEwNjVdfQ==
-->