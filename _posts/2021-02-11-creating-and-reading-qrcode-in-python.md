---
layout: single
title: "Creating and Reading QR Code in Python: A Simple Python Class using `qrcode` and `opencv` module"
header:
  image: "https://live.staticflickr.com/65535/51686080612_afb4e84885_o.png"
  teaser: "https://live.staticflickr.com/65535/51686080612_afb4e84885_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - QRCode
  - cv2
  - opencv
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


We often read QR codes from different products. One of the closest example is reading QR code on top of walmart products to find out the exact price.

In this post, we will create a python class that features creating and reading QR codes.

## Import Modules
Let's first import two modules

1. qrcode $\rightarrow$ for creating QR code from input data and then saving to an image file
2. cv2 $\rightarrow$ for reading a QR code from image
```python
import qrcode
import cv2
```

## Creating a Class
Now let's create a class like the following:
```python
class myQRCode:
    def __init__(self):
        self.qr = qrcode.QRCode(
                        version=2,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=5,
                    )
```
Because we are not passing anything while calling the class, we don't include any parameter in the initializer method. We only create an object of the `qrcode.QRCode()` class.

Here,
1. Version $\rightarrow$ size of the QR code. Typically ranges from $1-40$.
2. box_size $\rightarrow$ size of pixel box
3. border $\rightarrow$ thickness of the border around the code

## Other Methods
### Method for creating QR code
Now, we create a method that requires primarily two input data

1. data $\rightarrow$ The data we are gonna convert to a QR code
2. filename $\rightarrow$ The filename where we are going to save the QR code

Apart from that, for styling, we can provide two more inputs:

1. fill_color $\rightarrow$ filling the QR code with a target color
2. background_color $\rightarrow$ the background color of the QR code

Now, we add data to our early created object using the command  `self.qr.add_data(data)` and then make image using `self.qr.make_image()`. Then finally, we save the image using `<object>.save(filename)`.
```python
	def create_QR_Code(self, data, filename, fill_color=None, background_color=None):
	        self.qr.add_data(data)
	        self.qr.make(fit=True)
	        if fill_color is not None and background_color is not None:
	            img = self.qr.make_image(fill=fill_color, back_color=background_color)
	        else:
	            img = self.qr.make_image()
	        img.save(filename)
```

### Method for reading a QR code
We use `cv2.imread(filename)` to read the file where `filename` is the input for this method. Then we create an object of `cv2.QRCodeDetector()` class and decode using `detectAndDecode()` method.
```python
	def read_QR_Code(self, filename):
	        img = cv2.imread(filename)
	        det = cv2.QRCodeDetector()
	        data, bbox, straight_qrcode = det.detectAndDecode(img)
	        return data
```

## Full Code
Here is the full code:
```python
class myQRCode:
    def __init__(self):
        self.qr = qrcode.QRCode(
                        version=2,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=5,
                    )
    
    def create_QR_Code(self, data, filename, fill_color=None, background_color=None):
        self.qr.add_data(data)
        self.qr.make(fit=True)
        if fill_color is not None and background_color is not None:
            img = self.qr.make_image(fill=fill_color, back_color=background_color)
        else:
            img = self.qr.make_image()
        img.save(filename)
        
    def read_QR_Code(self, filename):
        img = cv2.imread(filename)
        det = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = det.detectAndDecode(img)
        return data
```

## Testing
Let's create two objects of our own created `myQRCode()` class and try different inputs. Then we read the files to check if the outputs are correct.
```python
obj1 = myQRCode()
obj2 = myQRCode()
obj1.create_QR_Code("This is my data", "test2.png")
print(obj1.read_QR_Code("test2.png"))
obj2.create_QR_Code("This is another data", "test3.png", 'black', 'white')
print(obj2.read_QR_Code("test3.png"))
```
Here, we see the following output on the terminal.
```
This is my data
This is another data
```

That's it for today. Until next post, Cheers!!! 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc3Nzg2NzU4M119
-->