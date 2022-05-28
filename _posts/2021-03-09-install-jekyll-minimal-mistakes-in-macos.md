---
layout: single
title: "How to install Jekyll with the Minimal Mistakes Theme in macOS"
header:
  image: "https://live.staticflickr.com/65535/52104048713_44e91fe733_o.png"
  teaser: "https://live.staticflickr.com/65535/52104048713_44e91fe733_o.png"
categories:
  - Blogging
tags:
  - Blogging
  - Tutorial
  - Jekyll
  - Minimal Mistakes
  - TmacOS
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



I have been using Jekyll Blog platform for two years and have been using the most popular and well-maintained theme `minimal mistakes` in this blog. 

Although I have always used the blog repository via `github-pages`, recently, I wanted to test some issues by running a site in the local machine.

Therefore, in this tutorial, I will show you how to run a Jekyll blog in your local machine. In this example, I will show how to use the `minimal mistakes` theme.

## Prerequisites
-   [Ruby](https://www.ruby-lang.org/en/downloads/)  version  **2.5.0**  or higher, including all development headers (check your Ruby version using  `ruby -v`)
-   [RubyGems](https://rubygems.org/pages/download)  (check your Gems version using  `gem -v`)
-   [GCC](https://gcc.gnu.org/install/)  and  [Make](https://www.gnu.org/software/make/)  (check versions using  `gcc -v`,`g++ -v`, and  `make -v`)

If the prerequisites are not installed on your system, just install them first.

## Install Jekyll
Once you have the prerequisites, install `jekyll` and `bundler` via `gem`.
```bash
gem install jekyll bundler
```

Now, let's create a directory which will serve as our blog directory. 
```bash
mkdir newblog
jekyll new newblog
cd newblog
```

After going to the directory, let's run the following:
```bash
bundle exec jekyll serve
```

Now, you will be able to see your blog in the `http://127.0.0.1:4000/` address on your browser.

## Install Minimal Mistakes
Copy following contents to the `Gemfile`

```
source "https://rubygems.org"

# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!

# gem "github-pages", group: :jekyll_plugins

# To upgrade, run `bundle update`.

gem "github-pages", group: :jekyll_plugins
gem "minimal-mistakes-jekyll"

# The following plugins are automatically loaded by the theme-gem:
#   gem "jekyll-paginate"
#   gem "jekyll-sitemap"
#   gem "jekyll-gist"
#   gem "jekyll-feed"
#   gem "jekyll-include-cache"
#
# If you have any other plugins, put them here!
# Cf. https://jekyllrb.com/docs/plugins/installation/
group :jekyll_plugins do
end
```

Then run the following command

```bash
$ bundle install
```

Now, again run the following:

```bash
bundle exec jekyll serve
```

That's all! Cheers!!! :sunglasses:
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjI5MTAwNTEwXX0=
-->