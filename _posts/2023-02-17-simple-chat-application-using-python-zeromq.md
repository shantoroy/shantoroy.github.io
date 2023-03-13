---
layout: single
title: "Python ZeroMQ Module: A Simple Publisher-Subscriber Chat Application"
header:
  image: "https://live.staticflickr.com/65535/52696720985_7cff7b56a3_o.png"
  teaser: "https://live.staticflickr.com/65535/52696720985_7cff7b56a3_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - ZeroMQ
  - Publisher-subscriber
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "Learn how to build a simple chat application using Python and the ZeroMQ module! Our step-by-step guide will teach you about publisher-subscriber messaging and how to use ZeroMQ to create a real-time chat experience between multiple people."
---


ZeroMQ is a high-performance messaging library that makes it easy to build distributed applications. 

In this tutorial, we'll use ZeroMQ to create a simple publisher-subscriber model-based chat application in Python that allows users to send messages to each other in real-time.

First, let's install the PyZMQ library.

```py
pip install pyzmq
```

## Server and Client Codes
Let's first create a client using the library to create a chat application using the Request-Reply messaging pattern. In the following example let's use port $5000$.

```py
# client.py
import zmq
context = zmq.Context()

# Create a socket to send messages to the server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5000")

while True:
    message = input("me: ")
    socket.send_string(message)

    # Wait for the server's response
    response = socket.recv_string()
    print("Alice:", response)
```

Here's the code for the server:

```py
# server.py
import zmq
context = zmq.Context()

# Create a socket to receive messages from the client
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5000")

while True:
    # Wait for a message from the client
    message = socket.recv_string()
    print("Bob:", message)

    # Send a response back to the client
    response = input("Me: ")
    socket.send_string(response)
```

Now, we need to open to terminal tabs/windows. And run one of the following in each.

```bash
(venv)$ python server.py
```

```bash
(venv)$ python client.py
```

## Chat Application for Multiple users
To allow multiple people to participate in the chat, we can use the Publish-Subscribe messaging pattern. 

In this pattern, each person acts as a publisher, publishing messages to a single topic, and a subscriber, subscribing to messages on that topic.

### Publisher Code

```py
# publisher.py
import zmq
context = zmq.Context()

# Create a socket to publish messages to the subscribers
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    message = input("You: ")
    socket.send_string(message)
```

### Subscriber Code

```py
# subscriber.py
import zmq
context = zmq.Context()

# Create a socket to subscribe to messages from the publisher
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    # Wait for a message from the publisher
    message = socket.recv_string()
    print(message)
```

Now, let's start the publisher (person 1) in one terminal window

```bash
(venv)$ python publisher.py
```

And then start the subscribers (person 2+) in separate terminal windows:
```bash
(venv)$ python subscriber.py
```

Please note that, in this example, we're using the default topic, which is an empty string. If you want to use a specific topic, you can specify it using the `socket.setsockopt_string(zmq.SUBSCRIBE, "<topic>")` method on the subscriber socket, and the `socket.send_string(message, zmq.SNDMORE)` method on the publisher socket, where `"<topic>"` is the name of the topic we want to use.


Here's one issue though. Only the publisher can send message and every subscriber only listens. If we want all users to interact simulatneously, we need a `Push-Pull` pattern, we have multiple "pushers" and multiple "pullers." The pushers send messages to a queue, and the pullers receive messages from the same queue.


## Final Code
Let's use thread to handle `subscribe` and `publish` at the same time.

```py
# user.py
import zmq
import threading

def subscriber():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://localhost:5005")
    while True:
        message = socket.recv_string()
        print(message)

def publisher():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://*:5005")
    while True:
        message = input()
        socket.send_string(message)

if __name__ == "__main__":
    threading.Thread(target=subscriber).start()
    publisher()
```
Now we need to run `user.py` in different terminal tabs/windows based on how many users we want.

Note that, here, the subscriber listens for messages from the socket and prints them to the console, while the publisher waits for user input and sends the input as a message to the socket.


## Concluding Remarks
This is not a full-functional chat application. I just wanted to explore zeroMQ and the first thing came to mind was a chat application as this library provides messaging system across distributed systems.

That's all for today! Cheers!!! 😎
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY1ODIwODY5Nyw5MzcwNzYyM119
-->