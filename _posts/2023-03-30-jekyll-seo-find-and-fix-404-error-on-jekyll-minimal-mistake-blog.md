---
layout: single
title: "Jekyll SEO: How to Find and Fix 404 Error on a Jekyll (Minimal Mistakes) Blog Website"
excerpt: "If you're a Jekyll blogger and struggling with 404 errors on your blog website, there is a way to fix this issue. Broken links and missing pages can frustrate your readers, and harm your search engine rankings. But fear not, there is a solution. In this blog post, I'll show you how to use Google Analytics and Console to find broken links and enable redirection to fix those 404 errors in your Jekyll (Minimal Mistakes) blog website. Redirection 301 is the best solution and here I show how to do that in Jekyll site."
seo_title: "Jekyll SEO: How to Find and Fix 404 Error on a Jekyll (Minimal Mistakes) Blog Website"
seo_description: "Struggling with 404 errors on your Jekyll (Minimal Mistakes) blog website? This blog post shows you how to find issues using Google Analytics/console and enable redirection to fix broken links. Keep your readers happy and improve your search engine rankings with these simple steps. I used Redirection 301 to fix the issue."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - Jekyll
tags:
  - Jekyll
  - mmistakes
  - Minimal Mistakes
  - github-pages
  - SEO
  - search engine optimization
  - redirection 301
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---
Recently, I found a number of times `404 not found` page was visited by my blog users. Then I investigated the matter and found some helpful tips that can fix this issue easily.

## Why Broken Links are Bad
Broken links can have a negative impact on our website's user experience and search engine optimization (SEO).

First of all, broken links can be frustrating for users and can lead to a poor user experience. If users click on a link and it leads to a "404 error" page, they may leave our website, resulting in a high bounce rate. This can negatively affect your website's reputation and credibility.
    
Also, search engines like Google or Bing consider broken links as a sign of poor quality and affect the site ranking. If search engines crawl our website and find broken links, they may negatively impact our website's ranking in search results. 

Additionally, broken links can negatively impact our website's overall crawlability. Search engine bots may stop crawling our website if they encounter too many broken links, resulting in a decrease in the number of pages indexed by the search engine.

## Why 404 may happen?
It can happen for various reason. From my experience, it happened to my blog because of the following reasons:
1.  Content Updates: I updated the content on my website and introduced new broken links. I updated some URLs of blog posts to have a better SEO. Also, there can be other reasons. For example, if you delete a page any internal or external links pointing to that page will become broken.
    
    
2.  External Websites: Broken links can also occur due to external websites linking to your website. If an external website that links to your website removes or changes the link, it can result in a broken link on your website. And I have done so as I advertised these earlier URLs in social media and other websites.



## `404-page not found` Solution
To avoid the negative impact of broken links, it is important to regularly check our website for broken links and fix them promptly.

We can use various online tools to scan your website for broken links, and then remove or update them. By doing so, you can improve our website's user experience, reputation, and search engine optimization.

### Check Status: Google Analytics
First, we can check the status of our website using Google Analytics. Google Analytics can help you identify "404 not found" page issues on your website in several ways:

1.  Pageviews: We can use the "Pageviews" metric in Google Analytics to see how many times a "404 not found" page has been viewed. This can help us identify the most commonly occurring "404 not found" pages on our website.
    
2.  Landing Pages: We can use the "Landing Pages" report in Google Analytics to see which pages on our website are causing visitors to land on a "404 not found" page. This can help us identify which pages on our website need to be fixed or redirected.
    
3.  Site Content: We can use the "Site Content" report in Google Analytics to see which pages on our website are causing "404 not found" errors. This report can help us identify broken links or pages that need to be redirected.
    
4.  Custom Reports: We can create custom reports in Google Analytics to track "404 not found" errors on our website. For example, we can create a custom report that shows the number of "404 not found" errors by page, so we can see which pages on our website need to be fixed or redirected.


### Finding 404 Source URLs: Google Search Console
Google Search Console can help us find 404 source URLs in several ways. Here are some examples:

