---
layout: single
title: "#100daysofSRE (Day 04): Chaos Engineering and SRE - Techniques and Tools to Break Things on Purpose"
excerpt: "Welcome to Day 4 of #100daysofSRE! Today, I'll be discussing Chaos Engineering and its role in Site Reliability Engineering. Chaos Engineering is a practice that involves intentionally introducing failures into a system to test its reliability and resilience. By breaking things on purpose in a controlled environment, SRE teams can identify potential vulnerabilities and weaknesses in their systems before they become serious issues. In this post, I'll also explore the benefits of Chaos Engineering for SRE, common techniques and tools used in Chaos Engineering."
seo_title: "Day 4 of #100daysofSRE: Chaos Engineering and SRE - Techniques and Tools to Break Things on Purpose"
seo_description: "Learn how Chaos Engineering is an essential practice for Site Reliability Engineering (SRE) and how to use tools and techniques to intentionally break things in a controlled environment."
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
  - chaos
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Hi there!!! 👋

It's the fourth day of the `#100dayschallenge`, and today I will talk about Chaos Engineering that is intended to break things to check reliability of a system in extreme environment or condition. 

> "Chaos engineering is not just about randomly breaking things. It’s about designing experiments that lead to failure, and learning from that failure to make systems more resilient." - Gremlin

