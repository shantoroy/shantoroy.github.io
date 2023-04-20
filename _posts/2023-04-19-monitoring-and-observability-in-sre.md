---
layout: single
title: "#100daysofSRE (Day 09): Monitoring and Observability in SRE"
excerpt: "In Day 9 of #100daysofSRE, we dive into the world of monitoring and observability in SRE. Learn how to improve the reliability and performance of your system by implementing effective monitoring and observability techniques."
seo_title: "#100daysofSRE (Day 09): Monitoring and Observability in SRE"
seo_description: "Learn about the importance of monitoring and observability in Site Reliability Engineering. Discover techniques and tools to enhance your system's performance, reliability, and observability. Join us for Day 9 of #100daysofSRE."
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

It's the ninth day of the `#100dayschallenge`, and today I will explore the imporatance, best practices, and tools used for monitoring and observability in SRE.

Monitoring for SRE (Site Reliability Engineering) refers to observing and tracking the performance and availability of software systems and applications to identify and resolve issues. This practice helps ensure that systems and applications are functioning as expected and meeting users' needs.

Observability understands what is happening within a system through data analysis. In software engineering, observability refers to instrumenting applications and infrastructure to produce telemetry data that provides visibility into a system's behavior. Observability enables SREs to diagnose and resolve issues on time, ultimately improving their systems' reliability and performance.

