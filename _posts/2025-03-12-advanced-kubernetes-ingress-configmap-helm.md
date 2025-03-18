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

### **Define an Ingress Resource**

 **ingress.yaml**

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  namespace: myapp
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.local
    http:
      paths:
      - path: /backend
        pathType: Prefix
        backend:
          service:
            name: backend
            port:
              number: 5000
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend
            port:
              number: 3000
``` 

### **Apply the Ingress Configuration**

```sh
kubectl apply -f ingress.yaml
``` 

### **Test the Ingress**

Update `/etc/hosts` (Linux/macOS) to map `myapp.local` to Minikube’s IP:

```sh
echo  "$(minikube ip) myapp.local" | sudo tee -a /etc/hosts
``` 

Now, visit **http://myapp.local/** for the frontend and **http://myapp.local/backend** for the backend!

----------

##  Step 2: Use ConfigMaps & Secrets for Secure Configuration

Instead of **hardcoding** environment variables, we will use **ConfigMaps** and **Secrets**.

### **Create a ConfigMap for Database URL**

 **configmap.yaml**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: myapp
data:
  DATABASE_URL: "postgresql://user:password@postgres:5432/mydatabase"
``` 

### **Create a Secret for Database Credentials**

 **secret.yaml**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
  namespace: myapp
type: Opaque
data:
  POSTGRES_USER: dXNlcg==  # Base64 encoded 'user'
  POSTGRES_PASSWORD: cGFzc3dvcmQ=  # Base64 encoded 'password'
``` 

### **Modify Backend Deployment to Use ConfigMap & Secret**

 **backend-deployment.yaml**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
  namespace: myapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: python:3.10
        env:
        - name: DATABASE_URL
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: DATABASE_URL
        - name: POSTGRES_USER
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: POSTGRES_USER
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: POSTGRES_PASSWORD
        ports:
        - containerPort: 5000
``` 

### **Apply ConfigMaps & Secrets**

```sh
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f backend-deployment.yaml
``` 

----------

##  Step 3: Use Helm Charts for Deployment Management

Manually managing Kubernetes YAML files is **tedious**. Instead, we can use **Helm**, the package manager for Kubernetes.

### **Install Helm**

```sh
brew install helm # macOS 
choco install kubernetes-helm # Windows
``` 

### **Create a Helm Chart**

```sh
helm create myapp-chart
``` 

### **Modify Helm Chart to Deploy the App**

Inside `myapp-chart/values.yaml`, update the service and deployment values.

 **myapp-chart/values.yaml**

```yaml
backend:
  image: python:3.10
  service:
    type: ClusterIP
    port: 5000

frontend:
  image: node:18
  service:
    type: ClusterIP
    port: 3000

database:
  image: postgres:15
  service:
    type: ClusterIP
    port: 5432
  env:
    POSTGRES_USER: user
    POSTGRES_PASSWORD: password
    POSTGRES_DB: mydatabase
``` 

### **Deploy the Application using Helm**

```sh
helm install myapp ./myapp-chart
``` 

### **Check the Helm Deployment**

```sh
helm list
kubectl get pods -n myapp
``` 

### **Upgrade the Helm Release**

If you modify the configuration:

```sh
helm upgrade myapp ./myapp-chart
``` 

### **Uninstall the Helm Release**

```sh
helm uninstall myapp
``` 

----------

## Final Thoughts

**Key Takeaways**  
✅ **Ingress Controllers** expose applications externally with routing rules  
✅ **ConfigMaps & Secrets** store environment variables securely  
✅ **Helm** simplifies Kubernetes deployments with reusable charts

 **What’s Next?**  
🔹 **Day 33**: Monitoring Kubernetes Apps with Prometheus & Grafana  
🔹 **Day 34**: CI/CD Pipelines for Kubernetes Deployments

 **Stay tuned for more Kubernetes posts in the #100DaysOfSRE series!**

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMTgxNDg4NzgsLTE4MDAyNzIzMl19
-->