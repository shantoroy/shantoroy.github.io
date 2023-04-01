---
layout: single
title: "Object Detection from Images and Counting Objects in Python using OpenCV and CVLib"
excerpt:  "Learn how to detect objects from images and count them using Python! In this tutorial, we will show you how to use OpenCV and CVLib to perform object detection on images. This post will walk you through each step of the process, including installing the necessary libraries, loading the image, detecting objects, and counting them. You'll also learn some useful techniques for filtering out unwanted objects and optimizing your object detection algorithm." 
seo_title:  "Object Detection from Images and Counting Objects in Python"
seo_description:  "Learn how to use OpenCV and CVLib to detect objects from images and count them in Python! This tutorial walks you through the process of installing necessary libraries, loading images, detecting objects, and filtering out unwanted objects."
header:
  image: "https://live.staticflickr.com/65535/51687913575_dc02a1466e_o.png"
  teaser: "https://live.staticflickr.com/65535/51687913575_dc02a1466e_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - image
  - cv2
  - opencv
  - object detection
  - cvlib
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Often we try to detect objects from images. Here, in this tutorial, we will use `cvlib` to detect objects and then count the occurrences of these objects in an image.

## Code
The code is self explanatory. I added comments to understand what each line does.
```python
import cv2
import matplotlib.pyplot as plt
import cvlib
from cvlib.object_detection import draw_bbox

def image_Object_Detection(image_file):
	# reading the image
    img = cv2.imread(image_file)
    # detect common objects
    bbox, label, conf = cvlib.detect_common_objects(img)
    # draw bbox around the objects
    output_image = draw_bbox(img, bbox, label, conf)
    # show and plot the image
    plt.imshow(output_image)
    plt.show()
	
	# print the number of different labels found in the images
    for item in set(label):
        print(f'Number of {item} in the image is {str(label.count(item))}')
        
if __name__=="__main__":
	# list image paths
    image_list = ['cats_dogs.png','people.jpeg']
    # call the above function for each image
    for img in image_list:
        image_Object_Detection(img)
```

## Output
Both images are downloaded from Google to test. The first photo has cats and dogs, and the second one has people in it. Here's the output after running the program.
<figure>
  <a href="https://live.staticflickr.com/65535/51687009916_98685a45b0_o.png"><img src="https://live.staticflickr.com/65535/51687009916_98685a45b0_o.png"></a>
</figure>
<br/>

In a later tutorial we will see how to detect objects from a live feed.

Till then Cheers! :sunglasses:
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU0OTQ5NTczMywxMDU0NDA1ODY3XX0=
-->