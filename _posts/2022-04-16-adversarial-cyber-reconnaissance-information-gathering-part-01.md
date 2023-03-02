---
layout: single
title: "Summary of the Paper: Survey and Taxonomy of Adversarial Reconnaissance Techniques"
excerpt:  "Adversarial reconnaissance techniques are becoming increasingly sophisticated and challenging to mitigate, making them a major threat to the organizations. In this post, I summarize our paper that surveys and categorizes various adversarial reconnaissance techniques, providing valuable insights into how these attacks are performed from the attacker's point of view."
seo_title:  "Survey and Taxonomy of Adversarial Reconnaissance Techniques: A Summary of the reputed paper published in the ACM Computing Survey"
seo_description:  "Discover the various adversarial reconnaissance techniques and their implications for organizations in this summary of my comprehensive first-authored paper. The paper was published in the renowned Journal ACM Computing Survey which has a high impact factor and well-known in the academic communities. Learn how these techniques and tools are performed to gather information. I also discuss the review processes and the reviewer's comments."
header:
  image: "https://live.staticflickr.com/65535/52008239918_4ec6bc5c4b_o.png"
  teaser: "https://live.staticflickr.com/65535/52008239918_4ec6bc5c4b_o.png"
categories:
  - Security
tags:
  - Paper
  - Adversarial Reconnaissance
  - Cyber Reconnaissance
  - Information Gathering
  - OSINT
  - Cyber Intelligence
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


I am happy to let you know that our paper entitled `Survey and Taxonomy of Adversarial Reconnaissance Techniques` has been accepted in the [_ACM Computing Surveys_](https://dl.acm.org/journal/csur). [2020 Impact Factor: 10.282 (ranked 4/137 in Computer Science Theory & Methods)]

You can find the updated version here in [Arxiv](https://arxiv.org/pdf/2105.04749.pdf) (revised version will be updated soon). And if you are curious about the earlier version we submitted, you can find it using this link ->
[Initial Version](https://drive.google.com/file/d/1_v-ZfC3HEOK6xuHr3hudiSlBP3ddosR2/view?usp=sharing).

In this post, I will summarize how we categorized different reconnaissance techniques in both earlier and the revised version, and most importantly why we did that.


### New Concepts
In the earlier work, we first claimed that the traditional kill chain model cannot answer all the questions and processes followed by the attackers. It is because of the `reconnaissance` phase described earlier.

Cyber reconnaissance used to be assumed to take place only at the very initial stage of an attack plan. However, from different attack perspectives, we divided the reconnaissance in two phases: external and internal reconnaissance. 

The external reconnaissance is somewhat close to the earlier reconnaissance definition. Internal reconnaissance typically takes place after the attacker compromises at least one internal node. the following figure defines our thought in the modified kill chain.
<figure class="align-center">
  <a href="https://shantoroy.com/security/adversarial-cyber-reconnaissance-information-gathering-part-01/"><img src="https://live.staticflickr.com/65535/52008684679_0cb782e8be_o.png"></a>
<figcaption>Fig 1: Internal and External Recon in the Modified Kill Chain</figcaption>
</figure>
<br/>

Then we provided a taxonomy of `target information` which is divided initially as `non-technical` and `technical` information. The non-technical cluster includes physical location, logistics, and people information of an organization or an individual. Technical information includes different types of user, host, network, and application information. The whole taxonomy is provided in the paper. 


We also categorized reconnaissance approaches as `active` and `passive`. Active recon directly involves the target and passive recon does not.

Later we categorized different reconnaissance techniques into four major categories:

 - Target Footprinting
 - Social Engineering
 - Cyber Scanning
 - Local Discovery

There are some survey papers regarding `Social Engineering`, and `Cyber Scanning`. However, there was no proper survey related to the `Target Footprinting` and `Local Discovery`, which we thought could be a nice addition in an overall comprehensive way. 

The following figure is not included in the paper, I just have drawn it to illustrate the ways we have thought. Please, go through the earlier version for more details.

<figure class="align-center">
  <a href="https://shantoroy.com/security/adversarial-cyber-reconnaissance-information-gathering-part-01/"><img src="https://live.staticflickr.com/65535/52008257576_2371335c34_o.png"></a>
<figcaption>Fig 2: Dimensuins of Different Reconnaissance techniques</figcaption>
</figure>
<br/>

### Revision
The reviewers questioned the way we categorized the reconnaissance techniques earlier. From the above figure, you can see, these techniques are not exclusive in any dimension mentioned above and overlaps in different criteria. 

Therefore, in the revised version we categorized the techniques based on source: `third-party`, `Human`, and `System`. Then Human- and System-based reconnaissance techniques are again cetegorized as `remote` and `local`. Please, go through the paper for further details.

Learning how the cyber reconnaissance work is important for security researchers, engineers, and architects. This taxonomy provides the ides of how, when, and where these methods work for the attacker. And, that's why we all should know these categorization since if you want to catch a thief, you have to think as a thief first.

I intend to post details of each categories in later posts. Stay tuned and have a good day. Cheers!!!
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY0MDE3MzIyNyw4NDAyNTk3NTgsMTMyNz
AxNTUyOSwtMTI2MDg3MDk3NSwxMjQ1NDUxOTE2XX0=
-->