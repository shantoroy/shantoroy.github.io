---
layout: single
title: "#100DaysOfSRE (Day 34): Automating Kubernetes Deployments with ArgoCD & GitOps"
excerpt: "Learn how to automate Kubernetes deployments using ArgoCD and GitOps principles for continuous delivery."
seo_title: "ArgoCD & GitOps: Automating Kubernetes Deployments"
seo_description: "A step-by-step guide to using ArgoCD for Kubernetes deployments with GitOps, ensuring consistency, automation, and version control."
header:
  image: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
  teaser: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
categories:
  - Kubernetes
tags:
  - Kubernetes
  - DevOps
  - ArgoCD
  - GitOps
  - CI/CD
  - SRE
toc: true
toc_label: "Table of Contents"
toc_icon: "rocket"
---

**Argo CD**  is a popular GitOps tool for managing Kubernetes applications. It provides a declarative way to deploy and manage applications using Git as the single source of truth. Here are the key reasons why Argo CD is widely used:

----------

#### 1.  **GitOps Principles**

-   **Declarative Configuration**: Argo CD uses YAML manifests stored in Git repositories to define the desired state of applications.
    
-   **Version Control**: All changes are tracked in Git, providing a clear audit trail and enabling rollbacks.
    
-   **Automation**: Argo CD continuously monitors the Git repository and automatically syncs the cluster state with the desired state.
    

#### 2.  **Continuous Delivery**

-   Argo CD ensures that the Kubernetes cluster is always in sync with the desired state defined in Git.
    
-   It supports automated deployments, reducing manual intervention and human error.
    

#### 3.  **Multi-Environment Support**

-   Argo CD can manage applications across multiple environments (e.g., dev, staging, production) using the same Git repository.
    

#### 4.  **Self-Healing**

-   If the cluster state drifts from the desired state (e.g., due to manual changes), Argo CD can automatically correct it.
    

#### 5.  **User Interface**

-   Argo CD provides a web-based UI for visualizing applications, their status, and synchronization state.
    

#### 6.  **Integration with Kubernetes Ecosystem**

-   Argo CD integrates seamlessly with Helm, Kustomize, and other Kubernetes tools.
    
-   It supports multi-cluster deployments and can manage applications across multiple Kubernetes clusters.


Today, we’ll **set up ArgoCD, deploy an app using GitOps, and automate Kubernetes deployments.**

---

##  Step 1: Install ArgoCD in Kubernetes

Deploy ArgoCD in the `argocd` namespace:
```sh
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Wait for the pods to be ready:

```sh
kubectl get pods -n argocd
``` 

Expose the ArgoCD UI:

```sh
kubectl port-forward svc/argocd-server -n argocd 8080:443
``` 

Now, access **ArgoCD UI at**: https://localhost:8080

----------

##  Step 2: Login & Change ArgoCD Admin Password

Fetch the **default admin password**:

```sh
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d
``` 

Login to ArgoCD CLI:

```sh
argocd login localhost:8080 --username admin --password <your-password>
``` 

Change the password:

```sh
argocd account update-password
``` 

----------

##  Step 3: Deploy an App Using GitOps

### 1️⃣ **Prepare the Git Repository**

Create a **GitHub repository** (e.g., `k8s-gitops-demo`) with the following structure:

```text
k8s-gitops-demo/
├── manifests/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
└── .gitignore
``` 

### 2️⃣ **Define Kubernetes Manifests**

 **manifests/deployment.yaml**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: nginx:latest
        ports:
        - containerPort: 80
``` 

 **manifests/service.yaml**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
``` 

### 3️⃣ **Push Code to Git**

```sh
git init
git add .
git commit -m "Initial Kubernetes manifests" git branch -M main
git remote add origin https://github.com/<your-username>/k8s-gitops-demo.git
git push -u origin main
``` 

----------

##  Step 4: Create an ArgoCD Application

Create an ArgoCD **Application** that syncs with your Git repository.

 **argocd-application.yaml**

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/<your-username>/k8s-gitops-demo.git
    targetRevision: main
    path: manifests
  destination:
    server: https://kubernetes.default.svc
    namespace: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
``` 

Apply it:

```sh
kubectl apply -f argocd-application.yaml
``` 

Check the app status:

```sh
argocd app list
``` 

Verify deployment:

```sh
kubectl get pods
kubectl get svc
```

----------

##  Step 5: Automate Deployments with GitOps

1️⃣ **Make a Change in Git**  
Modify `deployment.yaml` to use a different image (e.g., `nginx:1.23`).  
Commit & push the change:

```sh
git commit -am "Updated image version" git push origin main
``` 

2️⃣ **ArgoCD Auto-Syncs Changes**  
Check the ArgoCD UI—your deployment will **automatically update!** 

----------

##  Step 6: Rollback with ArgoCD

If a deployment breaks, rollback easily:

```sh
argocd app history myapp
argocd app rollback myapp 2
``` 

Now, the app is restored to version `2`.

----------

## Remarks

 **Key Takeaways**  
✅ **ArgoCD automates Kubernetes deployments using Git**  
✅ **GitOps ensures consistency, auditability, and automation**  
✅ **Auto-sync eliminates manual `kubectl apply` commands**  
✅ **Rollback instantly using ArgoCD commands**

 **What’s Next?**  
🔹 **Day 35**: Kubernetes CI/CD Pipeline with GitHub Actions & ArgoCD  
🔹 **Day 36**: Securing Kubernetes Workloads with Network Policies
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMDc2NTU3MzRdfQ==
-->