So, I have planned the  [contents for next 100 days](https://medium.com/@shantoroy/learning-about-site-reliability-engineering-with-the-100daysofsre-challenge-66380323c0d1), and I will be posting one blog post each and everyday under the hashtag  `#100daysofSRE`. ✌️

I hope you tag along and share valuable feedback as I grow my knowledge and share my findings. 🙌

Alright! Let’s begin…




## Monitoring

Monitoring is tracking and measuring the performance of systems and applications to ensure they function correctly. 

This includes collecting data on key performance indicators (KPIs) such as response time, availability, and throughput. 

By monitoring KPIs, SRE teams can quickly detect and diagnose problems and take corrective actions before they affect the end users.

### Importance of Monitoring for SRE

Monitoring is crucial for SRE because it helps teams proactively identify and mitigate issues before they cause system downtime or service degradation. Effective monitoring can help SRE teams to:

1.  **Identifying potential problems before they cause outages:**  By monitoring systems, SRE teams can identify potential problems before they cause outages. This can help to prevent costly and disruptive outages.
2.  **Providing insights into system performance:**  Monitoring data can provide valuable insights into system performance. This information can be used to improve system design, configuration, and operations.
3.  **Ensuring compliance with regulations:**  Many regulations require businesses to monitor their systems for compliance. Monitoring can help businesses to meet these requirements.
4.  **Detecting security threats:**  Monitoring data can be used to detect security threats. This information can be used to quickly respond to threats and protect systems from attack.
5.  **Providing evidence for incident investigations:**  In the event of an incident, monitoring data can be used to investigate the cause of the incident and identify steps to prevent future incidents.
6.  **Improving customer satisfaction:**  By ensuring that systems are performing as expected, monitoring can help to improve customer satisfaction.
7.  **Reducing costs:**  By identifying and addressing potential problems before they cause outages, monitoring can help to reduce costs.

### Different Types of Monitoring

There are different types of monitoring that SRE teams can use to ensure that systems and applications are running smoothly. These include:

-   **Infrastructure monitoring:** This type of monitoring tracks the performance of the underlying infrastructure, such as servers, databases, and network devices.
-   **Application monitoring:** This type of monitoring tracks the performance of the software applications themselves, including response times, throughput, and error rates.
-   **Network monitoring:** This type tracks the network's performance, including bandwidth usage, latency, and packet loss.




### Best Practices for Monitoring in SRE

Effective monitoring requires a combination of tools, processes, and best practices. Here are some best practices for monitoring in SRE:

-   **Define KPIs:** Define KPIs that are relevant to the business and track them regularly. This helps SRE teams quickly identify issues that impact users.
-   **Set up alerts:** Configure alerts that notify SRE teams when KPIs exceed certain thresholds. This helps teams proactively identify and resolve issues before they become critical.
-   **Monitor key workflows:** This includes processes such as logins, checkouts, and transactions.
-   **Use automation:** Use automation to collect data and generate alerts. This helps reduce the workload on SRE teams and ensures consistent and accurate monitoring.
-   **Monitor for security:** Monitor security issues such as unauthorized access attempts and data breaches.


## Observability
Observability is crucial for SREs because it enables them to proactively identify and address issues before they cause system downtime or negatively impact end users. With observability, SREs can quickly diagnose the root cause of an issue and implement a fix, minimizing the impact on end-users.

While monitoring and observability are related concepts, there are some critical differences between them. Monitoring focuses on the collection and analysis of metrics. In contrast, observability encompasses a broader set of data, including metrics, traces, and logs. Additionally, observability is designed to provide context and enable SREs to understand the behavior of a system. At the same time, monitoring is focused on identifying specific metrics and anomalies.

### Key Components
The three components of observability are metrics, traces, and logs. 

-   **Metrics**  are data points that measure the health of a system. They can be used to track things like CPU usage, memory usage, and database queries.
-   **Logs**  are records of events that occur in a system. They can be used to track things like user activity, errors, and security incidents.
-   **Traces**  are a record of how a request travels through a system. They can be used to identify bottlenecks and performance problems.

## Best practices
1.  **Define and align on key metrics:** Define key metrics for each service or application and align with business goals. This will help to ensure that everyone is focused on the right metrics and that they are being tracked consistently.
    
2.  **Distributed tracing:** Distributed tracing allows you to follow a transaction as it moves through different services or applications. It can help you identify where bottlenecks or errors are occurring and make it easier to troubleshoot issues.
    
3.  **Logging and log aggregation:** Logs are a key component of observability, but they can be difficult to manage at scale. We should use a centralized logging system to aggregate logs from different services and applications, and make sure that logs are properly structured and tagged for easy searching.
    
5.  **Automated alerting and escalation:** Use automation to create alerts based on predefined thresholds, and make sure that alerts are sent to the right people at the right time. Implement escalation policies to ensure that critical alerts are addressed promptly.
    
6.  **Machine learning and AI:** Machine learning and AI can help to identify patterns and anomalies in large data sets. Use these tools to identify issues before they become major problems, and to provide insights into application behavior and performance.
    
7.  **Regular reviews and post-mortems:** Conduct regular reviews of your observability practices to identify areas for improvement, and use post-mortems to analyze major incidents and identify opportunities to improve your processes and tools.

## Tools for Monitoring and Observability
Open source tools are as follows:
1.  Prometheus: [https://prometheus.io/](https://prometheus.io/)
2.  Grafana: [https://grafana.com/](https://grafana.com/)
3.  Nagios: [https://www.nagios.org/](https://www.nagios.org/)
4.  Zabbix: [https://www.zabbix.com/](https://www.zabbix.com/)
5.  Icinga: [https://icinga.com/](https://icinga.com/)
6.  Munin: [https://munin-monitoring.org/](https://munin-monitoring.org/)
7.  Cacti: [https://cacti.net/](https://cacti.net/)
8.  OpenNMS: [https://www.opennms.com/](https://www.opennms.com/)
9.  Netdata: [https://www.netdata.cloud/](https://www.netdata.cloud/)
10.  Monitorix: [https://www.monitorix.org/](https://www.monitorix.org/)

List of common paid tools are as follows:

1.    Datadog: [https://www.datadoghq.com/](https://www.datadoghq.com/)
2. New Relic: [https://newrelic.com/](https://newrelic.com/)
3. Dynatrace: [https://www.dynatrace.com/](https://www.dynatrace.com/)
4. AppDynamics: [https://www.appdynamics.com/](https://www.appdynamics.com/)
5. Amazon CloudWatch: [https://aws.amazon.com/cloudwatch/](https://aws.amazon.com/cloudwatch/)
6. Microsoft Azure Monitor: [https://azure.microsoft.com/en-us/services/monitor/](https://azure.microsoft.com/en-us/services/monitor/)
7. Google Cloud Monitoring: [https://cloud.google.com/monitoring](https://cloud.google.com/monitoring)
8. Splunk [https://www.splunk.com/](https://www.splunk.com/)

## Concluding Remarks
Monitoring and observability are critical aspects of SRE that play a significant role in ensuring the reliability and availability of software systems. 

By implementing the best practices for monitoring and observability, SRE teams can effectively detect, diagnose, and resolve incidents before they impact the end users. 

Monitoring helps SRE teams gain insights into infrastructure performance, applications, and networks. At the same time, observability enables them to better understand the system's behavior and performance through metrics, traces, and logs.

## References
* [Why Observability Matters in Site Reliability Engineering (SRE)](https://insights.daffodilsw.com/blog/why-observability-matters-in-site-reliability-engineering-sre)
* [Why Observability is Critical to Site Reliability Engineering](https://saucelabs.com/resources/blog/why-observability-is-critical-to-site-reliability-engineering)
* [Top 10 Monitoring and observability tools in 2022 for SRE (Site reliability engineering)](https://www.devopsschool.com/blog/top-10-monitoring-and-observability-tools-in-2022-for-sre-site-reliability-engineering/)
* [Observability - School of SRE](https://linkedin.github.io/school-of-sre/level101/metrics_and_monitoring/observability/)
* [A Guide to Understanding Observability & Monitoring in SRE Practices](https://www.blameless.com/blog/observability-and-monitoring)
* [Why Observability and Monitoring Matter to SREs - JJ Tang](https://devops.com/why-observability-and-monitoring-matter-to-sres/)
* [# Observability, A Pillar of Site Reliability Engineering Explained](https://www.plutora.com/blog/observability-pillar-site-reliability-engineering#:~:text=Monitoring%20is%20the%20process%20of,diagnose%20issues%20in%20real%2Dtime.)
* [OpenAI ChatGPT](https://chat.openai.com/)
* [Google Bard](https://bard.google.com/)



___

___

Thank you for reading my blog post! 🙏

If you enjoyed it and would like to stay updated on my latest content and plans for next week, be sure to subscribe to my newsletter on Substack. 👇

Once a week, I'll be sharing the latest weekly updates on my published articles, along with other news, content and resources. Enter your email below to subscribe and join the conversation for Free! ✍️

<iframe src="https://shantoroy.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

I am also writing on Medium. You can [follow me here](https://medium.com/@shantoroy).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIwNjcwNjkxNF19
-->