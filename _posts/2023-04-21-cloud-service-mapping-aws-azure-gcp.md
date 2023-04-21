---
layout: single
title: "Cloud Service Mapping across AWS, Azure, and GCP"
excerpt: "Are you looking for an easy way to compare and find alternatives of different cloud services across AWS, Azure, and GCP? Look no further than a GitHub repository that provides a side-by-side comparison of products based on target services. In this post, I'll explore this repository, as well as share a basic map for common services that I created myself. Plus, I'll throw in some links to free courses that I found on Twitter to help you get started. Read on to learn more about cloud service mapping and how it can benefit your cloud-based projects."
seo_title: "Cloud Service Mapping: AWS vs Azure vs GCP"
seo_description: "Learn how to map cloud services across AWS, Azure, and GCP in one place. Check out a comprehensive GitHub repository, a basic mapping of common services, and free course links for your cloud education."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - SRE
tags:
  - SRE
  - 100daysofsre
  - 100daychallenge
  - devops
  - sysadmin
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Hi there!!! 👋

If you are a cloud computing researcher or practitioner, you definitely worked with one of the most popular public cloud providers: Amazon Web Service (AWS), Microsoft Azure, or Google Cloud Provider (GCP).

These services offer a lot of products for particular service needs and it's even difficult to remember all the names or map the alternatives.

Recently, I found a GitHub repository that provides a comprehensive list of products across AWS, Azure, and GCP side-by-side based on target services. 

In this post, I talk about that repository, add a simple basic map for common services myself, and added some free course links found on twitter.

## Cloud Service Mapping

Created by Milan Milanović, [this repository](https://github.com/milanm/Cloud-Product-Mapping) provides an easy-to-read infographic that maps out the different cloud services offered by the three major cloud providers, organized by purpose. The infographic covers services related to computing, storage, networking, databases, security, analytics, machine learning, and more.

This resource is handy for those looking to compare and contrast the services offered by each cloud provider for a specific purpose or use case. For example, suppose you're looking for the best solution for data warehousing. In that case, the infographic can quickly point you to AWS's Redshift, Azure's SQL Data Warehouse, and GCP's BigQuery.

This Cloud Product Mapping repository is a valuable resource for anyone navigating cloud services. It's especially helpful for those who need to compare and contrast the offerings of AWS, Azure, and GCP for specific use cases.


## Example Map of some Popular Services
I'm also adding an example mapping of some popular services here:

| Service | AWS | Azure | GCP |
|---------|-----|-------|-----|
| Compute | EC2, Lambda, ECS | Virtual Machines, Azure Functions | Compute Engine, Cloud Functions |
| Storage | S3, EBS, Glacier | Blob Storage, Azure Files | Cloud Storage, Persistent Disk |
| Database | RDS, DynamoDB, Redshift | SQL Database, Cosmos DB | Cloud SQL, Cloud Spanner, Cloud Bigtable |
| Networking | VPC, ELB, Route 53 | Virtual Network, Load Balancer | Virtual Private Cloud, Load Balancing |
| Analytics | EMR, Kinesis, Athena | HDInsight, Stream Analytics | Dataproc, Dataflow, BigQuery |
| Machine Learning | SageMaker, Rekognition, Polly | Machine Learning, Cognitive Services | AI Platform, Cloud ML Engine |
| Identity & Access Management | IAM, Cognito | Active Directory, Azure AD | Cloud IAM, Cloud Identity |
| Security | WAF, Inspector, GuardDuty | Security Center, Sentinel | Cloud Security Command Center, Cloud IAM |
| Internet of Things | IoT Core, Greengrass, FreeRTOS | IoT Hub, IoT Central | Cloud IoT Core, IoT Edge |
| DevOps | CodePipeline, CodeBuild, CodeDeploy | DevOps, Azure DevTest Labs | Cloud Build, Cloud Source Repositories |
| Management & Governance | CloudFormation, CloudTrail, Config | Azure Resource Manager, Log Analytics | Cloud Deployment Manager, Stackdriver |
| Application Integration | SQS, SNS, Step Functions | Service Bus, Event Grid | Cloud Pub/Sub, Cloud Functions |
| Mobile | AWS Amplify, Mobile Hub | Mobile Apps | Firebase, App Engine |
| Media | Elemental MediaLive, MediaConvert | Media Services | Cloud Video Intelligence |


## Bonus Free Tutorials Links
While writing the post, I found some free materials posted by `Linuxopsys` on twitter:

* Linux → [https://www.netacad.com/courses/os-it/ndg-linux-essentials](https://www.netacad.com/courses/os-it/ndg-linux-essentials) 
* Bash → [https://linuxopsys.com/?s=bash](https://linuxopsys.com/?s=bash) 
* AWS → [https://explore.skillbuilder.aws](https://explore.skillbuilder.aws) 
* Azure → [https://learn.microsoft.com](https://learn.microsoft.com) 
* DevOps → [https://edx.org/learn/devops](https://edx.org/learn/devops) 
* Docker → [https://docker-curriculum.com](https://docker-curriculum.com) 
* Kubernetes → [https://kubernetes.io/docs/tutorials/kubernetes-basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)


<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Learn for free &amp; get a job! <br><br>Linux → <a href="https://t.co/lMabwl3yYV">https://t.co/lMabwl3yYV</a> <br><br>Bash → <a href="https://t.co/MWXSq4CPyY">https://t.co/MWXSq4CPyY</a> <br><br>AWS → <a href="https://t.co/iAy5xTBuAb">https://t.co/iAy5xTBuAb</a><br><br>Azure → <a href="https://t.co/t2sBFK4fFv">https://t.co/t2sBFK4fFv</a><br><br>DevOps → <a href="https://t.co/P9H2OiMAyn">https://t.co/P9H2OiMAyn</a> <br><br>Docker → <a href="https://t.co/AGRKarTi1w">https://t.co/AGRKarTi1w</a><br><br>Kubernetes → <a href="https://t.co/emf1AakwEv">https://t.co/emf1AakwEv</a> <a href="https://t.co/aLMybROJga">pic.twitter.com/aLMybROJga</a></p>&mdash; Linuxopsys (@linuxopsys) <a href="https://twitter.com/linuxopsys/status/1648969981512630272?ref_src=twsrc%5Etfw">April 20, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Thought, it would be worth sharing!

That's all for today, guys! Cheers!!!

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc1MTM5MTE4NSw2NzE2MjM0N119
-->