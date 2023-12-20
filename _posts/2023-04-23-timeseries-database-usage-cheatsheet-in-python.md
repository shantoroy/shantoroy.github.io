---
layout: single
title: "Timeseries Database Usage Cheatsheet and Templates in Python: InfluxDB, PostgreSQL, and Prometheus"
excerpt: "If you're working with data that changes over time, you need a timeseries database to store that information effectively. In this guide, I'll provide you with a comprehensive timeseries database usage cheatsheet and templates in Python for InfluxDB, PostgreSQL, and Prometheus. I'll show you how to collect and store timeseries data efficiently, and I'll provide you with examples and templates that you can use to get started right away."
seo_title: "Timeseries Database Usage Cheatsheet and Templates in Python: InfluxDB, PostgreSQL, and Prometheus"
seo_description: "Looking for a comprehensive timeseries database usage cheatsheet and templates in Python? Check out this post that includes templates for InfluxDB, PostgreSQL, and Prometheus. Learn how to collect and store timeseries data efficiently and effectively for your timeseries data-based applications."
header:
  image: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
  teaser: "https://live.staticflickr.com/65535/53398371763_5fc8772ed9_o.png"
categories:
  - Python
tags:
  - python
  - timeseries
  - prometheus
  - influxdb
  - postgresql
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Hi there!!! 👋

I have been working on some timeseries data for some time now and wanted to explore more on different timeseries databases out there. 

So, there are a number of timeseries databases including [influxdb](https://www.influxdata.com/), [TimeScale](https://www.timescale.com/products), [Prometheus](https://prometheus.io/), [QuestDB](https://questdb.io/docs/get-started/docker/), [DataStax](https://www.datastax.com/products/datastax-enterprise), [Amazon timestream](https://aws.amazon.com/timestream/), [dataPARC](https://www.dataparc.com/parcview/), etc.

A lot of other timeseries databases use and optimize postgreSQL in the background. Therefore, I decided to keep a simple template records of three most popular ones ones: influxDB, postgreSQL, and Prometheus.

So, what I will do is post templates for doing similar tasks: connection databases, and then storing a few fields including one column for the timestamp. 

## InfluxDB
Here's an example code for parsing 4/5 fields (including a timestamp) from JSON and storing the fields in InfluxDB in Python using the `influxdb-client` library:

```py
from influxdb_client import InfluxDBClient
import json

# Load JSON data
data = '{"timestamp": "2022-01-01T00:00:00Z", "field1": 10, "field2": "value2", "field3": 3.14, "field4": true}'

# Parse JSON data
parsed_data = json.loads(data)

# Connect to InfluxDB
client = InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org")
write_api = client.write_api()

# Create InfluxDB point
point = {}
point["measurement"] = "my-measurement"
point["tags"] = {"tag1": "value1", "tag2": "value2"}
point["fields"] = {"field1": parsed_data["field1"], "field2": parsed_data["field2"], "field3": parsed_data["field3"], "field4": parsed_data["field4"]}
point["time"] = parsed_data["timestamp"]

# Write data to InfluxDB
write_api.write(bucket="my-bucket", record=point)

# Close connection to InfluxDB
client.close()
```

This code assumes that you have already installed the `influxdb-client` library and have an InfluxDB instance running locally on port 8086 with a token and organization configured. It also assumes that the JSON data contains a timestamp field called "timestamp" and four other fields called "field1", "field2", "field3", and "field4".

## PostgreSQL
Here's an example code for parsing 4/5 fields (including a timestamp) from JSON and storing the fields in PostgreSQL using Python:
```py
import psycopg2
import json
from datetime import datetime

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_username",
    password="your_password"
)

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Load the JSON data
with open('data.json') as f:
    data = json.load(f)

# Parse the fields from the JSON data and store them in PostgreSQL
for item in data:
    timestamp = datetime.strptime(item['timestamp'], '%Y-%m-%d %H:%M:%S')
    field1 = item['field1']
    field2 = item['field2']
    field3 = item['field3']
    field4 = item['field4']

    # Execute an SQL INSERT statement to store the parsed fields in PostgreSQL
    cur.execute(
        "INSERT INTO your_table (timestamp, field1, field2, field3, field4) VALUES (%s, %s, %s, %s, %s)",
        (timestamp, field1, field2, field3, field4)
    )

# Commit the changes and close the connection
conn.commit()
conn.close()
```

Note that you'll need to replace `your_host`, `your_database`, `your_username`, `your_password`, `your_table`, and `data.json` with the appropriate values for your setup.


## Prometheus
Here's an example code for parsing 4/5 fields (including a timestamp) from JSON and storing the fields in Prometheus using Python:
```py
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import json
import time

# Load JSON data from file
with open('data.json', 'r') as file:
    data = json.load(file)

# Create Prometheus registry and metric
registry = CollectorRegistry()
gauge = Gauge('metric_name', 'metric_help', ['field1', 'field2', 'field3', 'timestamp'], registry=registry)

# Parse data and push to Prometheus
for item in data:
    field1 = item['field1']
    field2 = item['field2']
    field3 = item['field3']
    timestamp = int(time.mktime(time.strptime(item['timestamp'], '%Y-%m-%d %H:%M:%S')))
    gauge.labels(field1=field1, field2=field2, field3=field3, timestamp=timestamp).set(item['value'])

# Push metrics to Prometheus server
push_to_gateway('localhost:9091', job='job_name', registry=registry)
```

Note that this code assumes that you have a Prometheus server running on `localhost:9091` and that you have defined a job named `job_name` in your Prometheus configuration file. 


---

---

So, that's all for today! cheers!!!

___

___

Thank you for reading my blog post! 🙏

If you enjoyed it and would like to stay updated on my latest content and plans for next week, be sure to subscribe to my newsletter on Substack. 👇

Once a week, I'll be sharing the latest weekly updates on my published articles, along with other news, content and resources. Enter your email below to subscribe and join the conversation for Free! ✍️

<iframe src="https://shantoroy.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

I am also writing on Medium. You can [follow me here](https://medium.com/@shantoroy).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU0NTM0NzA1MiwtMTgxNjQxMzU0NF19
-->