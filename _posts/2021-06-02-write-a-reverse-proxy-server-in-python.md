---
layout: single
title: "Write a Reverse Proxy  Server in Python: Part 1 (Reverse Proxy Server)"
excerpt:  "In this tutorial, you will learn how to write a reverse proxy server in Python. Reverse proxies are used to distribute traffic across multiple servers or to hide the identity of the server. We will start by building the reverse proxy server, which will listen on a specified port and forward incoming requests to one of the backend servers."
seo_title:  "Write a Reverse Proxy Server in Python: Part 1 (Reverse Proxy Server)"
seo_description:  "Learn how to build a reverse proxy server in Python. In this tutorial, I will cover the basics of a reverse proxy and write a reverse proxy server that listens on a specified port and forwards incoming requests to one of the backend servers. Follow this step-by-step guide to create your own reverse proxy server in Python."
header:
  image: "https://live.staticflickr.com/65535/51222794636_14a21deed5_w.jpg"
  teaser: "https://live.staticflickr.com/65535/51222794636_14a21deed5_w.jpg"
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

In this tutorial we will learn, how to build a `Reverse Proxy Server` in python. I will post a series of this tutorial where we will build a complete system that includes several servers and clients alongside the Reverse Proxy server. 

After the basic script-based implementation, I will  provide details on how to implement the system in `Amazon EC2` instances. 

The series will have the following contents:
* Part 01: The Reverse Proxy Server
* Part 02: A Server in a Server Pool
* Part 03: A Client
* Part 04: Simulation with Packets
* Part 05: Deploy in Amazon EC2 instances

## Reverse Proxy
A reverse proxy server is connected to a pool of servers and forwards user requests any of the server from the pool. In a server-client architecture, a client typically used to directly connect to a server for some work to be done. But it raises some issues regarding server availability and scaling of the server-end. The `red` connection in the figure depicts the direct communication between a client and a server.

To resolve the above-mentioned issues, a reverse proxy server is used to handle all the incoming connection from the users or clients and then forward the request to any of the servers. When the server completes processing of the data, it returns the data to the client via the reverse proxy again. In the figure below, the green two-way communication is established in a. reverse proxy server-based system. 

<figure>
  <a href="https://live.staticflickr.com/65535/51224464010_60f06f2ac3_w.jpg"><img src="https://live.staticflickr.com/65535/51224464010_60f06f2ac3_w.jpg"></a>
</figure>

## Functionalities
In our Python code, we will apply the following functionalities to a Reverse Proxy Server:
* Keep a record of available servers
* Distinguish the servers based on policy
* Use `threading` to handle all processes seperately
* Handles incoming connections from the clients
* Forward the user requests to the available servers in a round-robin fashion
* Receives processed data from the servers and returns back the data to the users 

## Communication Packets
We will be using communication packets in `JSON` format. JSON is a python dictionary-alike representation of data and widely used in REST-based systems.

### Client-side Packets
```json
{
 "type": 0, // 0 is a message from a client to a server
 "srcid": 999, // source (client) id
 "privPoliId": 999, // destination server’s privacy policy
 "payloadsize": 999, // payload size
 "payload": "xyz" // payload
}
```
### Server (Server Pool)-side Connection Setup Packets
```json
{
 "type": 1 // 1 is a connection setup message from a server
 "id": 999, // id of the server
 "privPolyId": 999, // privacy policy of the server
 "listenport": 999 // port on which the server is listening
}
```

### Server (Server Pool)-side User-data Processed Packets
```json
{
 "type": 2, // 2 is an ACK from a server to a client
 "srcid": 999, // source (server) id
 "destid": 999, // destination (client) id
 "payloadsize": 999, // payload size
 "payload": "xyz" // payload
}
```

## Code in Python

### Used Modules
Here, the most important module we are going to use is `socket`, which will help us to establish socket communication between nodes. Here, let's check why we are using particular modules for what purpose

 -  **`_thread`** and **`threading`** - for implementing thread-based isolated processes for each communication. 
 -  **`json`** - handles packet data that is JSON-alike.
 - **`sys`** - handles options and arguments while running the scripts
 - **`pandas`** - keep a table-based record of available servers
 - **`itertools`** - to help the round-robin cycle
 - **`time`** - optional, you can keep track of the sessions (not included)

