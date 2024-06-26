---
layout: single
title: "How to Set Git Repository-specific User Credential Configuration"
excerpt:  "Setting up Git credentials is an essential step in securing your Git repository. However, you may encounter situations where you need to use different user credentials for different Git repositories. This blog post will guide you through the process of setting up user credentials configuration for specific Git repositories using Git command line and Git config file. Whether you are working with multiple Git repositories or sharing your computer with other users, this tutorial will help you manage your Git credentials effectively."
seo_title:  "How to Set Git Repository-specific User Credential Configuration | Git Tips"
seo_description:  "Learn how to set up user credentials configuration for specific Git repositories using Git command line and Git config file."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - Git
tags:
  - Github
  - Tutorial
  - Overleaf
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Sometimes, we may have more than one GitHub accounts, for example, one personal and another for a group. 

If we are maintaining a particular repository of that group, we may need to change the default username and password, which is usually set for our personal account.

In that case, we can set repository-specific username and password so that it doesn't cost us time while pulling or pushing repository updates.

In this post, I will show how to set repository-specific user credentials. 

### set repository-specific username/email configuration
1.  change username
	```
	git config user.name "FIRST_NAME LAST_NAME"
	``` 
2.  change email address:  
	```
	git config user.email "MY_NAME@example.com"
	```

### Change it back to Ask Password
```
git config credential.${remote}.username yourusername
```

```
git config credential.helper store
```

## References
1. [Configure your DVCS username for commits](https://support.atlassian.com/bitbucket-cloud/docs/configure-your-dvcs-username-for-commits/)
2. [How to set up username and passwords for different git repos?](https://unix.stackexchange.com/questions/335704/how-to-set-up-username-and-passwords-for-different-git-repos)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0ODA3ODIyMDEsLTIwOTE1NTQ2NTIsLT
U2NjEzNDczMF19
-->