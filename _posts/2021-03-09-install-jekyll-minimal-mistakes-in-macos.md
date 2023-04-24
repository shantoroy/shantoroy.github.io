---
layout: single
title: "How to install Jekyll with the Minimal Mistakes Theme in macOS"
excerpt:  "In this tutorial, you will learn how to install Jekyll, a simple static site generator, on macOS and use the popular Minimal Mistakes theme to create a clean and professional-looking website. This step-by-step guide is designed to help both beginners and experienced developers get started with Jekyll and Minimal Mistakes quickly and easily."
seo_title:  "How to Install Jekyll with the Minimal Mistakes Theme in macOS | Step-by-Step Guide" 
seo_description:  "Learn how to install Jekyll on macOS and create a stunning website with the popular Minimal Mistakes theme. This easy-to-follow tutorial includes step-by-step instructions and helpful tips for beginners and experienced developers alike. Get started with Jekyll and Minimal Mistakes today!"
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

That's all! Cheers!!! 


## Related Posts on Jekyll/ Minimal Mistakes
* [Google Adsense in Jekyll Static Site or Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/how-I-added-google-adsense-to-my-jekyll-minimal-mistakes-blog/)
* [Google Analytics in Minimal Mistakes Blog Theme](https://shantoroy.com/jekyll/google-analytics-in-jekyll-minimal-mistakes-blog-theme/)
* [How to Enable Facebook Comments Plugin in Jekyll Blog Posts](https://shantoroy.com/jekyll/facebook-comment-plugin-jekyll-minimal-mistakes-blog-posts/)
* [Minimal Mistakes Cheat Sheet: Code Snippets I use to Blog using Jekyll and the Minimal Mistakes Theme](https://shantoroy.com/jekyll/code-snippets-I-use-for-blogging-in-minimal-mistakes/)
* [Jekyll SEO: How to Find and Fix 404 Error on a Jekyll (Minimal Mistakes) Blog Website](https://shantoroy.com/jekyll/jekyll-seo-find-and-fix-404-error-on-jekyll-minimal-mistake-blog/)
* [Medium: How to Effectively Perform Search Engine Optimization to a Jekyll (Minimal Mistakes) Blog Post Header](https://medium.com/@shantoroy/how-to-effectively-perform-search-engine-optimization-to-a-jekyll-minimal-mistakes-blog-post-9c3a17865eca)
* [How to Add Latex Math to Jekyll-based Theme- Minimal Mistakes](https://shantoroy.com/jekyll/add-latex-math-to-jekyll-blog-minimal-mistakes/)
* [Tools and Platforms I use for Blogging](https://shantoroy.com/blog/tools-I-use-for-blogging/)

<!--stackedit_data:
eyJoaXN0b3J5IjpbNjM3MTY3MDA3LDYyOTEwMDUxMF19
-->