---
layout: single
title: "#100DaysOfSRE (Day 33): Monitoring Kubernetes Apps with Prometheus & Grafana"
excerpt: "Learn how to set up Prometheus and Grafana for monitoring Kubernetes applications, collecting metrics, and visualizing real-time performance."
seo_title: "Kubernetes Monitoring: Prometheus & Grafana"
seo_description: "Monitor Kubernetes applications using Prometheus for metrics collection and Grafana for visualization. Step-by-step setup for Minikube."
header:
  image: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
  teaser: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
categories:
  - Kubernetes
tags:
  - Kubernetes
  - Monitoring
  - Prometheus
  - Grafana
  - Observability
  - SRE
toc: true
toc_label: "Table of Contents"
toc_icon: "bar-chart"
---


**Why Monitor Kubernetes?**  
- **Detect performance bottlenecks** before they impact users  
- **Visualize metrics** such as CPU, memory, and request rates  
- **Set up alerts** for failures or resource exhaustion  
- **Improve system reliability** and proactively respond to issues  

Today, we’ll **install, configure, and visualize Kubernetes metrics** using **Prometheus & Grafana** on Minikube.

---

##  Step 1: Enable Monitoring Addons in Minikube

Minikube provides a **built-in Prometheus-Grafana stack**. To enable it:

```sh
minikube addons enable metrics-server
minikube addons enable prometheus
minikube addons enable grafana
```

Check running pods:

sh

CopyEdit

`kubectl get pods -n monitoring` 

----------

## 📌 Step 2: Access Prometheus & Grafana

### **Access Prometheus Dashboard**

Forward the Prometheus service to your local machine:

sh

CopyEdit

`kubectl port-forward -n monitoring svc/prometheus-k8s 9090:9090` 

Now, open **http://localhost:9090** in your browser.

### **Access Grafana Dashboard**

Forward Grafana service:

sh

CopyEdit

`kubectl port-forward -n monitoring svc/grafana 3000:3000` 

Now, open **http://localhost:3000**  
(Default login: **admin / prom-operator**)

----------

## 📌 Step 3: Configure Prometheus to Collect Metrics

Prometheus scrapes metrics from Kubernetes using **ServiceMonitors**. Let’s define one.

📌 **prometheus-servicemonitor.yaml**

yaml

CopyEdit

`apiVersion:  monitoring.coreos.com/v1  kind:  ServiceMonitor  metadata:  name:  myapp-monitor  namespace:  myapp  spec:  selector:  matchLabels:  app:  backend  endpoints:  -  port:  http  interval:  15s` 

Apply it:

sh

CopyEdit

`kubectl apply -f prometheus-servicemonitor.yaml` 

Now, Prometheus will **scrape metrics** every **15 seconds** from the **backend service**.

----------

## 📌 Step 4: Expose Application Metrics

By default, Prometheus expects an endpoint like **/metrics** to collect data. Let’s modify our **backend** to expose metrics.

📌 **backend/app.py**

python

CopyEdit

`from flask import Flask from prometheus_client import start_http_server, Counter

app = Flask(__name__)
REQUESTS = Counter('http_requests_total', 'Total number of HTTP requests') @app.route("/") def  home():
    REQUESTS.inc() return  "Hello, Kubernetes Monitoring!"  if __name__ == "__main__":
    start_http_server(8000) # Expose metrics on /metrics app.run(host="0.0.0.0", port=5000)` 

Rebuild and restart the backend:

sh

CopyEdit

`docker build -t my-backend .
kubectl rollout restart deployment backend` 

Verify metrics:

sh

CopyEdit

`curl http://backend:8000/metrics` 

----------

## 📌 Step 5: Visualize Metrics in Grafana

### **Import Prometheus as a Data Source**

1.  Open **Grafana** (`http://localhost:3000`)
2.  Go to **Configuration > Data Sources > Add Data Source**
3.  Select **Prometheus**
4.  Enter **http://prometheus-k8s.monitoring.svc:9090** as the URL
5.  Click **Save & Test**

### **Import a Prebuilt Dashboard**

1.  Go to **Dashboards > Import**
2.  Use **ID: 3119 (Kubernetes Cluster Monitoring)**
3.  Click **Load** and **Import**

🎉 **Now you can see real-time Kubernetes metrics!**

----------

##  Step 6: Set Up Alerts with Prometheus Alertmanager

Define an **Alert Rule**:

 **alert-rules.yaml**

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: high-cpu-alert
  namespace: monitoring
spec:
  groups:
  - name: instance-rules
    rules:
    - alert: HighCPUUsage
      expr: rate(container_cpu_usage_seconds_total[2m]) > 0.5
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: "High CPU Usage Detected"
        description: "CPU usage is above 50% for more than 2 minutes."
``` 

Apply it:

```sh
kubectl apply -f alert-rules.yaml
``` 

Prometheus will now trigger an **alert** if **CPU usage exceeds 50%** for **2 minutes**.

----------

## Remarks

 **Key Takeaways**  
✅ **Prometheus collects metrics** from Kubernetes workloads  
✅ **Grafana visualizes metrics** in real-time dashboards  
✅ **ServiceMonitors configure scraping rules** for Prometheus  
✅ **Alerts notify teams** when performance degrades

 **What’s Next?**  
🔹 **Day 34**: Automating Kubernetes Deployments with ArgoCD & GitOps  
🔹 **Day 35**: Building a Kubernetes CI/CD Pipeline

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAxMDcyMzY4NV19
-->