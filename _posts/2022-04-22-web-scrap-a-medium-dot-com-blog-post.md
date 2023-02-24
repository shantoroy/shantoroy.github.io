---
layout: single
title: "Web Scrapping: Finding Necessary Contents from a Medium Dot Com Blog Post"
excerpt:  "Are you tired of manually copying and pasting data from a Medium blog post? In this tutorial, we will learn how to extract the necessary contents from a Medium.com blog post using web scraping techniques, especially the items like post title, author names, blog content, tags, publish dates, number of claps, comments, etc."
seo_title:  Your  meta  title  
seo_description:  Your  meta  description
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/52024571959_915c770b73_o.png"
categories:
  - WebScrapping
tags:
  - Python
  - Tutorial
  - Requests
  - Beautifulsoup
  - Medium blog
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post explains the way and provides necessary code to scrap a post from Medium dot com Blog"
---


Sometime we need to to scrap contents of an article from medium blog to create a dataset or analyze data.

Here, in this post, I will provide necessary code to scrap different contents of a blog post from Medium. 

### Necessary Modules
Let's first install the following modules. `Beautifulsoup` and `requests` are our primary modules, which are popular for this type of task. Then we need `json` and `re` for some little tuning tasks.
```python
from bs4 import BeautifulSoup
import requests
import json
import re
```

### Scrapping Specific Content
Here is a class that includes method for collecting following information:

1. post title
2. author name
3. author link
4. publish date
5. post tags
6. readtime
7. no. of claps
8. no. of voters
9. no. of post responses

 
```python
class PostDetais(object):
    def __init__(self, soup, link=None):
        self.page_soup = soup
        self.link = link
    
    # returns the basic JSON response
    # collection target -> title, author infos, publication dates, tags, post links etc
    def json_response_basic(self):
        try:
            for my_tag in self.page_soup.find_all('script', {
                'type': "application/ld+json"}):
                res = my_tag.text
                return res
        except Exception as e:
            error_trace = {}
            error_trace["link"] = self.link
            error_trace["method"] = "get_response"
            error_trace["message"] = str(e)
            print(json.dumps(error_trace, indent=4))
        return ""
    
    # returns a larger json response with rigorous information
    # collection target -> read time, upvotes, responses etc
    def json_response_whole(self):
        try:
            # [source: https://stackoverflow.com/questions/13323976/how-to-extract-a-json-object-that-was-defined-in-a-html-page-javascript-block-us 
            # script = re.compile('window.__APOLLO_STATE__ = ({.*})', re.DOTALL)
            # json_text = script.search(str(self.page_soup)]
            # following code of mine looks simpler :D
            for tag in self.page_soup.find_all('script'):
                if 'window.__APOLLO_STATE__' in tag.text:
                    data = tag.text
            return data[26:]
        except Exception as e:
            error_trace = {}
            error_trace["link"] = self.link
            error_trace["method"] = "get_response"
            error_trace["message"] = str(e)
            print(json.dumps(error_trace, indent=4))
        return ""
    
    # find particular first key that is required in the larger json response
    # we're using regex as post number will be different for each post
    # we know that the post key starts with "Post:"
    def find_first_key(self, json_data):
        find_key_string = [re.compile("^Post:*").match]
        required_key = [k for k,v in json_data.items()
                if any (item(k) for item in find_key_string)]
        return required_key[0]
    

    # return post title using h1 tag
    # it could be collected from the basic json response as well
    def get_title(self):
        try:
            for my_tag in self.page_soup.find_all('h1'):
                title = my_tag.text
                return title
        except Exception as e:
            error_trace = {}
            error_trace["link"] = self.link
            error_trace["method"] = "get_title"
            error_trace["message"] = str(e)
            print(json.dumps(error_trace, indent=4))
        return ""
    
    # returns two values: name and url
    def get_author_name(self, json_data):
        try:
            author_name = json_data['author']['name']
            author_url = json_data['author']['url']
            return author_name, author_url
        except Exception as e:
            error_trace = {}
            error_trace["link"] = self.link
            error_trace["method"] = "get_title"
            error_trace["message"] = str(e)
            print(json.dumps(error_trace, indent=4))
        return ""
    
    # return 3 dates for a post- creation, publication, & last modification date
    def get_date(self, json_data):
        try:
            creation_date = json_data['dateCreated']
            published_date = json_data['datePublished']
            last_modification_date = json_data['dateModified']
            return creation_date, published_date, last_modification_date
        except Exception as e:
            error_trace = {}
            error_trace["link"] = self.link
            error_trace["method"] = "get_title"
            error_trace["message"] = str(e)
            print(json.dumps(error_trace, indent=4))
        return ""
    
    
    def get_tags(self, key, json_data):
        try:
            tags = []
            for item in json_data[key]['tags']:
                tags.append(item["__ref"][4:])
            return tags
        except Exception as e:
            error_trace = {}
            error_trace["link"] = self.link
            error_trace["method"] = "get_tags"
            error_trace["message"] = str(e)
            print(json.dumps(error_trace, indent=4))
        return ""

    def get_read(self, key, json_data):
        try:
            read = json_data[key]['readingTime']
            return read
        except Exception as e:
            error_trace = {}
            error_trace["link"] = self.link
            error_trace["method"] = "get_title"
            error_trace["message"] = str(e)
            print(json.dumps(error_trace, indent=4))
        return ""

    def get_upvote(self, key, json_data):
        try:
            clap_count = json_data[key]['clapCount']
            voter_count = json_data[key]['voterCount']
            return clap_count, voter_count
        except Exception as e:
            error_trace = {}
            error_trace["link"] = self.link
            error_trace["method"] = "get_upvote"
            error_trace["message"] = str(e)
            print(json.dumps(error_trace, indent=4))
        return ""


    def get_post_content(self):
        try:
            # class_="section-content"
            # we are using <article> tag as section-content class no longer works
            # everything is inside the article tag including title & author names
            for content in self.page_soup.find_all('article'):
                return content.text
        except Exception as e:
            error_trace = {}
            error_trace["link"] = self.link
            error_trace["method"] = "get_post_content"
            error_trace["message"] = str(e)
            print(json.dumps(error_trace, indent=4))
        return ""
    
    
    def get_response(self, key, json_data):
        try:
#             res = json_data[key]['responsesCount']
            res = json_data[key]['postResponses']
            return res["count"]
        except Exception as e:
            error_trace = {}
            error_trace["link"] = self.link
            error_trace["method"] = "get_response"
            error_trace["message"] = str(e)
            print(json.dumps(error_trace, indent=4))
        return ""
```


