---
layout: single
title: "Simple and Short Interesting Python Code Snippets for your Projects"
excerpt:  "If you're looking for some interesting and useful Python code snippets to use in your projects, look no further. In this blog post, we've compiled a list of simple and short Python code snippets that you can use to make your projects more efficient and effective. Whether you're a beginner or an experienced developer, these snippets are sure to come in handy."
seo_title:  "Simple and Short Interesting Python Code Snippets for your Projects" 
seo_description:  "Looking for some useful Python code snippets for your projects? Check out this blog post for a list of simple and short Python code snippets that you can use to make your projects more efficient and effective."
header:
  image: "https://live.staticflickr.com/65535/51716722206_4eba6e6d3b_o.png"
  teaser: "https://live.staticflickr.com/65535/51716722206_4eba6e6d3b_o.png"
categories:
  - Python
tags:
  - Python
  - Snippets
  - Projects
  - OpenCV
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Here, in this post, I have added a few necessary code snippets that we might need to use for our Python projects. Most of the codes are self-explanatory with variable names or comments. That's why, I am ignoring adding additional descriptions, for now, will add later.

### Text to Voice
```python
# for using gTTS module install as follows:
# pip install gTTS

# for installing a voice player:
# apt/brew install mpg123

from gtts import gTTS
import os

def textToVoice(input_text, filename, language):
    text2speech = gTTS(text=input_text, lang=language)
    tts.save(filename)
    os.system("mpg123 " + filename)

if __name__=="__main__":
    text = "How you doing!"
    filename = "test.mp3"
    language = "en"
    textToVoice(text, filename, language)
```


### password generator

```python
def random_password_genarator(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    mix = lower + upper + digits + symbols
    password = "".join(random.sample(mix, length))
    return password

print(random_password_genarator(10))
```
 
### Text to handwriting (It will save the output in a png file)
```python
# !pip install pywhatkit
import pywhatkit as py
py.text_to_handwriting("This is a test", rgb=(0,0,255))
```

### Capture Video Frame
```python
import cv2
# Initialize video capture object
capture = cv2.VideoCapture(0)

# Loop until a selected key  
while True:  
	# Capture the current frame  
	ret, frame = capture.read()

	# Display the frame
	# for jupyter notebook use plt.imshow(frame)
	# check all the changes in the `face detection` code
	cv2.imshow('captured frame', frame)

	# Detect if the 'q' is pressed
	# waitKey() returns the ASCII code of the key pressed
    exit_key = cv2.waitKey(1)
    # check complete code list here:
    # https://theasciicode.com.ar/
    if exit_key == 113:
        break

# Release the capture object after loop
capture.release()

# Destroy all windows
cv2.destroyAllWindows()
```

### Face detection
```python
# uncomment this if using jupyter notebook
# %matplotlib inline

import cv2
# uncomment this if using jupyter notebook
# from matplotlib import pyplot as plt

# Load the cascade
# download the xml from here:
# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# input image
img = cv2.imread('person.jpeg')

# need to convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# # Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,
                            minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
# output
# uncomment following two lines if using jupyter notebook
# plt.imshow(img)
# plt.show()

# comment following lines if using jupyter notebook
cv2.imshow("faces", img)
cv2.waitKey(0)
# uncomment following if having any trouble using cv2
# cv2.destroyAllWindows()
# cv2.waitKey(1)
```

### Scraping a web article
```python
# !pip3 install newspaper3k
import newspaper

url = "https://shantoroy.com/security/personal-security-awareness-and-best-practices/"

article = newspaper.Article("%s" % (url), language="en")
article.download()
article.parse()
article.nlp()

print(article.title,"\n")
print(article.text,"\n")
print(article.summary,"\n")
print(article.keywords,"\n")
``` 

### A simple translator
```python
# !pip install translate

from translate import Translator
trans_obj = Translator(from_lang="english",to_lang="spanish")
print(trans_obj.translate("Good Morning!"))
```

If someone is trying `googletrans` module, you might find several issues. Just check the [stack overflow thread](https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group) for solution.

### Encryption and Decryption using Fernet
```python
# !pip install cryptography

from cryptography.fernet import Fernet

key = Fernet.generate_key()
crypt = Fernet(key)
enc_data = crypt.encrypt(b"A secret text message.")
print(enc_data)
print(crypt.decrypt(enc_data))

# b'gAAAAABhlqkqj5zxFarXH5sZO9E-SpkqyfmKMV91C-oJ1L8vJes1bre_S2kTUKYGrgTh74gAZVRoQ8KLgS3wBFA4tndy7Wd5VW2jmTIujJtsrgw2Gygj2a4='
# b'A secret text message.'
```

### Hash a password using `hashlib`
```python
import uuid
import hashlib

def hash_password(password):
    # generate a random salt
    salt = uuid.uuid4().hex
    salted_password = salt.encode() + password.encode()
    return hashlib.sha256(salted_password).hexdigest()

print(hash_password("password"))
```

### Encryption Decryption using `pycrypto`module

```python
# !pip install pycrypto

from os import urandom
from Crypto.Cipher import AES

def AES_encrypt(secret,iv,mode,data):
    enc = AES.new(secret, mode, iv)
    return data, enc.encrypt(data)

def AES_decrypt(secret,iv,mode,data):
    dec = AES.new(secret, mode, iv)
    return dec.decrypt(data).decode('utf-8')

if __name__=="__main__":
    secret = urandom(16)
    iv = urandom(16)
    mode = AES.MODE_CBC
    
    msg, encrypted_msg = AES_encrypt(secret, iv, mode, "this is a crypto")
    print(encrypted_msg)
    print(AES_decrypt(secret, iv, mode, encrypted_msg))
```

That's it for now, I will keep updating this post by adding more code snippets.

Have a good day! :sunglasses:
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg2MTgwNjI1MSw1NTU0MzA1NDddfQ==
-->