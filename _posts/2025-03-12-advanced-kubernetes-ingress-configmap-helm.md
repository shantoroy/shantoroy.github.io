---
layout: single
title: "#100DaysOfSRE (Day 32): Advanced Kubernetes: Ingress, ConfigMaps, Secrets & Helm"
excerpt: "Take your Kubernetes skills to the next level by adding Ingress for routing, ConfigMaps & Secrets for secure configuration, and Helm Charts for deployment."
seo_title: "Advanced Kubernetes: Ingress, ConfigMaps, Secrets & Helm"
seo_description: "Learn how to enhance your Kubernetes setup with Ingress, ConfigMaps, Secrets, and Helm Charts. Secure and manage your applications effectively."
header:
  image: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
  teaser: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
categories:
  - Kubernetes
tags:
  - Kubernetes
  - Ingress
  - ConfigMaps
  - Secrets
  - Helm
  - SRE
toc: true
toc_label: "Table of Contents"
toc_icon: "rocket"
---


In **Day 31**, we deployed a **Python-based backend, frontend, and PostgreSQL database** on Minikube using Kubernetes manifests. Now, let’s **enhance** our setup by adding:

✅ **Ingress Controller** for external access  
✅ **ConfigMaps & Secrets** for secure configuration  
✅ **Helm Charts** for easier deployment management  

---

## Step 1: Add an Ingress Controller for External Access

By default, Kubernetes services are **only accessible inside the cluster**. Instead of using `NodePort`, we will configure an **Ingress Controller** to route requests.

### **Install Ingress Controller on Minikube**
```sh
minikube addons enable ingress
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMwOTE5MzUxNF19
-->