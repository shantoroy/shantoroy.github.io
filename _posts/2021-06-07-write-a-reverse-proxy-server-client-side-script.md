---
layout: single
title: "Write a Reverse Proxy  Server in Python: Part 3 (Client-side Script)"
excerpt:  "In this third part of the "Write a Reverse Proxy Server in Python" series, we'll cover the client-side script implementation. The client-side script is the script that the end-user interacts with when they try to access the resources on the backend server."
seo_title:  Your  meta  title  
seo_description:  Your  meta  description
header:
  image: "https://live.staticflickr.com/65535/51223565539_e5e45f3896_w.jpg"
  teaser: "https://live.staticflickr.com/65535/51223565539_e5e45f3896_w.jpg"
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


In our previous two posts, we have coded our `reverse proxy server` and the regular `server-side` script of a server from the server pool.

* [Write a Reverse Proxy Server in Python: Part 1 (Reverse Proxy Server)](https://shantoroy.com/network/write-a-reverse-proxy-server-in-python/)
* [Write a Reverse Proxy Server in Python: Part 2 (Server Pool)](https://shantoroy.com/network/write-a-reverse-proxy-in-python-part-02-servers/)

In this post, we will code our `client-side` script that will send the following packets to the reverse proxy server. Note that, the user/client does not know which server is going to process the user data. A client can only knows about the reverse proxy server and sends data to the reverse proxy thereby. More details are available in the [first post](https://shantoroy.com/network/write-a-reverse-proxy-server-in-python/).

## Communication packet
Each client sends json-alike data (stored in a file) to the reverse proxy server. Here is an example packet.

```json
{
 "type": 0, // 0 is a message from a client to a server
 "srcid": 999, // source (client) id
 "privPoliId": 999, // destination server’s privacy policy
 "payloadsize": 999, // payload size
 "payload": "xyz" // payload
}
```

## Code in Python
### Used Modules
We are going to use only the following modules (description already discussed in the previous two posts).
```python
import socket 
import hashlib
import json
import sys
```

### Available Input Arguments
We need to provide three input arguments while running the script.
* id $\rightarrow$ client ID
*  revproc $\rightarrow$ reverse proxy listening port
* pkt $\rightarrow$ packet file name (stores the packet data)
```python
def option_check():
    global args 

    # all available argument options
    avail_options = ["-id", "-revproc", "-pkt"]

    # receive user given options
    options = [opt for opt in sys.argv[1:] if opt.startswith("-")]

    # receive user given arguments
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    # raise error if user given option is wrong
    for i in options:
        if i not in avail_options:
            raise SystemExit(f"Usage: {sys.argv[0]} (-id & -revproc & -pkt) <argument>...")

    # raise error if not all options or arguments are available
    if len(options) != 3 or len(args) != 3:
        raise SystemExit(f"Usage: {sys.argv[0]} (-id & -revproc & -pkt) <argument>...")
```

### Function to read data from the files
This function is straight-forward. It just opens the file and returns the read data.
```python
def read_json(filename):
    with open(filename) as f:
        data = json.load(f)
    return data
```

### Main function
Now, we establish a socket communication with the `reverse proxy server`. Feel free to change your hostname if it is not the `localhost`. You can bind port address with IP address as well instead of names. 

First the client reads the packet file and sends read data to the `reverse proxy`. Then it waits for the reverse proxy to return processed (hashed) data.
On receiving the processed data, the client matches the hash calculation itself and be sure if the processed payload data is correct. 
```python
if __name__ == "__main__":
    option_check()
    server_name = 'localhost'
    # server_name = 'ec2-3-21-114-31.us-east-2.compute.amazonaws.com'
    server_port = int(args[1])
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_name,server_port))

    # Use while loop for continuous connection
    # while True:
    with open(args[2]) as f:
        send_msg = json.load(f)
    print("Sending message", send_msg["payload"], "to privacy policy", send_msg["privPoliId"],\
                        "through reverse proxy running on port", args[1])
    client_socket.send(json.dumps(send_msg).encode())
    recv_msg = client_socket.recv(2048).decode()
    recv_msg = json.loads(recv_msg)
    # print (">> ", recv_msg)
    hashed_sent = hashlib.sha1(send_msg["payload"].encode()).hexdigest()
    print ("Receiving a response from the server payload:", recv_msg["payload"])

    if hashed_sent == recv_msg["payload"]:
        print ("Hash of payload is correct")
    else:
        print ("Hash of payload is not correct")
```

Coding the client part is a lot easier than coding the server or the reverse proxy. The entire code is available in the [Github](https://github.com/shantoroy/reverse_proxy/blob/master/client.py).

So, now we are done with coding all three scripts. In the next post, we will write an automation script in `shell` and check whether our round-robin-based load-balancing works fine in the `reverse proxy`.


The whole tutorial series is listed here:
* [Write a Reverse Proxy Server in Python: Part 1 (Reverse Proxy Server)](https://shantoroy.com/network/write-a-reverse-proxy-server-in-python/)
* [Write a Reverse Proxy Server in Python: Part 2 (Server Pool)](https://shantoroy.com/network/write-a-reverse-proxy-in-python-part-02-servers/)
* [Write a Reverse Proxy Server in Python: Part 3 (Client-side Script)](https://shantoroy.com/network/write-a-reverse-proxy-server-client-side-script/)
* [Write a Reverse Proxy Server in Python: Part 4 (Shell Script for Automation)](https://shantoroy.com/network/write-a-reverse-proxy-in-python-automation-shell-script/)



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NTU1NTE3NTEsMTQ0MzIyODI5MSwtMT
g4Njc1NjUwLC0xOTIxMjc5MzcyLC0yMDgwODc4OTA3LC0yMTI2
NDc4MTg0LDE2ODExMTk5NjUsLTU4MDUzNTY3OV19
-->