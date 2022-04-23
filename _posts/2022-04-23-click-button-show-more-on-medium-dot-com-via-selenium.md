---
layout: single
title: "Web Scrapping: Clicking the 'Show More' Button Multiple times in Medium.com Blog via Selenium"
header:
  overlay_image: "https://live.staticflickr.com/65535/51699602895_9f512e632d_o.png"
  teaser: "https://live.staticflickr.com/65535/52023019312_ca3bbdb467_o.png"
categories:
  - WebScrapping
tags:
  - Python
  - Tutorial
  - Selenium
  - Button-Click
  - Medium blog
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "This post explains the way and provides necessary code to enable clicking on the 'show more' button on medium blog site via selenium"
---



We often need to scrap information from the Medium blog to create a dataset and need to download the content of different blog posts.

However, before scrapping a particular blog post, you need the URL and the best way to get many URLs from a single page is searching medium.com using keywords and finding all the post URLs.

Back in 2019, it was easier since then I just needed to scroll down using `selenium`. But in 2022, when I have tried to do it again, I found that they again changed the structure. Now, we need to click on a `Show more` button.

From my previous experience, I knew this is a dynamic site and the class is changed so often. Based on [this Stack Overflow Thread](https://stackoverflow.com/questions/63121107/selenium-click-on-button-by-class-name), `find_element_by_class_name`() only accept single classname. That's why they suggested using `css selector` or the `xpath`.  

I initially, tried using the `xpath` by copying it via:
1. Load a sample medium query page, e.g., https://medium.com/search?q=security
2. Right click on `show more` button
3. inspect element
4. right click on the element on the right pane
5. copy `xpath`, not `full xpath`

It looked like this:

```css
//*[@id="root"]/div/div[3]/div/div/main/div/div/div/div/div[2]/div[9]/div/div/button
```

However, this only clicked the `Show more` button once and I was wondering why! So, I went back to my regular browser, went upto the second `Show more` button and copied the `xpath` again. Now, it looks like as follows:

```css
//*[@id="root"]/div/div[3]/div/div/main/div/div/div/div/div[2]/div[19]/div/div/button
```

If you watch carefully, a particular value is chamged: $9 \rightarrow 19$. I understood, it will continue as $29, 39, \dots,49$.  So, I just needed to change the value by adding $1$ at the 67th number position.

The code is adapted from [this stackoverflow thread](https://stackoverflow.com/questions/52800174/clicking-more-button-via-selenium). You need to change the path based on where you put your webdriver. 

Also, you can customize the `max_click_SHOW_MORE` based on how many times you want to click it and load more posts.

Here is the full working code:

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver=webdriver.Chrome(chrome_options=options, executable_path=r'../chromedriver')
driver.get("https://medium.com/search?q=metamask")

initial_XPATH = "//*[@id='root']/div/div[3]/div/div/main/div/div/div/div/div[2]/div[9]/div/div/button"
max_click_SHOW_MORE = 5
count = 1 

WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, initial_XPATH))).click()

while count <= max_click_SHOW_MORE:
    try:
        time.sleep(20)
        new_XPATH = initial_XPATH[:67] + str(count) + initial_XPATH[67:]
        WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, new_XPATH))).click()
        print("Button clicked #", count+1)
        count += 1
    except TimeoutException:
        break

time.sleep(20)
driver.quit()
```

Let me know if you have any question. Thanks, have a good day!
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI2NzA0MjcxOCwxODkyMzU2OTc2XX0=
-->