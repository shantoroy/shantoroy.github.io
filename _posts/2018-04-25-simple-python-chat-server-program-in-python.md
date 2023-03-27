---
layout: single
title: "A simple Half-Duplex Chatting program in Python"
header: 
  image: "https://farm1.staticflickr.com/980/41781019432_d3614829b6_b.jpg"
  teaser: "https://farm1.staticflickr.com/980/41781019432_d3614829b6_b.jpg"
categories: 
  - Tutorial
tags:
  - Python
  - Socket Programming
toc: true
toc_label: "Table of Contents"
toc_icon: "heart" 
---


Python is the most popular programming language for it's readability and generally anything can be built using this pseudo-code alike language. It is best suited for scripting, Data Science, Machine learning, back-end web development, artificial intelligence and scientific researches.

In this blog article we will find out how to write a simplest half duplex TCP chat application written in python. 

Before starting, let's learn a little about socket programming. 

## What is Socket?
>A socket is one of the most fundamental technologies of computer network programming. Sockets allow network software applications to communicate using standard mechanisms built into network hardware and operating systems. [^1]

>A network socket is one endpoint in a communication flow between two programs running over a network. [^2]

Well, a definition is not enough. For practical implementation we will have to know about the `socket` module of python. And obviously about the methods those will be called in from that module.

## TCP Socket Stages
The following diagram presents the stages of a TCP (connection-oriented) socket.
<figure>
  <a href="https://farm1.staticflickr.com/978/26960685907_41839085e6_b.jpg"><img src="https://farm1.staticflickr.com/978/26960685907_41839085e6_b.jpg"></a>
</figure>

Now let's look at the methods of python for socket programming.

## Socket Methods
### Server Socket Methods
<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">s.bind()</td>
<td markdown="span">binds address (hostname, port number pair) to socket</td>
</tr>
<tr>
<td markdown="span">s.listen()</td>
<td markdown="span">sets up and start TCP listener</td>
</tr>
<tr>
<td markdown="span">s.accept()</td>
<td markdown="span">passively accept TCP client connection, waiting until connection arrives</td>
</tr>
</tbody>
</table>

### Client Socket Methods
<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">s.connect()</td>
<td markdown="span">initiates TCP server connection</td>
</tr>
</tbody>
</table>

### Common Socket Methods
<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">s.recv()</td>
<td markdown="span">receives TCP message</td>
</tr>
<tr>
<td markdown="span">s.send()</td>
<td markdown="span">transmits TCP message</td>
</tr>
<tr>
<td markdown="span">s.close()</td>
<td markdown="span">closes socket</td>
</tr>
</tbody>
</table>


## Chat Application Code
### Server side Script

```python
# Server Side Script
# Supports Python v3.*

from socket import *
server_port = 5000
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)
print ("Welcome: The server is now ready to receive")
connection_socket, address = server_socket.accept()
while True:
  sentence = connection_socket.recv(2048).decode()
  print('>> ',sentence)
  message = input(">> ")
  connection_socket.send(message.encode())
  if(message == 'q'):
    connectionSocket.close()
```



### Client Side Script

```python
# Client Side Script
# Supports Python v3.*

from socket import *
server_name = 'localhost'
server_port = 5000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))

while True:
  sentence = input(">> ")
  client_socket.send(sentence.encode())
  message = client_socket.recv(2048)
  print (">> ", message.decode())
  if(sentence == 'q'):
    client_socket.close()
```

Save the server side code in a file and name it as `server.py` or anything as you wish. Also save the client side code in another file and name as `client.py`. You can run the code in windows command prompt (cmd) by opening it in the directory you stored your script file. Then type `python server.py`and hit Enter. Running `client.py` will require another cmd window. Type there as `python client.py` and hit enter. You will get a message in the server side that a client is connected. Now, you can send and receive message from and to both ends.


[^1]: An Overview of Socket Programming for Computer Networking- [lifewire](https://www.lifewire.com/socket-programming-for-computer-networking-4056385)

[^2]: Network Socket definition - [techtarget](https://whatis.techtarget.com/definition/sockets)

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjk0MzIzMDQsLTY5OTk3MzQ5N119
-->