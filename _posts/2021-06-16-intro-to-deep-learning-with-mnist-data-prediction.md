---
layout: single
title: "Introduction to Deep Learning in Python (Keras and Tensorflow) using the MNIST Dataset"
header:
  image: "https://live.staticflickr.com/65535/51255187292_17ae375815_b.jpg"
  teaser: "https://live.staticflickr.com/65535/51255187292_17ae375815_b.jpg"
categories:
  - machine-learning
tags:
  - Machine-learning
  - Deep-learning
  - Deep Neural Network
  - Neural Network
  - Tutorial
  - Classification
  - Recurrent Neural Network
  - Convolutional Neural Network
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



In this post we will see how to implement basic deep learning in python (Keras and Tensorflow). To make the post shorter, I skip the theoretical basics in this post.

We will implement a basic deep neural network, a convolutional neural network, and a recurrent neural network to learn the MNIST data in this post.

## Prerequisite
We will use the following modules and classes in our implementation. 
```python
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, LSTM
from keras.utils import normalize
import numpy as np
import matplotlib.pyplot as plt
```

### Modules
* tensorflow $\rightarrow$ for importing the dataset
* keras $\rightarrow$ to use artificial neural network (ANN) functionalities
* numpy and matplotlib $\rightarrow$ check the prediction and plot the image

We will use the following classes for different types of neural networks
#### Common
* DNN $\rightarrow$ Dense, Flatten, Dropout

#### Additional
* CNN $\rightarrow$ Conv2D, MaxPooling2D
* RNN $\rightarrow$ LSTM

Here, `Dense`, `Flatten`, and `Dropout` are common in all types of ANNs. Let's take a brief look at what functionalities these classes/methods provide

*  Dense $\rightarrow$ neural network layer that feeds all outputs from previous layer to its neurons
* Flatten $\rightarrow$ serialize a multi-dimensional tensor (e.g., 10x10 2D image to 1x100 flat data)
* Dropout $\rightarrow$ prevents overfitting by randomly selecting nodes to be dropped out with a given input probability
* conv2D $\rightarrow$ Filter image data while maintaining the relations between pixels, e.g., 3x3 pixel filter (CNN is mainly used for image type data)
* MaxPooling2D $\rightarrow$ reduces spatial size by counting the max values within the 2x2 pixel boundaries

## Load Data
Let's first download the MNIST data. Here, we download the dataset using the tensorflow keras API and then normalize the data. For CNN, the additional work is to reshape the train and test data as 4-dimensional numpy arrays.
### Load data for NN and RNN
```python
def load_data_NN():
    # load mnist dataset
    mnist = tf.keras.datasets.mnist  # 28 x 28 images of 0-9
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # normalize data
    x_train = normalize(x_train, axis = 1)
    x_test = normalize(x_test, axis = 1)
    return x_train, y_train, x_test, y_test
```

### Load data for CNN
```python
def load_data_CNN():
    # load mnist dataset
    mnist = tf.keras.datasets.mnist  # 28 x 28 images of 0-9
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # reshape data
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    # convert from integers to floats
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    # normalize data
    x_train = normalize(x_train, axis = 1)
    x_test = normalize(x_test, axis = 1)
    return x_train, y_train, x_test, y_test
```

## Neural Network Models
Usually most of the layers except the final output layers use the `relu` activation. In our final layer, we will use `softmax` as it converts the scores to a normalized probability distribution.

Additionally, as the model parameters, we will use the `adam` optimizer and `sparse_categorical_crossentropy` loss function. You can take a look at the list of all available optimizers [here](https://keras.io/api/optimizers/).

### A simple DNN
```python
def simple_DNN():
    model = Sequential()
    model.add(Flatten())  # input layer
    model.add(Dense(128, activation = 'relu'))
    model.add(Dense(128, activation = 'relu'))
    model.add(Dense(10, activation = 'softmax'))

    model.compile(optimizer= "adam", 
                  loss= "sparse_categorical_crossentropy", 
                  metrics=["accuracy"])
    return model
```

### Recurrent Neural Network (LSTM)
```python
def RNN(input_shape):
    model.add(LSTM(128, input_shape=input_shape, activation = 'relu', return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(128, input_shape=input_shape, activation = 'relu'))
    model.add(Dropout(0.2))
    model.add(Dense(32, activation = 'relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation = 'softmax'))

    model.compile(optimizer= "adam", 
                  loss= "sparse_categorical_crossentropy", 
                  metrics=["accuracy"])
    return model
```

### Convolutional Neural Network
```python
def conv_NN(input_shape):
    model = Sequential()

    model.add(Conv2D(32, (3,3),  input_shape = input_shape))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Flatten())  # converts 3D feature maps to 3D feature vectors
    model.add(Dense(100, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    model.compile(loss="sparse_categorical_crossentropy",
                 optimizer="adam",
                 metrics=["accuracy"])
    return model
```

## Additional Utilities
The following function will help us to check the prediction output of a particular index of the image dataset.

```python
def sample_prediction(index):
    plt.imshow(x_test[index].reshape(28, 28),cmap='Greys')
    pred = model.predict(x_test[index].reshape(1, 28, 28, 1))
    print(np.argmax(pred))
```

## Main Function
Now, we can train and test the dataset with our built neural networks.
### DNN
```python
if __name__ == "__main__":
    # load data
    x_train, y_train, x_test, y_test = load_data_NN()
	# load the model
    model = simple_DNN()
    
    print("\n\nModel Training\n")
    model.fit(x_train, y_train, epochs = 5)
    
    print("\n\nModel Evaluation\n")
    model.evaluate(x_test, y_test)
    
    print("\n\nSample Prediction")
    sample_prediction(0)
```

### RNN
```python
if __name__ == "__main__":
    # load data
    x_train, y_train, x_test, y_test = load_data_NN()
    
    # load model
    model = RNN(x_train.shape[1:])
    
    print("\n\nModel Training\n")
    model.fit(x_train, y_train, epochs = 5)
    
    print("\n\nModel Evaluation\n")
    model.evaluate(x_test, y_test)
    
    print("\n\nSample Prediction")
    sample_prediction(0)
```

### CNN
```python
if __name__ == "__main__":
    # load data
    x_train, y_train, x_test, y_test = load_data_CNN()
    
    # load model
    input_shape = (28,28,1)
    model = conv_NN(input_shape)
    
    print("\n\nModel Training\n")
    model.fit(x_train, y_train, epochs = 5)
    
    print("\n\nModel Evaluation\n")
    model.evaluate(x_test, y_test)
    
    print("\n\nSample Prediction")
    sample_prediction(0)
```

For now, the post is very short. I will keep adding contents and details over time with further explanation. Cheers!




## References
* [Introduction to Deep Learning - Deep Learning basics with Python, TensorFlow and Keras p.1](https://pythonprogramming.net/introduction-deep-learning-python-tensorflow-keras/)
* [Recurrent Neural Networks - Deep Learning basics with Python, TensorFlow and Keras p.7](https://pythonprogramming.net/recurrent-neural-network-deep-learning-python-tensorflow-keras/)
* [Image Classification in 10 Minutes with MNIST Dataset](https://towardsdatascience.com/image-classification-in-10-minutes-with-mnist-dataset-54c35b77a38d)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcyODQyNjI4MywtNTkyMzA3NjQwLDExMD
Q0OTg0MzksLTE5OTcwMDc0NDZdfQ==
-->