So, I have planned the  [contents for next 100 days](https://medium.com/@shantoroy/learning-about-site-reliability-engineering-with-the-100daysofsre-challenge-66380323c0d1), and I will be posting one blog post each and everyday under the hashtag  `#100daysofSRE`. ✌️

I hope you tag along and shre valuable feedback as I grow my knowledge and share my findings. 🙌

Alright! Let’s begin…



## What is chaos engineering? 

> "Chaos engineering is the discipline of experimenting on a distributed system in order to build confidence in the system's capability to withstand turbulent conditions in production." - Netflix

The idea behind chaos engineering is to intentionally introduce failures into a system to identify weaknesses and potential points of failure, aiming to improve overall reliability. 

> "Chaos engineering is a discipline that acknowledges the complexity of the system, and creates experiments to expose its weaknesses." - Nora Jones, Director of Engineering at Slack

Chaos engineering deliberately introduces chaos into a system to test its resilience and reliability. The goal is to create a controlled environment where engineers can test how a system responds to various types of failures, ranging from small-scale issues like a single server going down to larger-scale problems like an entire data center going offline.

 By introducing these failures in a controlled setting, engineers can better understand how a system is likely to behave in real-world scenarios and can make improvements accordingly.

## How does chaos engineering work? 
Chaos engineering typically involves several different steps, including:

1.  **Identifying potential failure points:** Before chaos engineering can be implemented, it's essential to identify the various issues in a system where failures are most likely. This could include network connectivity, hardware failure, software bugs, etc.
2.  **Creating a hypothesis:** Once the potential failure points have been identified, engineers will hypothesize how the system will likely respond to those failures. For example, they might predict that the system will automatically fail over to a backup server in the event of a hardware failure.
3.  **Introducing chaos:** With the hypothesis in place, engineers will intentionally introduce failures into the system. This might involve shutting down a server, simulating network congestion, or introducing software bugs.
4.  **Analyzing the results:** As chaos is introduced, engineers will monitor how the system responds, collecting data and analyzing the results. This data can then be used to evaluate the original hypothesis's accuracy and identify potential areas for improvement.

## Benefits of chaos engineering

While the idea of intentionally breaking things to improve reliability might sound counterintuitive, chaos engineering can offer many benefits to organizations looking to build more resilient systems. Some of the key benefits include:

1.  **Improved reliability:** By identifying a system's potential failure points and weaknesses, chaos engineering can help organizations build more resilient systems better equipped to handle unexpected failures.
2.  **Reduced downtime:** By identifying potential issues before they become significant problems, organizations can reduce the downtime they experience, translating into substantial cost savings.
3.  **Increased confidence:** By intentionally testing a system's resilience and ability to handle failures, organizations can gain greater confidence in their systems and their ability to perform under pressure.

> "The value of chaos engineering is not in discovering new bugs or faults, but rather in increasing the resiliency and reliability of the system." - Tammy Butow, Principal SRE at Gremlin


## Techniques and Tools
Chaos engineering is a practice of intentionally injecting failures and faults into a system to observe and analyze its performance under stress and failure conditions. 

>  "The key to chaos engineering is to start small and gradually increase the level of chaos." - Ana Medina, Chaos Engineer at Gremlin

### Chaos Engineering Techniques
There are several techniques and tools used in chaos engineering that can help engineers to test their system's resilience.

1.  **Game Days:** A game day is a planned event where a team simulates a failure scenario to test the system's reliability. The team creates a set of scenarios, runs them in a controlled environment, and observes how the system responds.
    
2.  **Fault Injection:** Fault injection is the process of intentionally injecting failures or faults into a system to test its resilience. This technique involves creating synthetic failures, such as network latency, CPU overload, or disk failures, to see how the system responds.
    
3.  **Performance Testing:** Performance testing is a technique that helps to identify performance bottlenecks and other issues that may cause system failures. This technique involves simulating a high load on the system to see how it handles the traffic.
    
    
4.  **Failure Testing:** Failure testing is a technique that involves simulating different types of failures, such as hardware failures, network failures, or software failures, to see how the system responds.
    
5.  **Canary Testing:** Canary testing is a technique that involves releasing a new feature or change to a small group of users before releasing it to the entire user base. This technique helps to identify any issues or problems before the changes are released to the entire user base.

 
### Chaos Engineering Tools
 
The Chaos Toolkit is an open-source tool that helps to automate the chaos engineering process. The tool allows engineers to create scenarios and inject faults into the system to test its resilience.
    
Chaos Monkey is another well-known tool developed by Netflix that randomly terminates instances in their production environment to test the system's resilience. This tool has now been expanded to include several other tools such as Chaos Kong, Chaos Gorilla, and Chaos Snail.

Here is a list of a few open-source chaos engineering tools:
1. Chaos Monkey ([https://github.com/Netflix/chaosmonkey](https://github.com/Netflix/chaosmonkey))
2. Chaos Toolkit ([https://chaostoolkit.org/](https://chaostoolkit.org/))
3.  LitmusChaos ([https://litmuschaos.io/](https://litmuschaos.io/))
4.  Pumba ([https://github.com/alexei-led/pumba](https://github.com/alexei-led/pumba))
5.  Gremlin ([https://www.gremlin.com/community/tutorials/](https://www.gremlin.com/community/tutorials/))
6.  PowerfulSeal ([https://github.com/bloomberg/powerfulseal](https://github.com/bloomberg/powerfulseal))
7.  Chaos Mesh ([https://chaos-mesh.org/](https://chaos-mesh.org/))
8.  Toxiproxy ([https://github.com/Shopify/toxiproxy](https://github.com/Shopify/toxiproxy))
9.  Muxy ([https://github.com/itaysk/muxy](https://github.com/itaysk/muxy))
10.  ChaosBlade ([https://chaosblade.io/](https://chaosblade.io/))
11.  Goofer ([https://github.com/alexdai186/Goofer](https://github.com/alexdai186/Goofer))


## Concluding Remarks
>  "Chaos engineering is not a luxury for high-velocity teams, it's a requirement." - Adrian Cockcroft, Vice President of Cloud Architecture Strategy at AWS

So, chaos engineering is a critical practice in improving the resilience and reliability of a system. There are several techniques and tools available to engineers to test their system's resilience, including game days, fault injection, performance testing, failure testing, and canary testing, etc. 


By using different techniques and tools, engineers can identify and address weaknesses in their system before they cause major issues.

While chaos engineering may be a relatively new concept, it's already proving to be an effective tool for improving the reliability of software systems. 

By intentionally introducing controlled failures into a system, organizations can identify weaknesses, improve resilience, and gain greater confidence in their systems.


## References
* [Why SREs Need to Embrace Chaos Engineering](https://www.xmatters.com/blog/why-sres-need-to-embrace-chaos-engineering/)
* [Site Reliability Engineering (SRE) and the Chaos testing methodology](https://devopsartisan.ro.digital/blog/site-reliability-engineering-and-the-chaos-testing-methodology)
* [SRE and Chaos Engineering](https://chethansp.medium.com/sre-and-chaos-engineering-50b381d1679c)
* [Understanding chaos engineering and resilience](https://learn.microsoft.com/en-us/azure/chaos-studio/chaos-studio-chaos-engineering-overview)

___

___

Thank you for reading my blog post! 🙏

If you enjoyed it and would like to stay updated on my latest content and plans for next week, be sure to subscribe to my newsletter on Substack. 👇

Once a week (typically, Sunday), I'll be sharing the latest weekly updates on my published articles, along with other news, content and resources. Enter your email below to subscribe and join the conversation! ✍️

<iframe src="https://shantoroy.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

I am also writing on Medium. You can [follow me here](https://medium.com/@shantoroy).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAwMTc4MDUwNiwxNjEwNDA2ODMsMjA3OT
E1NzgzOV19
-->