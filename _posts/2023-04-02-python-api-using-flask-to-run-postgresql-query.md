---
layout: single
title: "How to Write a RESTful API using Python Flask to fetch data from PostgreSQL Database"
excerpt: "Learn how to build a RESTful API in Python using Flask and PostgreSQL. In this tutorial, you'll learn how to connect Flask to a PostgreSQL database and create API endpoints to fetch data. By the end of this post, you'll have a fully functional API that can be used to query your PostgreSQL database."
seo_title: "How to Write a Python API using Flask and PostgreSQL"
seo_description: "Learn how to build a RESTful API in Python using Flask and PostgreSQL. In this tutorial, you'll learn how to connect Flask to a PostgreSQL database and create API endpoints to fetch data."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - API
  - Flask
  - REST
  - json
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

First of all, writing an API that allows to execute SQL queries is not recommended. 

Why!?! Because, using this method an attacker can run malicious SQL queries and can retrieve sensitive information or execute something else.

However, this is a simple tutorial on how to write a python API that allows executing an SQL query. You can use this type of APIs for learning how to fetch data from database for local application usage or create more endpoints with executing different direct queries.

## Create a Read-Only user on PostgreSQL
Even though we have said, it is not a recommended way to make an API execute queries. However, we can minimize the issue by creating a new user that has read-only permission.

We will use this user in our API to make our database safe. We will give only to execute `select` operations.

To create a new user in PostgreSQL with read-only permission to a particular database, follow these steps:

1.  Connect to the PostgreSQL server as a superuser.
    
    rubyCopy code
    
    ```bash
    $ sudo -u postgres psql
    ``` 
    
2.  Create a new user with a username and password.
    
    ```sql
    CREATE USER <username> WITH PASSWORD '<password>';
    ``` 
    
3.  Grant read-only permission to the user for the particular database.

    ```sql
    GRANT CONNECT ON DATABASE <database_name> TO <username>;
    GRANT USAGE ON SCHEMA public TO <username>;
    GRANT SELECT ON ALL TABLES IN SCHEMA public TO <username>;
    ``` 
    
    Here, replace `<username>` with the desired username, `<password>` with the desired password, and `<database_name>` with the name of the particular database.

## Create the API
Now, it's time to write the API. 
### Install Requirements
```bash
$ pip install flask
$ pip install requests
```


### API Code using `flask`
The code is self-descriptive. Just change the database-oriented information.
```python
# filename: query_api.py
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Change the following values to match yours
db_name = "your_db_name"
db_user = "your_db_user"
db_password = "your_db_password"
db_host = "your_db_host"
db_port = "your_db_port"

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(database=db_name, user=db_user, password=db_password,
                        host=db_host, port=db_port)
cur = conn.cursor()

# Define a route that accepts POST requests to run SQL queries
@app.route("/query", methods=["POST"])
def query():
    query_text = request.json.get("query")
    cur.execute(query_text)
    result = cur.fetchall()

    # Return the result as JSON
    return jsonify(result)

# Run the Flask app on port 7000
if __name__ == "__main__":
    app.run(port=7000)
```

## Client Code
At the client side, you can use the following code and modify the SQL query as you want.
```python
import requests

url = "http://localhost:7000/query"
query = "SELECT * FROM <table_name> WHERE <some_column>='<some_value>' limit 10"

response = requests.post(url, json={"query": query})
print(response.json())
```

## Concluding Remarks
This post is for learning how to write a basic API that can fetch data from a postgresql database.

The recommended way is to execute predetermined queries within the API code and not allow external users to run queries. You can use individual queries for individual endpoints, which is recommended.

However, I wanted to make the code short, let you know the security concerns associated with it, and why you should execute queries defined within the app. 
 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ0NzMwMDIzOV19
-->