---
layout: single
title: "#100daysofSRE (Day 07): Effective Communication during Incidents for Better Incident Response"
excerpt: "In this post, I'll be discussing the importance of effective communication during incidents in order to improve incident response in Site Reliability Engineering. I'll cover communication strategies, tools, and techniques that SREs can use to ensure that communication is clear, concise, and timely."
seo_title: "#100daysofSRE (Day 07): Effective Communication during Incidents for Better Incident Response"
seo_description: "Learn about effective communication during incidents for better incident response in Site Reliability Engineering. Discover communication strategies, tools, and techniques that SREs can use to ensure clear and timely communication during incidents. Join the #100daysofSRE challenge for more SRE insights!"
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

It's the sixth day of the `#100dayschallenge`, and today I will explore how to effectively communicate and related best practices. 

Effective communication is crucial during incidents because it enables all stakeholders to remain informed, coordinated, and ultimately focused on resolving the issue. 

In the earlier post, I discussed [Incident Management and Response for Site Reliability Engineers](https://shantoroy.com/sre/incident-management-and-response-for-site-reliability-engineers/).



>   "Incident management is the process of identifying, assessing, and responding to incidents that impact the availability or performance of a system or service."

So, I have planned the  [contents for next 100 days](https://medium.com/@shantoroy/learning-about-site-reliability-engineering-with-the-100daysofsre-challenge-66380323c0d1), and I will be posting one blog post each and everyday under the hashtag  `#100daysofSRE`. ✌️

I hope you tag along and share valuable feedback as I grow my knowledge and share my findings. 🙌

Alright! Let’s begin…


## Importance of Effective Communication during Incident Response

Here are some specific reasons why effective communication is essential during incidents:

1.  **Timely Response:** Communication during incidents helps ensure a timely response, which can be critical in mitigating or preventing potential damage.
2.  **Efficient Collaboration:** Different teams and individuals must work together to effectively address an incident. Effective communication helps facilitate this collaboration and ensures everyone is on the same page.
4.  **Accountability:** During an incident, everyone must know their roles and responsibilities. Effective communication ensures that everyone is accountable for their part in resolving the issue.
6.  **Documentation and Future Preparation:** Effective communication during incidents is crucial for resolving the current issue and preparing for future incidents. By documenting and analyzing the communication process, teams can learn from their experiences and improve their communication in the future.
7.  **Stakeholder Involvement:** Clear and timely communication with stakeholders helps them understand the situation and any potential impact on them, which can help reduce confusion and anxiety.


## Challenges
During incidents, various challenges can arise when it comes to effective communication. Some of these challenges include:

1.  **Time pressure:** During an incident, time is of the essence, and there is often a sense of urgency to resolve the issue as quickly as possible. This can lead to rushed communication, which may need to be clarified or concise.
2.  **Miscommunication and Misinterpretation:** Miscommunication can quickly happen during incidents, as people may need help understanding the problem's technical aspects or the proposed solutions. This can lead to misunderstandings and delays in resolving the issue.
3.  **Multiple stakeholders or Involved Teams:** During incidents, there are often numerous stakeholders involved, including technical teams, management, and customers. It can be challenging to communicate effectively with all parties and ensure everyone is on the same page. Similarly, SRE, Developers, and Security teams may have different opinions towards solutions and divided tasks.
4.  **Stress and emotions:** People may become frustrated, angry, or panicked, leading to poor communication and further exacerbating the issue.
6.  **Lack of communication protocols:** With established communication protocols, ensuring everyone knows how and when to communicate during an incident can be more manageable. This can lead to confusion and delays in resolving the issue.



## Strategies for Effective Communication During Incidents

Effective communication can make all the difference in how quickly and efficiently the situation is resolved during incidents. Here are some strategies for effective communication during incidents:

1.  **Establish a Communication Protocol:** In advance, establish a communication plan that outlines who is responsible for communicating with whom during an incident. Teams need to identify the communication tools and platforms used, including phone, email, chat, or collaboration.
3.  **Establish Roles and Responsibilities:** Clearly define roles and responsibilities for all team members involved in the incident. This will ensure everyone knows their responsibilities and how they fit into the overall response effort.
4.  **Share Updates Frequently:** Provide frequent updates to all stakeholders involved in the incident. These updates should include information about the status of the incident, any progress that has been made, and any new information that has been discovered.
5.  **Be Transparent:** When communicating during an incident, being transparent about the situation is essential. Share all relevant information with stakeholders, including any potential risks or challenges.
7.  **Use Visualization:** In some cases, visual aids such as diagrams or flowcharts can help explain complex information. Consider using visual aids like whiteboards/images of workflow/graphs to help communicate important information during an incident.
8.  **Practice Effective Conflict Resolution:** During an incident, tensions can run high, and conflicts may arise. It is important to practice effective conflict resolution techniques to resolve disagreements quickly and effectively. Chaos engineering can be introduced to test incident response. I discussed [chaos engineering in my earlier post](https://shantoroy.com/sre/chaos-engineering-techniques-and-tools-for-sre/).



## Technologies and Tools
When incidents occur, communication is essential to ensure the right actions are taken to resolve the issue. In today's world, many tools and technologies are available to facilitate effective communication during incidents.


1.  **Chat Applications:** Chat applications such as Slack, Microsoft Teams, and Discord are widely used in incident response. These applications allow team members to communicate in real time, share important information, and collaborate on resolving issues.
2.  **Video Conferencing:** Video conferencing tools such as Zoom, MS Teams, Google Meet, and Skype are helpful for geographically dispersed teams. Video conferencing allows team members to see and hear each other, which can help resolve incidents quickly.
3.  **Incident Management Systems:** Incident management systems such as PagerDuty, Opsgenie, and VictorOps are explicitly designed for incident response. These systems provide a central platform for communication, collaboration, and tracking of incident progress. I have posted a long list of related tools [in an earlier post](https://shantoroy.com/sre/incident-management-and-response-for-site-reliability-engineers/).
5.  **Mobile Phones:** Mobile phones are an essential tool for incident responders who must always be available and responsive. Mobile phones allow team members to communicate quickly and easily, regardless of location. My manager shared his phone number the very first day we talked after I was offered an internship.
6.  **Whiteboards:** A physical whiteboard can help track incident progress and communicate information to the team. Whiteboards can be especially useful in a physical war room environment.
7.  **Social Media:** Social media platforms might be used to communicate with customers and other external stakeholders during incidents. Social media can also share updates and important information with the broader community. Like Elon Musk do 😉. 


## Best Practices


The following best practices can help teams maintain effective communication during incidents:

1.  **Establish clear communication channels:** Establishing clear communication channels is the first step toward effective communication. Ensure everyone knows how and when to communicate, what channels to use, and who to contact.
2. **Train, Test and Demo Run:** With the help of Chaos engineering, companies should simulate similar scenarios that might happen during a major incident. The demo run will train the employees and help them hone their effective communication skill.
3.  **Practice active listening:** Listening to what others say is essential during incidents. This involves paying attention to the speaker, asking questions, and providing feedback to ensure everyone is on the same page.
4.  **Keep everyone informed:** Keep everyone involved in the incident informed about the current status, what's being done, and any changes in the situation. This helps prevent confusion and ensures that everyone is on the same page.
5.  **Document everything:** Documentation is crucial during incidents and key to success for future incidents. Record all communication, actions taken and decisions made. This helps to maintain an accurate record of the incident and can be used for future reference.
6.  **Use collaboration tools:** Collaboration tools like messaging apps, video conferencing, and project management software can facilitate communication and ensure everyone is on the same page.
7.  **Conduct post-incident reviews:** After resolving the incident, conduct a post-incident review to evaluate what worked and what didn't. This helps identify improvement areas and ensures that the incident response process is continuously improved.


## Concluding Remarks
Effective communication is crucial for successful incident management. Still, achieving it can be challenging, especially when dealing with high-pressure situations. 

Many tools and technologies are available to facilitate effective communication during incidents. The key is to choose the right tools for your team and ensure that everyone is familiar with their use. 

With the right communication tools and strategies, incident responders can work together more efficiently, resolve incidents quickly, and minimize the impact on customers and the business.

Documentation is the key to success and proper response to furture incidents. Document as many processes, ways, tips, what to do, what not to do, best practices, etc. and keep updating after each incident.

Additionally, following the above-mentioned best practices can help teams maintain clear and effective communication.


## References
* [Incident communication best practices](https://www.atlassian.com/incident-management/incident-communication)
* [How to communicate effectively during an IT incident](https://www.manageengine.com/academy/incident-communication-plan.html)
* [Communication is the Key to Effective Incident Management](https://riskonnect.com/business-continuity-management/communication-is-the-key-to-effective-incident-management/)
* [A Guide to Incident Communications](https://www.pagerduty.com/resources/learn/a-guide-to-incident-communications/)
* [A Guide to Effective Incident Management Communications](https://resources.sei.cmu.edu/asset_files/Handbook/2021_002_001_651819.pdf)
* [Incident response: How to implement a communication plan]()

___

___

Thank you for reading my blog post! 🙏

If you enjoyed it and would like to stay updated on my latest content and plans for next week, be sure to subscribe to my newsletter on Substack. 👇

Once a week, I'll be sharing the latest weekly updates on my published articles, along with other news, content and resources. Enter your email below to subscribe and join the conversation for Free! ✍️

<iframe src="https://shantoroy.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

I am also writing on Medium. You can [follow me here](https://medium.com/@shantoroy).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzA1NDY0MTQ5LDYzNzA1NDAzNl19
-->