```python
# Import required modules
import socket
import _thread
import threading
import json
import sys
import time
import pandas as pd
import itertools
```

### Check Available Arguments
The following function checks for available options and receives each input arguments that will help us to run the servers. The only input we need is the `port` address. 

It will give user the usage message if the user does not run the script based on our need.
```python
def option_check():
    # all available argument options
    avail_options = ["-port"]

    # receive user given options
    options = [opt for opt in sys.argv[1:] if opt.startswith("-")]

    # receive user given arguments
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    # raise error if user given option is wrong
    for i in options:
        if i not in avail_options:
            raise SystemExit(f"Usage: {sys.argv[0]} -port <argument>...")

    # raise error if not all options or arguments are available
    if len(options) != 1 or len(args) != 1:
        raise SystemExit(f"Usage: {sys.argv[0]} -port <argument>...")

    return args
```

### Round Robin
Our Round-Robin implementation is too simple. We take a `Itertools.cycle()` object as an input and our function returns one output each time using the `next` function. We will infact pass a list object of `ip addresses` that have the same privacy policy.
```python
def round_robin(iterable):
    return next(iterable)
```

### A dataframe to keep records
Here, we will use a dataframe table using `pandas` to store the `type`, `id`, `privacy policy`, `listening port`, and the `ip address` of each available server.
```python
# define the available table
column_names = ["type", "id", "privPolyId", "listenport", "ip_addr"]
updated_available_server_table = pd.DataFrame(columns = column_names)
```

Here we add entry to the server record table once a message is received.
```python
def available_server(msg):
    global updated_available_server_table
    global policy_table

    updated_available_server_table = updated_available_server_table.append(msg, ignore_index = True)
    policy_list = set(updated_available_server_table["privPolyId"].tolist())
    # print(policy_list)
    
    policy_table = {}
    for policy in policy_list:
        policy_table[policy] = itertools.cycle(set(updated_available_server_table\
                [updated_available_server_table["privPolyId"]==policy]["id"].tolist()))
```

### Receive New Connection
Now, the following function will start action when our proxy server receives a new connection request (whether a server from the server pool or a user client machine). 

It first retrieves the incoming packet and check the `packet type`. If it is `0`, the incoming connection identifies a client on the opposite side. If `1`, then the connection establishing node must be a server.

Now, if the opposite node is a server, we add an entry to our table using the previously defined `available_server` function.

If the node is client, we first retrive the privacy policy of the packet, and then receive the next server from the same policy using our `round_robin` function. Then our proxy server creates a new connection to the target server, forward the user packet, and receives the processed data followed by sending the packet back to the client. You can imagine the new socket connection as a nested socket communication.
```python
# Establish connection with new client
def on_new_client(clientsocket,addr):
    while True:

        msg = clientsocket.recv(2048)
        if not msg:
            # lock released on exit
            print_lock.release()
            break
        
        json_msg = json.loads(msg.decode())

        if json_msg["type"] == "1":
            ip, port = clientsocket.getpeername()
            print ("Received Connection from IP:", ip, "Port:", port)
            json_msg["ip_addr"] = ip
            print ("Received setup message from server id", json_msg["id"], "privacy policy",\
                                json_msg["privPolyId"], "port", json_msg["listenport"])
            available_server(json_msg)


        elif json_msg["type"] == "0":
            print ('Received a message from client', json_msg["srcid"], \
                                            "payload", json_msg["payload"])
            policy = json_msg["privPoliId"]
            # print(policy)
            target_host_id = round_robin(policy_table[policy])
            # print(target_host_id)
            server_name = updated_available_server_table.loc\
                            [updated_available_server_table["id"]==target_host_id, "ip_addr"].values[0]
            server_port = int(updated_available_server_table.loc\
                            [updated_available_server_table["id"]==target_host_id, "listenport"].values[0])

            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((server_name,server_port))

            print("Forwarding a data message to server id", target_host_id, "server ip", server_name, \
                                                "port", server_port, "payload", json_msg["payload"])
            server_socket.send(json.dumps(json_msg).encode())
            recv_msg = server_socket.recv(2048)
            recv_json_msg = json.loads(recv_msg.decode())
            print ("Received a data message from server id", recv_json_msg["srcid"],\
                                                 "payload", recv_json_msg["payload"])
            print("")
            server_socket.close()

            clientsocket.send(json.dumps(recv_json_msg).encode())

        else:
            pass

    clientsocket.close()
```

