---
layout: single
title: "#100daysofSRE (Day 01): Introduction to Site Reliability Engineering (SRE)"
excerpt: "Site Reliability Engineering (SRE) is a discipline that emerged from Google's need to manage the massive scale of their infrastructure. It's a cross-functional approach that focuses on creating and maintaining highly reliable and scalable systems. In this #100daysofSRE challenge, I'll cover the fundamentals of SRE, its key principles, and how it differs from traditional operations like devops and sysadmin. Tag along and learn how to become an SRE expert."
seo_title: "#100daysofSRE (Day 01): An Introduction to Site Reliability Engineering (SRE)"
seo_description: "Learn the basics of Site Reliability Engineering (SRE) and its importance in maintaining highly reliable and scalable software systems. Follow our #100daysofSRE challenge and get ready to become an SRE expert."
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

Hi, there! 👋

I will join as a Site Reliability Engineer (SRE) intern at Charles Schwab in this summer of 2023. Now, I plan to take the `#100dayschallenge` for learning and sharing my journey through SRE resources.

I have planned the [contents for next 100 days](https://medium.com/@shantoroy/learning-about-site-reliability-engineering-with-the-100daysofsre-challenge-66380323c0d1), and I will be posting one blog post each and everyday under the hashtag `#100daysofSRE`. ✌️

I hope you tag along and shre valuable feedback as I grow my knowledge and share my findings. 🙌

Alright! Let's begin... 

## Site Reliability Engineering (SRE)

In today’s digital world, uptime is everything for services. Organizations rely on their online presence to deliver services to their customers, and any downtime or performance issues can have a significant impact on revenue, customer satisfaction, and brand reputation. 

There comes the role of SRE to address the issues of reliability. Site Reliability Engineering (SRE) is a discipline that aims to improve the reliability, availability, and scalability of software systems, while also reducing the operational overhead/cost required to maintain them. 


The goal of SRE is to ensure that services are reliable, scalable, and efficient, while also maintaining a high level of velocity and innovation. 

SRE teams work closely with development (like DevOps as well) teams to design, build, and operate systems that can meet the demanding requirements of modern applications. We will learn about the difference between SRE and DevOps at a later section of this post.

## Key Concepts and Principles of SRE

To achieve its goals, SRE relies on a set of key concepts and principles that help guide its practices and processes. Here are some of the most important ones:

1.  **Service-Level Objectives (SLOs):** SRE teams define SLOs to set expectations for the availability, latency, and performance of services. SLOs are based on the needs of users and the business, and they provide a clear and measurable target for service reliability.
    
2.  **Error Budgets:** SRE teams use error budgets to balance reliability and innovation. Error budgets are a measure of the amount of downtime that is acceptable for a service, and they provide a way to trade off reliability against new features and improvements.
    
3.  **Automation:** SRE teams rely heavily on automation to reduce the risk of human error and increase efficiency. Automation tools and processes can help with tasks such as configuration management, deployment, testing, monitoring, and incident response.
    
4.  **Monitoring and Observability:** SRE teams use monitoring and observability tools to collect and analyze data about the behavior and performance of services. This data can be used to detect and diagnose issues, as well as to identify areas for improvement.
    
5.  **Incident Response and Management:** SRE teams follow well-defined processes for incident response and management, including escalation, communication, and post-incident analysis. These processes help ensure that incidents are resolved quickly and effectively, and that they are used as opportunities for learning and improvement.

Well, I have experience in Automation and I have also worked with monitoring tools. However, the terms `SLO` and `Error budget` are new to me. I hope I will learn more in the future and share details in a different post.
    

## Benefits of SRE

SRE offers a number of benefits for organizations that adopt it. Here are some of the most important ones:

1.  **Improved Reliability:** SRE teams can help improve the reliability of services by using practices such as automation, monitoring, observability, and incident management.
    
2.  **Faster Time-to-Market:** SRE teams can help reduce the time-to-market for new features and improvements by using practices such as automation, continuous delivery, and error budgets.
    
3.  **Better Collaboration:** SRE teams can help improve collaboration between development and operations teams by working closely together to design, build, and operate services.
    
4.  **Improved Customer Satisfaction:** SRE teams can help improve customer satisfaction by ensuring that services are reliable, scalable, and efficient.

So, it's all about reliability of service that leads to customer satisfaction. We will have to manage the downtime or less availability time based on service-level-agreements (SLAs). 
    

## How SRE is Different than DevOps and SysAdmin?
This question bugged me for a while at the beginning as there are so many overlaps between the roles of all these three positions.

Well, while there may be some overlap between Site Reliability Engineering (SRE), DevOps, and traditional System Administration (SysAdmin), there are some key differences too, between these roles.

***SysAdmins*** are responsible for maintaining the infrastructure and servers that support the organization's services. This includes tasks including, installing software, configuring systems, managing backups, and monitoring performance. SysAdmins are focused on keeping the **infrastructure running smoothly**, but they are not typically involved in developing or deploying applications.

***DevOps*** is a set of practices that emphasizes collaboration and communication between development and operations teams. The goal of DevOps is to create a culture of shared responsibility for **delivering high-quality software quickly and efficiently**. DevOps teams bridges the gap between the developers and operation teams to automate processes, improve visibility and communication, and increase agility.

***SRE***, on the other hand, is focused on the **reliability and availability of services**. SRE teams work closely with development teams to ensure that services are designed and built with reliability in mind. They use **automation and monitoring tools** to detect and resolve issues quickly, and they use incident management processes to learn from incidents and improve service reliability over time.

| Role            | Focus                                | Responsibilities                                       |
|-----------------|--------------------------------------|--------------------------------------------------------|
| Site Reliability Engineer (SRE) | Service reliability and availability | Collaborate with development teams, design and build reliable services, automate monitoring and incident response, improve service reliability over time |
| DevOps          | Collaboration and automation         | Collaborate between development and operations teams, automate processes, improve visibility and communication, increase agility |
| System Administrator (SysAdmin) | Infrastructure maintenance and support | Install and configure software, manage backups, monitor performance, maintain the infrastructure, troubleshoot issues |


## Concluding Remarks

Site Reliability Engineering is a powerful discipline that can help organizations achieve their goals of reliable and scalable software systems, while also enabling faster time-to-market and better collaboration between development and operations teams (a lot similar to DevOps, but not DevOps exactly 😌). 

By focusing on key concepts and principles such as SLOs, error budgets, automation, monitoring, and incident management, SRE teams can deliver services that are more reliable and leads to customer satisfaction.

So, that's all for today. See you in the next post of `#100daysofSRE` tomorrow! 🫡


___

___

Thank you for reading my blog post! 🙏

If you enjoyed it and would like to stay updated on my latest content and plans for next week, be sure to subscribe to my newsletter on Substack. 👇

Once a week, I'll be sharing the latest weekly updates on my published articles, along with other news, content and resources. Enter your email below to subscribe and join the conversation! ✍️


<iframe src="https://shantoroy.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

I am also writing on Medium. You can [follow me here](https://medium.com/@shantoroy). 👉
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNTcwMDMyNzIsLTE0NTMzNjUzMjZdfQ
==
-->