---
layout: single
title: "#100daysofSRE (Day 30): Learn Kubernetes Commands and Operations using Minikube"
excerpt: "Master Kubernetes with Minikube! This post provides a cheatsheet of essential commands and walks through real-world scenarios to help you practice deployments, scaling, troubleshooting, and networking in a local Kubernetes environment."
seo_title: "Learn Kubernetes Commands and Operations using Minikube"
seo_description: "A practical guide to Kubernetes commands and operations using Minikube. Includes essential commands, scenario-based examples, and step-by-step troubleshooting for Kubernetes beginners and SREs."
header:
  image: "https://live.staticflickr.com/65535/55672381423_3128d9aaf7_b.jpg"
  teaser: "https://live.staticflickr.com/65535/55672381423_3128d9aaf7_b.jpg"
categories:
  - Kubernetes
tags:
  - Kubernetes
  - Minikube
  - DevOps
  - SRE
  - Containers
toc: true
toc_label: "Table of Contents"
toc_icon: "rocket"
---


Minikube is an excellent tool to **practice Kubernetes operations** in a local environment. 

This post provides a **cheatsheet** of essential commands followed by **scenario-based examples** to simulate real-world Kubernetes tasks.  

---

##  Kubernetes Command Cheatsheet  

### 🔹 Minikube Management  

| Task                     | Command |
|--------------------------|---------|
| Start Minikube cluster   | `minikube start` |
| Stop Minikube            | `minikube stop` |
| Delete Minikube cluster  | `minikube delete` |
| Check Minikube status    | `minikube status` |
| Open Minikube dashboard  | `minikube dashboard` |

### 🔹 Cluster & Node Information  

| Task                          | Command |
|--------------------------------|---------|
| View cluster information       | `kubectl cluster-info` |
| Get all nodes                  | `kubectl get nodes` |
| Describe a node                 | `kubectl describe node <node-name>` |

### 🔹 Managing Pods  

| Task                           | Command |
|---------------------------------|---------|
| List all running pods          | `kubectl get pods` |
| Describe a specific pod         | `kubectl describe pod <pod-name>` |
| View pod logs                   | `kubectl logs <pod-name>` |
| Execute a command inside a pod  | `kubectl exec -it <pod-name> -- /bin/sh` |
| Delete a pod                    | `kubectl delete pod <pod-name>` |

### 🔹 Managing Deployments  

| Task                               | Command |
|------------------------------------|---------|
| List all deployments               | `kubectl get deployments` |
| Scale deployment replicas           | `kubectl scale deployment <deployment-name> --replicas=3` |
| Update an existing deployment       | `kubectl rollout restart deployment <deployment-name>` |
| Undo a deployment rollback          | `kubectl rollout undo deployment <deployment-name>` |

### 🔹 Exposing Services  

| Task                                    | Command |
|----------------------------------------|---------|
| List all services                      | `kubectl get services` |
| Expose a deployment via NodePort       | `kubectl expose deployment <deployment-name> --type=NodePort --port=80` |
| Get Minikube service URL               | `minikube service <service-name> --url` |

---

## Scenario-Based Kubernetes Operations in Minikube  

### **Scenario 1: Deploy a Simple Web Application**  
**Goal**: Deploy an Nginx web server and expose it via a service.

#### **Steps**:  
1️⃣ Create a deployment for **Nginx**  
```sh
kubectl create deployment nginx --image=nginx --replicas=2
```

2️⃣ Expose the deployment as a **NodePort** service

```sh
kubectl expose deployment nginx --type=NodePort --port=80
``` 

3️⃣ Get the external service URL using Minikube

```sh
minikube service nginx --url
``` 

4️⃣ Open the application in a browser

```sh
minikube service nginx
``` 

----------

### **Scenario 2: Scale an Application Dynamically**

**Goal**: Scale the Nginx deployment from 2 to 5 replicas.

#### **Steps**:

1️⃣ Check current pods

```sh
kubectl get pods
``` 

2️⃣ Scale deployment

```sh
kubectl scale deployment nginx --replicas=5
``` 

3️⃣ Verify the scaling

```sh
kubectl get pods
``` 

----------

### **Scenario 3: Rolling Update & Rollback**

**Goal**: Update the Nginx version and roll it back if something goes wrong.

#### **Steps**:

1️⃣ Check the current deployment

```sh
kubectl get deployments
``` 

2️⃣ Update the deployment to use **nginx:1.23**

```sh
kubectl set image deployment/nginx nginx=nginx:1.23
``` 

3️⃣ Check the rollout status

```sh
kubectl rollout status deployment/nginx
``` 

4️⃣ If the new version is unstable, rollback

```sh
kubectl rollout undo deployment/nginx
``` 

----------

### **Scenario 4: Debugging a Failing Pod**

**Goal**: Troubleshoot a pod that is stuck in `CrashLoopBackOff`.

#### **Steps**:

1️⃣ List pods and find the problematic one

```sh
kubectl get pods
``` 

2️⃣ Check pod logs

```sh
kubectl logs <pod-name>
``` 

3️⃣ Describe the pod for detailed information

```sh
kubectl describe pod <pod-name>
``` 

4️⃣ Get into the pod’s shell (if running)

```sh
kubectl exec -it <pod-name> -- /bin/sh
``` 

5️⃣ Delete and restart the pod

```sh
kubectl delete pod <pod-name>
``` 

----------

### **Scenario 5: Deploying a Multi-Tier App with Minikube**

**Goal**: Deploy a **frontend and backend** in Kubernetes.

#### **Steps**:

1️⃣ Deploy a **backend API**

```sh
kubectl create deployment backend --image=python:3.10-slim
``` 

2️⃣ Expose backend via a **ClusterIP**

```sh
kubectl expose deployment backend --port=5000 --type=ClusterIP
``` 

3️⃣ Deploy a **React frontend**

```sh
kubectl create deployment frontend --image=node:18-alpine
``` 

4️⃣ Expose frontend as a **LoadBalancer**

```sh
kubectl expose deployment frontend --port=3000 --type=LoadBalancer
``` 

5️⃣ Get the service URL

```sh
minikube service frontend
``` 

**Now we have a full-stack app running in Kubernetes!**

----------

## Remarks

Minikube is a powerful tool for **learning and testing Kubernetes commands** in a local environment. 

By practicing these **scenario-based tasks**, we can become comfortable with **real-world Kubernetes operations** before deploying in production.

**Key Takeaways**

-   Minikube helps you **test Kubernetes locally**.
-   You can create, scale, and troubleshoot applications easily.
-   Kubernetes commands allow **rolling updates, service exposure, and debugging** in a structured way.

**Next Steps**

-   Try deploying **stateful applications** with **Persistent Volumes**.
-   Experiment with **Ingress controllers** in Minikube.
-   Learn about **Kubernetes Helm Charts** for app deployment automation.

**Stay tuned for more Kubernetes posts in the #100DaysOfSRE series!**
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTI4Njc0OTU0XX0=
-->