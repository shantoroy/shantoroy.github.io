---
layout: single
title: "Write a Reverse Proxy  Server in Python: Part 4 (Shell Script for Automation)"
header:
  image: "https://live.staticflickr.com/65535/51236536118_0418e6819c_w.jpg"
  teaser: "https://live.staticflickr.com/65535/51236536118_0418e6819c_w.jpg"
categories:
  - network
tags:
  - Python
  - Tutorial
  - Reverse Proxy
  - Computer Nework
  - Socket Programming
  - Shell Programming
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

In the previous posts, we have coded our Reverse Proxy server, server-side code for the servers in the server pool, and our  client-side script.

* [Write a Reverse Proxy Server in Python: Part 1 (Reverse Proxy Server)](https://shantoroy.com/network/write-a-reverse-proxy-server-in-python/)
* [Write a Reverse Proxy Server in Python: Part 2 (Server Pool)](https://shantoroy.com/network/write-a-reverse-proxy-in-python-part-02-servers/)
* [Write a Reverse Proxy Server in Python: Part 3 (Client-side Script)](https://shantoroy.com/network/write-a-reverse-proxy-server-client-side-script/)

In this post we will write an automation script and then check the output to find out if our reverse proxy works fine.

## Running Scripts with arguments
This is an example of how we are going to run all the scripts
### Reverse Proxy Server
 ```sh
$ python reverse_proxy.py -port 8000
```

### Server
```sh
python server.py -id 100 -pp 111 -listen 5000 -revproc 8000
```

### Client
```sh
python client.py -id 1 -revproc 8000 -pkt pktfiles/1.json
```

## Automation Script
Let's put all the script in a directory named `reverse_proxy` and keep the directory in the `user home directory`. Now, to create a reverse proxy server we run the script with input arguments for once. We will also create four servers in a server pool and six clients in total. Let's create a file, copy the codes provided below, and then run the shell program in terminal.

Note: Do not forget to add `execute` permission to your script.
```sh
$ nano main.sh
$ chmod +x main.sh
```
or
```sh
$ nano main.sh
$ chmod 777 main.sh
```

Basically what we are going to achieve is launch new terminal window for each server and client, and then check the output.

### macOS terminal
The entire code is available in [GitHub](https://github.com/shantoroy/reverse_proxy/blob/master/main.sh).
```sh
#!/bin/bash

osascript -e 'tell app "Terminal"
    do script "cd ~/reverse_proxy && python reverse_proxy.py -port 2100"
end tell'

sleep 2

osascript -e 'tell app "Terminal"
    do script "cd ~/reverse_proxy && python server.py -id 100 -pp 111 -listen 2105 -revproc 2100"
end tell'

osascript -e 'tell app "Terminal"
    do script "cd ~/reverse_proxy && python server.py -id 200 -pp 222 -listen 2110 -revproc 2100"
end tell'

osascript -e 'tell app "Terminal"
    do script "cd ~/reverse_proxy && python server.py -id 300 -pp 111 -listen 2115 -revproc 2100"
end tell'

osascript -e 'tell app "Terminal"
    do script "cd ~/reverse_proxy && python server.py -id 400 -pp 222 -listen 2120 -revproc 2100"
end tell'

sleep 2

osascript -e 'tell app "Terminal"
    do script "cd ~/reverse_proxy && python client.py -id 1 -revproc 2100 -pkt pktfiles/1.json"
end tell'

osascript -e 'tell app "Terminal"
    do script "cd ~/reverse_proxy && python client.py -id 2 -revproc 2100 -pkt pktfiles/2.json"
end tell'

osascript -e 'tell app "Terminal"
    do script "cd ~/reverse_proxy && python client.py -id 3 -revproc 2100 -pkt pktfiles/3.json"
end tell'

osascript -e 'tell app "Terminal"
    do script "cd ~/reverse_proxy && python client.py -id 4 -revproc 2100 -pkt pktfiles/4.json"
end tell'

osascript -e 'tell app "Terminal"
    do script "cd ~/reverse_proxy && python client.py -id 5 -revproc 2100 -pkt pktfiles/5.json"
end tell'

osascript -e 'tell app "Terminal"
    do script "cd ~/reverse_proxy && python client.py -id 6 -revproc 2100 -pkt pktfiles/6.json"
end tell'
```

### Linux Terminal
I have not checked the Linux one, but it should work fine. The entire code is available in [GitHub](https://github.com/shantoroy/reverse_proxy/blob/master/main_linux.sh).
```sh
#!/bin/bash

gnome-terminal -- /bin/bash -c "cd ~/reverse_proxy; python reverse_proxy.py -port 2200; bash"

sleep 2

gnome-terminal -- /bin/bash -c "cd ~/reverse_proxy; python server.py -id 100 -pp 111 -listen 2105 -revproc 2200; bash"
gnome-terminal -- /bin/bash -c "cd ~/reverse_proxy; python server.py -id 200 -pp 222 -listen 2110 -revproc 2200; bash"
gnome-terminal -- /bin/bash -c "cd ~/reverse_proxy; python server.py -id 300 -pp 111 -listen 2115 -revproc 2200; bash"
gnome-terminal -- /bin/bash -c "cd ~/reverse_proxy; python server.py -id 400 -pp 222 -listen 2120 -revproc 2200; bash"

sleep 2

gnome-terminal -- /bin/bash -c "cd ~/reverse_proxy; python client.py -id 1 -revproc 2200 -pkt pktfiles/1.json; bash"
gnome-terminal -- /bin/bash -c "cd ~/reverse_proxy; python client.py -id 2 -revproc 2200 -pkt pktfiles/2.json; bash"
gnome-terminal -- /bin/bash -c "cd ~/reverse_proxy; python client.py -id 3 -revproc 2200 -pkt pktfiles/3.json; bash"
gnome-terminal -- /bin/bash -c "cd ~/reverse_proxy; python client.py -id 4 -revproc 2200 -pkt pktfiles/4.json; bash"
gnome-terminal -- /bin/bash -c "cd ~/reverse_proxy; python client.py -id 5 -revproc 2200 -pkt pktfiles/5.json; bash"
gnome-terminal -- /bin/bash -c "cd ~/reverse_proxy; python client.py -id 6 -revproc 2200 -pkt pktfiles/6.json; bash"
```

## Output
### Reverse Proxy Server
<figure>
  <a href="https://github.com/shantoroy/reverse_proxy/blob/master/screenshots/rev_proxy.png?raw=true"><img src="https://github.com/shantoroy/reverse_proxy/blob/master/screenshots/rev_proxy.png?raw=true"></a>
</figure>

### Any Server

<figure>
  <a href="https://github.com/shantoroy/reverse_proxy/blob/master/screenshots/server.png?raw=true"><img src="https://github.com/shantoroy/reverse_proxy/blob/master/screenshots/server.png?raw=true"></a>
</figure>

### Any Client

<figure>
  <a href="https://github.com/shantoroy/reverse_proxy/blob/master/screenshots/client.png?raw=true"><img src="https://github.com/shantoroy/reverse_proxy/blob/master/screenshots/client.png?raw=true"></a>
</figure>

### Example Video
<figure>
  <a href="https://github.com/shantoroy/reverse_proxy/blob/master/screenshots/reverse_proxy.gif?raw=true"><img src="https://github.com/shantoroy/reverse_proxy/blob/master/screenshots/reverse_proxy.gif?raw=true" width="700" height="350"></a>
</figure>

That's it for today. In the later tutorials, we will see how to implement the system in Amazon Web Service (AWS EC2).

The whole tutorial series is listed here:
* [Write a Reverse Proxy Server in Python: Part 1 (Reverse Proxy Server)](https://shantoroy.com/network/write-a-reverse-proxy-server-in-python/)
* [Write a Reverse Proxy Server in Python: Part 2 (Server Pool)](https://shantoroy.com/network/write-a-reverse-proxy-in-python-part-02-servers/)
* [Write a Reverse Proxy Server in Python: Part 3 (Client-side Script)](https://shantoroy.com/network/write-a-reverse-proxy-server-client-side-script/)
* [Write a Reverse Proxy Server in Python: Part 4 (Shell Script for Automation)](https://shantoroy.com/network/write-a-reverse-proxy-in-python-automation-shell-script/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0OTU0NTQzOTgsNTQwMjM5MTE3LDY2MD
IwMzA2NCwtMjAzNDAwMTEzMSwtMTg1MDAxNzY5NCwxNjA2NjI1
Mjc5XX0=
-->