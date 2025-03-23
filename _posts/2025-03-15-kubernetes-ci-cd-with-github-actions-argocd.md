---
layout: single
title: "#100DaysOfSRE (Day 35): Kubernetes CI/CD Pipeline with GitHub Actions & ArgoCD"
excerpt: "Learn how to set up a CI/CD pipeline for Kubernetes using GitHub Actions and ArgoCD to automate deployments."
seo_title: "Kubernetes CI/CD with GitHub Actions & ArgoCD"
seo_description: "Step-by-step guide to setting up a Kubernetes CI/CD pipeline using GitHub Actions and ArgoCD, automating deployments with GitOps."
header:
  image: "https://live.staticflickr.com/65535/53398463283_8c0c36b11f_o.png"
  teaser: "https://live.staticflickr.com/65535/53398463283_8c0c36b11f_o.png"
categories:
  - Kubernetes
tags:
  - Kubernetes
  - DevOps
  - CI/CD
  - GitHub Actions
  - ArgoCD
  - GitOps
  - SRE
toc: true
toc_label: "Table of Contents"
toc_icon: "rocket"
---

Combining  **GitHub Actions**  and  **Argo CD**  for CI/CD on Kubernetes is a powerful and modern approach that leverages the strengths of both tools. Here's why this combination is a proper choice:

----------

##  **GitHub Actions for CI (Continuous Integration)**

GitHub Actions is a robust CI/CD platform integrated directly into GitHub repositories. It excels at automating build, test, and packaging workflows. Here's why it's great for CI:

#### a.  **Tight Integration with GitHub**

-   GitHub Actions is natively integrated into GitHub, making it easy to trigger workflows based on repository events (e.g., push, pull request, release).
    
-   No need for external CI tools; everything is managed within GitHub.
    

#### b.  **Extensive Ecosystem**

-   GitHub Actions has a large marketplace of prebuilt actions for common tasks (e.g., building Docker images, running tests, deploying to cloud providers).
    
-   You can easily extend workflows with custom actions.
    

#### c.  **Scalability**

-   GitHub Actions supports parallel jobs and matrix builds, enabling efficient testing across multiple environments or configurations.
    

#### d.  **Artifact Management**

-   GitHub Actions can build and push Docker images to container registries (e.g., Docker Hub, GitHub Container Registry, AWS ECR).
    
-   It can also generate and store build artifacts (e.g., binaries, Helm charts).
---

##  **Why Combine GitHub Actions and Argo CD?**

#### a.  **Separation of Concerns**

-   **GitHub Actions**  handles the CI part: building, testing, and packaging applications.
    
-   **Argo CD**  handles the CD part: deploying and managing applications in Kubernetes.
    
-   This separation ensures that each tool focuses on its strengths.
    

#### b.  **End-to-End Automation**

-   GitHub Actions can trigger Argo CD to deploy applications after a successful build.
    
-   This creates a fully automated pipeline from code commit to production deployment.
    

#### c.  **GitOps Workflow**

-   GitHub Actions pushes changes (e.g., Docker images, Helm charts) to Git repositories.
    
-   Argo CD picks up these changes and deploys them to Kubernetes, ensuring a GitOps workflow.
    

#### d.  **Scalability and Flexibility**

-   GitHub Actions scales well for CI tasks, while Argo CD scales for managing complex Kubernetes deployments.
    
-   Both tools are highly flexible and can be customized to fit your workflow.
    

#### e.  **Auditability and Traceability**

-   All changes are tracked in Git, providing a clear audit trail and enabling rollbacks.
    
-   GitHub Actions logs and Argo CD's synchronization history provide visibility into the pipeline.
    

----------

### 4.  **Example Workflow: GitHub Actions + Argo CD**

Here’s how the two tools can work together in a CI/CD pipeline:

1.  **Code Push**:
    
    -   A developer pushes code to the  `main`  branch in GitHub.
        
2.  **GitHub Actions CI**:
    
    -   GitHub Actions triggers a CI workflow:
        
        -   Builds the application.
            
        -   Runs tests.
            
        -   Builds and pushes a Docker image to a container registry.
            
        -   Updates the Kubernetes manifests (e.g., Helm chart) in the Git repository with the new image tag.
            
3.  **Argo CD CD**:
    
    -   Argo CD detects changes in the Git repository.
        
    -   It syncs the new application state to the Kubernetes cluster.
        
    -   The application is deployed to the desired environment (e.g., staging or production).


Alright, now, let's set up both for an example Kubernetes environment.

---

## Set up CI/CD Pipeline
###  Step 1: Set Up Your Kubernetes & ArgoCD Environment

Before starting, ensure you have:  