### Download Page Source
Let's collect the page contents using the `requests` module. Then we need to parse it using `Beautifulsoup` HTML parser. 

Since, Medium is a dynamic site and you just simply cannot scrap contents using `class` elements. That's why I found a new way to do it: getting the JSON stored within the source. So, here, I just separately, store the JSON contents.
```python
headers = requests.utils.default_headers()
headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })
link = "https://medium.com/startup-grind/i-was-wrong-about-ethereum-804c9a906d36"
request_link = requests.get(link, headers=headers)
#request_link = urllib.request.urlopen(link, headers=headers)
request_content = BeautifulSoup(request_link.content,'html.parser')
post_details = PostDetais(request_content, link)

json_basic_script = json.loads(post_details.json_response_basic())
json_full_script = json.loads(post_details.json_response_whole())
first_key_element = post_details.find_first_key(json_full_script)
```


### Storing each content
Now, let's just call each method from our class and store corresponding contents in separate variables.
```python
post_title = post_details.get_title()
author_name, author_link = post_details.get_author_name(json_basic_script)
creation_date, published_date, modified_date = post_details.get_date(json_basic_script)
post_tags = post_details.get_tags(first_key_element, json_full_script)
post_readtime = post_details.get_read(first_key_element, json_full_script)
post_claps, post_voters = post_details.get_upvote(first_key_element, json_full_script)
post_contents = post_details.get_post_content()
post_responses = post_details.get_response(first_key_element, json_full_script)
```


### Checking the Output
If you print all the variables now, we will get the corresponding outputs as follows:
```python
print(post_title)
print(author_name)
print(author_link)
print(published_date[:10])
print(post_tags)
print((str(post_readtime))[:4])
print(post_claps)
print(post_voters)
print(post_responses)
```


```output
I was wrong about Ethereum
WhalePanda
[https://medium.com/@WhalePanda](https://medium.com/@WhalePanda)
2017-06-12
['blockchain', 'bitcoin', 'ethereum', 'fintech', 'finance']
8.61
3980
1718
131
```


That's all for today. Chill!!! :sunglasses:
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM0MDUzMjc1MCw1MTc5NzY3NDZdfQ==
-->