### Main Program
Now, let's create our main program where we follow the mandatory socket communication steps (binding host and port, listening for clients, etc.). Here, we start thread for each new socket communication.
```python
if __name__ == "__main__":
    args = option_check()
    s = socket.socket()         # Create a socket object
    # host = socket.gethostname() # Get local machine name
    host = 'localhost'
    port = int(args[0])              # Reserve a port for your service.
    print("Running the reverse proxy on port", port)

    # Binds to the port
    s.bind((host, port))     
    # Allow 10 clients to connect
    s.listen(100) 

    while True:
        c, addr = s.accept()     # Establish connection with client.
        # lock acquired by client
        print_lock.acquire()
        _thread.start_new_thread(on_new_client,(c,addr))
        
    s.close()
```

The entire code is available in [GitHub](https://github.com/shantoroy/reverse_proxy/blob/master/reverse_proxy.py). It was a homework in my network course taken in the last semester; if you want to through details of the problem, just go through this [document](https://github.com/shantoroy/reverse_proxy/blob/master/Reverse_Proxy_HW.pdf).

As this is a series tutorial, I will post the subsequent blog-posts soon. Stay tuned.

If you find this post helpful, and want to support this blog, you can
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="shantoroy" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script> or

<div style="width: 300px; height: 200px;">
<form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="business" value="Q9F45GULUSYMY" />
<input type="hidden" name="no_recurring" value="0" />
<input type="hidden" name="item_name" value="I appreciate your support! 😊" />
<input type="hidden" name="currency_code" value="USD" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
</form></div>


The whole tutorial series is listed here:
* [Write a Reverse Proxy Server in Python: Part 1 (Reverse Proxy Server)](https://shantoroy.com/network/write-a-reverse-proxy-server-in-python/)
* [Write a Reverse Proxy Server in Python: Part 2 (Server Pool)](https://shantoroy.com/network/write-a-reverse-proxy-in-python-part-02-servers/)
* [Write a Reverse Proxy Server in Python: Part 3 (Client-side Script)](https://shantoroy.com/network/write-a-reverse-proxy-server-client-side-script/)
* [Write a Reverse Proxy Server in Python: Part 4 (Shell Script for Automation)](https://shantoroy.com/network/write-a-reverse-proxy-in-python-automation-shell-script/)


---
## Promotions and Referrals (US Residents Only)
* **Chime:** Open a Checking account at Chime using [my referral link](https://chime.com/r/shantoroy) and get $100 after your employer deposit paycheck of minimum $200 within the first 45 days. 
* **Rakuten:** Get $30 after you spend $30 at Rakuten select stores after you use [my referral link](www.rakuten.com/r/STONEH425?eeid=44971) to open an account. 
* **Chase Freedom Credit Card:** Earn $200 cash back with Chase Freedom Unlimited or Chase Freedom Flex credit card. I can be rewarded if you apply using [my referral link](https://www.referyourchasecard.com/18o/E7MB03IG12) and are approved for the card.

* **Chase Checking Account:** Get $200 when you open a checking account using [my referral link](https://accounts.chase.com/raf/share/2564396166) after your first salary is deposited. 
* **Discover:** Earn $50 cash back with Discover when you apply using [my referral link](https://refer.discover.com/s/SHANTO10) and are approved for the card.
* **Amex Blue Cash Preferred:** Earn $250 as statement credit when you spend $3000 in first six months. Apply using [my referral link](https://americanexpress.com/en-us/referral/SHANTRzUOO?XL=MIANS).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU2NDA5OTE3NSwxNjQ0Nzk3MDE3LDYxMj
U1ODkwOCwxOTIyMTkyMDk5LDExNjEwMjgyODgsLTEyOTQxMjY3
NDMsLTE1MTUyMjc5MjUsLTEwODY0MzgxNiw2MzE4Mjk0MTNdfQ
==
-->