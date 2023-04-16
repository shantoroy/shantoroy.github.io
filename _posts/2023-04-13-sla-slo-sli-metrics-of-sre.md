---
layout: single
title: "#100daysofSRE (Day 03): SLAs, SLOs, and SLIs — Understanding the Metrics of Reliability"
excerpt: "In Site Reliability Engineering (SRE), metrics play a vital role in measuring the reliability of a system. Three key metrics in this regard are Service Level Agreements (SLAs), Service Level Objectives (SLOs), and Service Level Indicators (SLIs). In this blog post, I will dive deep into these metrics and their importance in ensuring system reliability."
seo_title: "#100daysofSRE (Day 03): Understanding the Metrics of Reliability: SLAs, SLOs, and SLIs"
seo_description: "In the world of SRE, understanding the metrics of reliability is crucial. This blog post explores the key metrics of Service Level Agreements (SLAs), Service Level Objectives (SLOs), and Service Level Indicators (SLIs) and their significance in ensuring system reliability."
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

It's the third day of the `#100dayschallenge`, and today I will talk about three key metrics of SRE: SLA, SLO, and SLI. 

So, I have planned the  [contents for next 100 days](https://medium.com/@shantoroy/learning-about-site-reliability-engineering-with-the-100daysofsre-challenge-66380323c0d1), and I will be posting one blog post each and everyday under the hashtag  `#100daysofSRE`. ✌️

I hope you tag along and share valuable feedback as I grow my knowledge and share my findings. 🙌

Alright! Let’s begin…



## What is an SLA?
You may have heard about the A Service Level Agreement (SLA) before as it has been a common term for cloud practitioners.

SLA is a contractual agreement between a service provider and a customer. The agreement outlines the level of service that the provider will deliver and defines the expectations and obligations of both parties. 

An SLA typically covers several areas, such as uptime, response time, and performance metrics, and is often accompanied by penalties (like refund 😛) if the provider fails to meet the agreed-upon service levels.

The purpose of an SLA is to assure the customer that the provider will deliver the level of service agreed upon. It also provides a framework for measuring and improving service quality and a mechanism for resolving provider and customer disputes over Quality of Service (QoS).

## What is an SLO?
The term Service Level Objective (SLO) is mostly new for the people entering SRE roles.

An SLO is a specific and measurable target a service provider aims to achieve. It is often a subset of the SLA, focusing on availability, latency, or throughput. 

SLOs define the level of service the provider aims to achieve and serve as a guide for monitoring and measuring the provider’s performance.

SLOs are typically expressed as a percentage or a ratio. For example, an SLO for uptime might be 99.9%, which means that the provider aims to achieve no more than 43 minutes of downtime per month. 

And the downtime is quite important for SRE as this is the time products are upgraded to a newer version.

Similarly, an SLO for response time might be 200ms, meaning the provider aspires to deliver a response time of no more than 200ms for a given request.

## What is an SLI?
This metric might be new to the new SRE practitioners, too.

A Service Level Indicator (SLI) is a metric used to measure a specific service aspect. SLIs are used to track the performance of a service and provide data that can be used to improve service quality. 

SLIs are typically expressed as a ratio or a percentage and are used to track availability, latency, and throughput areas.

For example, an SLI for availability might measure the percentage of time that a service is available over a given period. An SLI for latency might measure the response time for a specific request or transaction. And an SLI for throughput might count the number of requests a service can handle per second.

## Why are SLAs, SLOs, and SLIs important?
SLAs, SLOs, and SLIs are essential metrics for businesses that rely on digital services. These metrics provide a framework for measuring and improving service quality, ensuring that systems are reliable and available. 

These metrics also provide a mechanism for resolving disputes between service providers and their customers, ensuring that both parties are held accountable for the level of service they deliver.

Additionally, these metrics help businesses to identify areas for improvement and optimize their systems’ performance. By tracking SLIs, companies can identify areas where performance is lagging and take steps to address those issues. 

Similarly, by setting SLOs, businesses can define clear targets for performance and ensure that they are working towards achieving those targets.

## Concluding Remarks
Today’s businesses rely heavily on technology and digital services to operate. With this increased reliance comes the need for reliable and available systems. This is where the concepts of Service Level Agreements (SLAs), Service Level Objectives (SLOs), and Service Level Indicators (SLIs) come into play. 

All three are essential metrics for businesses that rely on digital services these days. These metrics provide a framework for measuring and improving service quality, ensuring that systems are reliable and available. 


___

___

Thank you for reading my blog post! 🙏

If you enjoyed it and would like to stay updated on my latest content and plans for next week, be sure to subscribe to my newsletter on Substack. 👇

Once a week, I'll be sharing the latest weekly updates on my published articles, along with other news, content and resources. Enter your email below to subscribe and join the conversation! ✍️

<iframe src="https://shantoroy.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

I am also writing on Medium. You can [follow me here](https://medium.com/@shantoroy).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ5NTYyMjQwMCwtMjA2NjM0Mzc4M119
-->