✅ **A Kubernetes cluster (Minikube, Kind, EKS, GKE, AKS, etc.)**  
✅ **ArgoCD installed in your cluster ([Day 34 Guide](https://shantoroy.com/kubernetes/kubernetes-deployment-with-argocd-gitops/))**  
✅ **A GitHub repository with Kubernetes manifests**  

---

### Step 2: Create a GitHub Actions Workflow for CI

#### ** Create `.github/workflows/ci.yaml`**
This **CI pipeline** will:  
- Build and tag a Docker image  
- Push it to **GitHub Container Registry (GHCR) or Docker Hub**  

 **`.github/workflows/ci.yaml`**
```yaml
name: CI - Build & Push Docker Image

on:
  push:
    branches:
      - main
    paths:
      - "app/**"  # Only trigger when app code changes

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Log in to GitHub Container Registry
        run: echo "${{ secrets.GHCR_PAT }}" | docker login ghcr.io -u ${{ github.actor }} --password-stdin

      - name: Build Docker Image
        run: docker build -t ghcr.io/${{ github.repository }}/myapp:${{ github.sha }} -f app/Dockerfile .

      - name: Push Image to GHCR
        run: docker push ghcr.io/${{ github.repository }}/myapp:${{ github.sha }}
```

 **Set up GitHub Secrets**:

-   `GHCR_PAT`: **GitHub Container Registry Personal Access Token**
-   `DOCKERHUB_USERNAME`, `DOCKERHUB_PASSWORD`: (if using Docker Hub instead)

----------

###  Step 3: Automate Kubernetes Deployment with CD

#### ** Create `.github/workflows/cd.yaml`**

This workflow:

-   Updates Kubernetes **manifests** with the new image tag
-   Pushes changes to the **GitOps repository**
-   ArgoCD automatically syncs and deploys the new version 

 **`.github/workflows/cd.yaml`**

```yaml
name: CD - Deploy to Kubernetes via ArgoCD

on:
  workflow_run:
    workflows: ["CI - Build & Push Docker Image"]
    types:
      - completed

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout GitOps Repository
        uses: actions/checkout@v3
        with:
          repository: <your-gitops-repo>
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Update Kubernetes Deployment YAML
        run: |
          sed -i "s|image: .*|image: ghcr.io/${{ github.repository }}/myapp:${{ github.sha }}|" k8s/deployment.yaml

      - name: Commit and Push Changes
        run: |
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add k8s/deployment.yaml
          git commit -m "Update deployment image to ${{ github.sha }}"
          git push

``` 

 **How It Works?**

1.  **CI Workflow** builds & pushes the Docker image.
2.  **CD Workflow** updates `deployment.yaml` with the new image tag.
3.  **ArgoCD auto-syncs the changes and deploys the updated version.**

----------

###  Step 4: Create an ArgoCD Application for GitOps

ArgoCD watches your Git repository and applies changes automatically.

 **`argocd-application.yaml`**

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/<your-gitops-repo>.git
    targetRevision: main
    path: k8s
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

----------

###  Step 5: Test the Pipeline

#### **1️⃣ Make a Code Change**

Modify `app/main.py` and push changes to `main`:

```sh
git commit -am "Update application logic" git push origin main
``` 

#### **2️⃣ Observe CI/CD Pipeline**

-   GitHub Actions runs the **CI workflow** → Builds & pushes Docker image
-   GitHub Actions runs the **CD workflow** → Updates `deployment.yaml`
-   ArgoCD **auto-syncs & deploys** the updated application 

#### **3️⃣ Verify Deployment**

```sh
kubectl get pods
kubectl get svc
``` 

Check your **ArgoCD UI** → The new version is deployed automatically! 

----------

## Final Thoughts


 **Key Takeaways**  
✅ **CI/CD with GitHub Actions + ArgoCD enables fully automated Kubernetes deployments**  
✅ **GitOps approach ensures consistency, security, and easy rollbacks**  
✅ **ArgoCD eliminates manual `kubectl apply` commands**  
✅ **Scalable CI/CD for cloud-native applications**

**Alternatives**
While GitHub Actions and Argo CD are a great combination, here are some alternatives:

-   **Jenkins + Argo CD**: Use Jenkins for CI and Argo CD for CD.
    
-   **GitLab CI/CD + Argo CD**: Use GitLab CI/CD for CI and Argo CD for CD.
    
-   **Tekton + Argo CD**: Use Tekton for CI and Argo CD for CD.

Combining **GitHub Actions** for CI and **Argo CD** for CD is a proper choice for Kubernetes-based CI/CD pipelines. It provides a seamless, automated, and GitOps-driven workflow that ensures consistency, scalability, and visibility. This combination is particularly well-suited for teams already using GitHub and looking to adopt modern DevOps practices.

 **What’s Next?**  
🔹 **Day 36**: Kubernetes Helm Charts 
🔹 **Day 37**: Kubernetes Deployment using Terraform
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTUwOTM0NTg1OV19
-->