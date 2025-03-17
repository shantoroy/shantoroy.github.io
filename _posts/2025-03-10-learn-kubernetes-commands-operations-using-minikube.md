---
layout: single
title: "#100daysofSRE (Day 30): Learn Kubernetes Commands and Operations using Minikube"
excerpt: "Master Kubernetes with Minikube! This post provides a cheatsheet of essential commands and walks through real-world scenarios to help you practice deployments, scaling, troubleshooting, and networking in a local Kubernetes environment."
seo_title: "Learn Kubernetes Commands and Operations using Minikube"
seo_description: "A practical guide to Kubernetes commands and operations using Minikube. Includes essential commands, scenario-based examples, and step-by-step troubleshooting for Kubernetes beginners and SREs."
header:
  image: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
  teaser: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
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


Minikube is an excellent tool to **practice Kubernetes operations** in a local environment. This post provides a **cheatsheet** of essential commands followed by **scenario-based examples** to simulate real-world Kubernetes tasks.  

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

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NzM0NDE5NTFdfQ==
-->