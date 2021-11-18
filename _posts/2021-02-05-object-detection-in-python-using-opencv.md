---
layout: single
title: "Object Detection from Images and Counting Objects in Python using OpenCV and CVLib"
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
eyJoaXN0b3J5IjpbMTA1NDQwNTg2N119
-->