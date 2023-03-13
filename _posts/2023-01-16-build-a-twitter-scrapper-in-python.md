---
layout: single
title: "How to write a Twitter Data Scrapper in Python"
header:
  image: "https://live.staticflickr.com/65535/52696451758_de672f8380_o.png"
  teaser: "https://live.staticflickr.com/65535/52696451758_de672f8380_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - Twitter
  - tweepy
  - tweety
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "Twitter is a popular source of data (tweets), but accessing the tweets can be a challenge. Previously I scraped data from Medium. In this tutorial, I write how to build a custom data scraper using Python, so we can easily collect and store Twitter data for further data analysis."
---


There are two popular python modules that helps collect tweets via APIs: `tweepy` and `tweety`.

In this tutorial, we will find out how to work with both modules.

## `tweepy` module
To collect Twitter data using Tweepy in Python, we will need to first create a Twitter developer account and obtain our API keys and access tokens.

Now, let's do the following steps:
1. Install the Tweepy library by running `pip install tweepy` in your terminal or command prompt.
2. Let's have the basic setup
	```py
	import tweepy

	consumer_key = "CONSUMER_KEY"
	consumer_secret = "CONSUMER_SECRET"
	access_token = "ACCESS_TOKEN"
	access_token_secret = "ACCESS_TOKEN_SECRET"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	```

### Collecting Tweets
Now, we can use Tweepy to search for tweets using various parameters, such as keywords, hashtags, location, and more. Here's an example,

```py
tweets = api.search(q="Cyber Security", lang="en", tweet_mode="extended")
```

Here, The `q` parameter specifies the query string to search for, `lang` specifies the language of the tweets, and `tweet_mode` specifies that we want to retrieve the full text of the tweets.

Let's look at some other examples:

```py
tweets = api.user_timeline(screen_name="elonmusk", count=10, tweet_mode="extended")
```
Here, we are collecting 10 most recent tweets from a specific user's timeline or from a specific location.

And the following code retrieves the 100 most recent tweets containing the word `Spaceship` and located within a 50km radius of `San Francisco`:

```py
tweets = api.search(q="Spaceship", geocode="37.7749,-122.4194,50km", count=100, tweet_mode="extended")
```

### Storing Tweets
Once, we are done, we can store the tweets in a CSV or JSON file. Here's a code to store in a CSV file.

```py
import csv

with open("tweets.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Text", "Created At"])
    for tweet in tweets:
        writer.writerow([tweet.full_text, tweet.created_at])
```


## `tweety` module
There's another module named `tweety` that claims that there is no limit collecting tweets. 

This one uses `Beautifulsoup`, `requests`, and `openpyxl` to collect tweet using the frontend API.

Based on the authors [github repo](https://github.com/mahrtayyab/tweety), here's an example:

```py
#!pip install tweety-ns
from tweety.bot import Twitter

app = Twitter("elonmusk")

all_tweets = app.get_tweets()
for tweet in all_tweets:
      print(tweet)
```

That's all for today! Cheers!!! 😎
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MjIyNDc5NTIsOTY1OTgyMjM5LDExNT
U5NjI2NTVdfQ==
-->