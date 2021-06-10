---
layout: single
title: "Write a Reverse Proxy  Server in Python: Part 2 (Server Pool)"
header:
  image: "https://live.staticflickr.com/65535/51223565529_111260e908_w.jpg"
  teaser: "https://live.staticflickr.com/65535/51223565529_111260e908_w.jpg"
categories:
  - network
tags:
  - Python
  - Tutorial
  - Reverse Proxy
  - Computer Nework
  - Socket Programming
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



In the [previous post](https://shantoroy.com/network/write-a-reverse-proxy-server-in-python/), we have coded the `reverse proxy server` in python. In this post, I will cover the server code for the servers in a pool waiting to process user data.

### Required Modules
As usual, we need the similar modules that we required to build a reverse proxy server. I only add a new module here: `hashlib`. This module is used for hashing a particular data. In our setup, we will use `sha1` hashing algorithm to hash user payload and return the digest back to the user via reverse proxy.

```python
# Import required modules
import socket
import _thread
import threading
import hashlib
import json
import sys
```

## Functionalities
Each server in the pool has the following functionalities
- Connect to the Reverse Proxy by sending a particular type (type: 1) of packet 
- Receive user data (type: 2) via reverse proxy and returns processed data back to the reverse proxy server

### Packet used to Connect to a Reverse Proxy
```json
{
 "type": 1 // 1 is a connection setup message from a server
 "id": 999, // id of the server
 "privPolyId": 999, // privacy policy of the server
 "listenport": 999 // port on which the server is listening
}
```

### User data packets
```json
{
 "type": 2, // 2 is an ACK from a server to a client
 "srcid": 999, // source (server) id
 "destid": 999, // destination (client) id
 "payloadsize": 999, // payload size
 "payload": "xyz" // payload
}
```


## Coding in Python
### Option Set up
The following function checks for available options and receives each input arguments that will help us to run the servers. Here, we have to input four arguments
- id $\rightarrow$ server ID
- pp $\rightarrow$ privacy policy (indicates a particular type of service)
- listen $\rightarrow$ listening port
- revproc $\rightarrow$ reverse proxy port

It will give user the usage message if the user does not run the script based on our need.

```python
def option_check():
    global args

    # all available argument options
    avail_options = ["-id", "-pp", "-listen", "-revproc"]

    # receive user given options
    options = [opt for opt in sys.argv[1:] if opt.startswith("-")]

    # receive user given arguments
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    # raise error if user given option is wrong
    for i in options:
        if i not in avail_options:
            raise SystemExit(f"Usage: {sys.argv[0]} (-id & -pp & -listen & -revproc) <argument>...")

    # raise error if not all options or arguments are available
    if len(options) != 4 or len(args) != 4:
        raise SystemExit(f"Usage: {sys.argv[0]} (-id & -pp & -listen & -revproc) <argument>...")
```

### Receiving Packets from the Reverse Proxy Server
In our setup, any message coming from the reverse proxy has to be a user packet data. After receiving the data, the server extracts the payload and generates a hash. Then creates a new type-2 packet with changed source and destination address, payload length, and new payload (hash digest). Now, it returns the packet back to the reverse proxy.
```python
# after receiving each connection from reverse proxy/client
def on_new_client(clientsocket,addr):
    while True:

        msg = clientsocket.recv(2048)
        if not msg:
            # lock released on exit
            print_lock.release()
            break

        json_msg = json.loads(msg.decode())
        print("Received a message from client", json_msg["srcid"], "payload", json_msg["payload"])
        payload = json_msg["payload"]
        new_msg = hashlib.sha1()
        new_msg.update(payload.encode())
        hashed_payload = new_msg.hexdigest()
        new_json_msg = {"type":"2", "srcid": str(args[0]), "destid": json_msg["srcid"],\
                        "payloadsize": len(hashed_payload), "payload": hashed_payload}
        
        print("Sending a message to the client", new_json_msg["destid"], "payload", new_json_msg["payload"])
        clientsocket.send(json.dumps(new_json_msg).encode())
    clientsocket.close()
```

### Connect to the Reverse Proxy
We need a function that connects to a reverse proxy when the server script is initiated. This function binds the reverse proxy name/IP with the reverse proxy port (last argument `revproc`) and establishes a communication with the proxy server. The function also sends additional data so that the reverse proxy can record the server privacy policy, listening port, and ID.
```python
# Connect to the Reverse Proxy
def connect_reverse_proxy():
    new_json_msg = {"type":"1", "id": str(args[0]), "privPolyId": str(args[1]),\
                        "listenport": str(args[2])}
    # rev_proxy_name = 'reverseproxy.ddns.net'
    rev_proxy_name = '127.0.0.1'
    rev_proxy_port = int(args[3])

    rev_proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rev_proxy_socket.connect((rev_proxy_name, rev_proxy_port))

    rev_proxy_socket.send(json.dumps(new_json_msg).encode())
    rev_proxy_socket.close()

```

### Main Function
Now, let’s create our main program where we follow the mandatory socket communication steps (binding host and port, listening for clients, etc.). Here, we start thread for each new socket communication.
```python
if __name__ == "__main__":
    option_check()
    s = socket.socket()         # Create a socket object
    host = '127.0.0.1' # Get local machine name
    port = int(args[2])              # Reserve a port for your service.


    print ("Server running with id", args[0])
    print ("Server serving privacy policy", args[1])
    print ("Listening on port", args[2])
    
    # Broadcast "Alive" status to the Reverse Proxy first
    connect_reverse_proxy()
    print ("Connecting to the reverse proxy on port", args[3])

    # Binds to the port
    s.bind((host, port))     
    # Allow 10 clients to connect
    s.listen(10)                 

    # Receive/Process each client connection in a seperate thread
    while True:
        c, addr = s.accept()     # Establish connection with client.
        # lock acquired by client
        print_lock.acquire()
        print ('Received a message from client', addr, "payload")
        _thread.start_new_thread(on_new_client,(c,addr))
        
    s.close()
```

The entire code is available in [Github](https://github.com/shantoroy/reverse_proxy/blob/master/server.py).

In the next tutorial, we will code the client-side script. Stay Tuned!

The whole tutorial series is listed here:
* [Write a Reverse Proxy Server in Python: Part 1 (Reverse Proxy Server)](https://shantoroy.com/network/write-a-reverse-proxy-server-in-python/)
* [Write a Reverse Proxy Server in Python: Part 2 (Server Pool)](https://shantoroy.com/network/write-a-reverse-proxy-in-python-part-02-servers/)
* [Write a Reverse Proxy Server in Python: Part 3 (Client-side Script)](https://shantoroy.com/network/write-a-reverse-proxy-server-client-side-script/)
* [Write a Reverse Proxy Server in Python: Part 4 (Shell Script for Automation)](https://shantoroy.com/network/write-a-reverse-proxy-in-python-automation-shell-script/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDIwNDU0MjYxLDg0OTY3MDMwMCw1MDIwMz
I1NzIsLTEyNTUwNTczODMsLTIxNDQ2OTM3OTldfQ==
-->