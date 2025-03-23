---
layout: single
title: "#100DaysOfSRE (Day 36): Kubernetes Helm Charts – Package & Deploy Applications"
excerpt: "Learn how to use Helm Charts for managing Kubernetes applications efficiently."
seo_title: "Kubernetes Helm Charts – Package & Deploy Applications"
seo_description: "Step-by-step guide to Kubernetes Helm Charts, packaging applications, and deploying them in a reproducible way."
header:
  image: "https://live.staticflickr.com/65535/53398563283_8c0c36b11f_o.png"
  teaser: "https://live.staticflickr.com/65535/53398563283_8c0c36b11f_o.png"
categories:
  - Kubernetes
tags:
  - Kubernetes
  - Helm
  - DevOps
  - SRE
  - CI/CD
  - Kubernetes Package Management
toc: true
toc_label: "Table of Contents"
toc_icon: "package"
---




[Helm](https://helm.sh/)  is a package manager for Kubernetes that simplifies the deployment and management of applications. Helm uses  **Helm charts**, which are collections of preconfigured Kubernetes resources (e.g., deployments, services, config maps) packaged together. Here’s why Helm charts are beneficial for Kubernetes application deployment:

----------

#### 1.  **Simplifies Application Deployment**

-   Helm charts provide a single, versioned package for deploying complex applications.
    
-   Instead of managing multiple YAML files, you can deploy an application with a single command:
    
    ```bash
    helm install my-app ./my-chart
    ```
    

#### 2.  **Reusability**

-   Helm charts are reusable across environments (e.g., dev, staging, production).
    
-   You can create a chart once and use it for multiple deployments with different configurations.
    

#### 3.  **Parameterization**

-   Helm charts support  **values.yaml**  files, which allow you to customize deployments without modifying the chart itself.
    
-   Example:
    
    ```yaml
    # values.yaml
    replicaCount: 3
    image:
      repository: my-app
      tag: latest
     ```
    
-   You can override these values during installation:
    
    ```bash
    helm install my-app ./my-chart --set replicaCount=5
    ```
    

#### 4.  **Versioning**

-   Helm charts are versioned, making it easy to roll back to a previous version if something goes wrong:
    
    ```bash
    helm rollback my-app 1.0.0
    ```
    

#### 5.  **Dependency Management**

-   Helm charts can define dependencies on other charts, simplifying the deployment of multi-component applications.
    
-   Example: A web application chart might depend on a Redis or PostgreSQL chart.
    

#### 6.  **Community and Ecosystem**

-   Helm has a large community and a rich ecosystem of prebuilt charts available in the  [Artifact Hub](https://artifacthub.io/).
    
-   You can use these charts to deploy popular applications (e.g., Prometheus, Grafana, WordPress) with minimal effort.
    

#### 7.  **Standardization**

-   Helm provides a standardized way to package and deploy applications, making it easier for teams to collaborate and share configurations.
    

#### 8.  **Lifecycle Management**

-   Helm supports lifecycle hooks (e.g., pre-install, post-upgrade) to execute custom logic during deployment.

---

## Usability
### **Example Workflow with Helm**

1.  Develop a Helm chart for your application.
    
2.  Store the chart in a version control system (e.g., Git).
    
3.  Use Helm to deploy the application to different environments (e.g., dev, staging, production) with environment-specific configurations.
    
4.  Monitor and update the application using Helm's upgrade and rollback features.

### **Challenges of Not Using Helm Charts**

1.  Manual YAML Management:
    
    -   Without Helm, teams must manually manage multiple YAML files for deployments, services, config maps, etc.
        
    -   This can be error-prone and time-consuming, especially for complex applications.
        
2.  Lack of Standardization:
    
    -   Each team might use its own approach to deploying applications, leading to inconsistencies and inefficiencies.
        
3.  Difficulty in Reusability:
    
    -   Without Helm, reusing configurations across environments or applications becomes challenging, leading to duplication of effort.
        
4.  No Versioning:
    
    -   Without Helm, there’s no built-in versioning for application configurations, making it harder to track changes and roll back to previous versions.
        
5.  Complex Dependency Management:
    
    -   Managing dependencies (e.g., databases, message queues) becomes more complex without Helm’s dependency management features.
        
6.  Limited Ecosystem Integration:
    
    -   Without Helm, companies miss out on the rich ecosystem of prebuilt charts and community support.
        

### **Example Workflow Without Helm**

1.  Manually create and manage YAML files for each Kubernetes resource.
    
2.  Copy and modify YAML files for different environments, increasing the risk of errors.
    
3.  Deploy applications using  `kubectl apply`:
    
    ```bash
    kubectl apply -f deployment.yaml -f service.yaml -f configmap.yaml
    ```
    
4.  Manually track changes and roll back deployments if necessary.


### When Should a Company Use Helm Charts?

-   **Complex Applications**: If your application has multiple components (e.g., microservices, databases, message queues), Helm simplifies deployment and management.
    
-   **Multi-Environment Deployments**: If you deploy applications to multiple environments (e.g., dev, staging, production), Helm ensures consistency and reusability.
    
-   **Frequent Updates**: If your application requires frequent updates, Helm’s versioning and rollback features are invaluable.
    
-   **Team Collaboration**: If multiple teams are involved in deploying and managing applications, Helm provides a standardized approach.

---

## Hands-on
###  Step 1: Install Helm

Ensure Helm is installed before proceeding.

```sh
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

Verify the installation:

```sh
helm version
``` 

----------

###  Step 2: Create a Helm Chart

Let's create a Helm chart for a simple **Node.js app with PostgreSQL**.

```sh
helm create myapp cd myapp
``` 

This creates a folder structure like:

```pgsql
myapp/
├── charts/
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── _helpers.tpl
│   ├── NOTES.txt
├── values.yaml
├── Chart.yaml
``` 

----------

### Step 3: Define Application Configuration

Modify `Chart.yaml` with details:

 **`Chart.yaml`**

```yaml
apiVersion: v2
name: myapp
description: A Helm chart for deploying a Node.js app with PostgreSQL
version: 1.0.0
appVersion: "1.0"
``` 

 **`values.yaml`** (customizable settings)

```yaml
replicaCount: 2

image:
  repository: mydockerhub/myapp
  tag: latest
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: false

postgresql:
  enabled: true
  username: admin
  password: secret
  database: myappdb
``` 

----------

###  Step 4: Define Kubernetes Resources

 **`templates/deployment.yaml`**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-app
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}
    spec:
      containers:
      - name: myapp
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: 3000
``` 

 **`templates/service.yaml`**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Release.Name }}-service