1.  Crawl Errors Report: In the Crawl Errors report, we can see the list of URLs that returned a 404 error. We can also see the number of times each URL was requested and when the error occurred. This report can help us identify the source URLs that are causing the 404 errors.
    
2.  Coverage Report: In the Coverage report, we can see the list of URLs that were crawled by Google and their status. We can filter the report to show only the URLs that returned a 404 error. This report can help us identify the source URLs that are causing the 404 errors.
    
3.  URL Inspection Tool: We can use the URL Inspection tool to check the status of a specific URL and see if it returns a 404 error. If the URL is returning a 404 error, we can see the details of the error, including the source URL that caused the error.

### Find Broken Links on our Site
[Dead Link Checker](https://www.deadlinkchecker.com/website-dead-link-checker.asp) is a website that offers a tool to scan websites for broken links. I used this to find existing broken links on my blog.

The site is free to use and scans the entire website for broken links, including internal links and external links. This comprehensive scanning ensures that all broken links are identified and can be fixed.

The tool is easy to use and doesn't require any technical expertise. All we need to do is enter the URL of the website we want to scan and click on the "Check" button.

## Enable Redirection
Initially, I started updating the new URLs everywhere. However, that is time consuming and does not solve the problem entirely. I still found `404` visits are occuring.

The best solution is enabling redirection from old URLs to new URLs. This, way we don't have to fix all other dead links.

If a page on your website has been moved or deleted, it may have built up SEO value over time. By redirecting the old URL to a new working URL using a 301 redirect, you can retain the SEO value and prevent your website from losing traffic and rankings.

If you have external links pointing to a page on your website that no longer exists, those links will result in a 404 error. By using a 301 redirect to redirect the old URL to a new working URL, you can fix the broken link and ensure that visitors can access the content they were looking for. 

## Enable Redirection 301 in Jekyll Minimal Mistakes

First, I was looking for ways to do it on my Jekyll blog that uses the Minimal Mistakes theme. Then I found a discussion on [minimal-mistakes issue #551](https://github.com/mmistakes/minimal-mistakes/issues/551).

They talked about this
[JekyllRedirectFrom Plugin](https://github.com/jekyll/jekyll-redirect-from), which is quite easy to use. This is how I enabled redirection to my blog.

### Install Plugin
Edit the `_config.yaml` file and add the plugin name in the following two places.
```yml
plugins:
  - jekyll-redirect-from
```

```yaml
whitelist:
  - jekyll-redirect-from
```

### How Redirection Works for a URL
In the blog post, we can simply add the array to the YAML front-matter of our page or post. For example, lik this after the title. If we have more than one old URLs, we can add all like this:
```yml
title: How to add subfigure in Latex
redirect_from:
  - /latex/add-subfig-in-latex/
  - /latex/how-to-add-subfig-in-latex/
```
or if we have only one old URL, we can do it in one line:
```yml
title: How to add subfigure in Latex
redirect_from: /latex/add-subfig-in-latex/
```


## Concluding Remarks
Overall, using a 301 redirect to fix old URL issues that lead to a 404 error is an important part of website maintenance. It helps to retain SEO value, improve the user experience, and fix broken links.

That's all for today. Cheers!!!

You can also read related posts:
1. [Google Adsense in Jekyll Static Site or Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/how-I-added-google-adsense-to-my-jekyll-minimal-mistakes-blog/)
2. [How to Enable Facebook Comments Plugin in Jekyll Blog Posts](https://shantoroy.com/jekyll/facebook-comment-plugin-jekyll-minimal-mistakes-blog-posts/)
3. [Google Analytics in Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/google-analytics-in-jekyll-minimal-mistakes-blog-theme/)
4. [Minimal Mistakes Cheat Sheet: Code Snippets I use to Blog using Jekyll and the Minimal Mistakes Theme](https://shantoroy.com/jekyll/code-snippets-I-use-for-blogging-in-minimal-mistakes/)
5. [Tools and Platforms I use for Blogging](https://shantoroy.com/blog/tools-I-use-for-blogging/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc3OTk3MzA0NF19
-->