spec:
  type: {{ .Values.service.type }}
  selector:
    app: {{ .Release.Name }}
  ports:
    - protocol: TCP
      port: {{ .Values.service.port }}
      targetPort: 3000
``` 

----------

###  Step 5: Deploy the Helm Chart

#### **1️⃣ Package the Chart**

```sh
helm package myapp
``` 

#### **2️⃣ Install the Chart**

```sh
helm install myapp ./myapp
``` 

#### **3️⃣ List Deployed Charts**

```sh
helm list
``` 

#### **4️⃣ Check Running Services**

```sh
kubectl get pods
kubectl get svc
``` 

#### **5️⃣ Uninstall the Chart**

```sh
helm uninstall myapp
``` 

----------

###  Step 6: Helm Repositories & Chart Distribution

#### **1️⃣ Add a Helm Repository**

```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
helm search repo bitnami
``` 

#### **2️⃣ Upgrade a Helm Release**

```sh
helm upgrade myapp ./myapp
``` 

#### **3️⃣ Rollback to a Previous Version**

```sh
helm rollback myapp 1
``` 

----------

## Remarks

Using **Helm charts** for Kubernetes application deployment offers significant advantages in terms of simplicity, reusability, parameterization, versioning, and standardization. 

Companies that adopt Helm can streamline their deployment processes, reduce errors, and improve collaboration. On the other hand, not using Helm can lead to manual, error-prone, and inconsistent deployment workflows, especially for complex applications. 

For most organizations, especially those managing large-scale or complex Kubernetes deployments, Helm is a highly recommended tool.

 **Key Takeaways:**  
✅ Helm simplifies Kubernetes deployments with reusable templates.  
✅ It provides versioning, rollback, and environment-based configurations.  
✅ Helm Charts can package complex applications with dependencies.

 **What’s Next?**  
🔹 **Day 37**: Kubernetes Security Best Practices  
🔹 **Day 38**: Scaling Kubernetes Applications with Horizontal Pod Autoscaler


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NzQwNDU0OTFdfQ==
-->