---
layout: single
title: "How to Create a Dashboard on Grafana showing IoT Device Status"
excerpt: "Learn how to create a dashboard on Grafana that displays the status of a set of IoT devices by fetching data from PostGreSQL table. Monitor your devices in real-time and gain insights into their performance with this easy-to-follow guide."
seo_title: "How to Create a Grafana Dashboard to Monitor IoT Device Status"
seo_description: "In this blog post, we will learn how to create a dashboard on Grafana that displays the status of a set of IoT devices. Let's learn how to monitor our devices in real-time and gain insights into their performance with this easy-to-follow guide."
header:
  image: "https://live.staticflickr.com/65535/52710961314_e1d5ea744a_o.png"
  teaser: "https://live.staticflickr.com/65535/52710961314_e1d5ea744a_o.png"
categories:
  - Monitoring
tags:
  - Grafana
  - Dashboard
  - Monitoring
  - PostGreSQL
  - IoT
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
---



As IoT devices become increasingly ubiquitous, it's essential to have a way to monitor their performance in real time. In a recent project, my professor asked me to create a dashboard where we can check the status (online/offline) of the devices based on selected time.

 Grafana is an open-source data visualization platform that provides a powerful way to create real-time dashboards for monitoring various data types, including IoT device status. In my work, I will fetch the latest timestamp to check whether that falls down to selected time period from current moment.

In this guide, we will walk you through the steps of creating a dashboard on Grafana that displays the status of our IoT devices. Here, we will be able to monitor our devices in real-time and gain insights into their performance.

## Prerequisites

Here, we need to have the following:

-   Access to a Grafana instance
-   A PostgreSQL database with a table containing your IoT device data
-   Basic knowledge of SQL and Grafana

Alright! Let's get started!!!


## Connect to the PostgreSQL database

First, we need to connect Grafana to our PostgreSQL database. To do this, let's click the "Configuration" icon in the left sidebar and select "Data Sources". Then, let's click the "Add data source" button and select "PostgreSQL" from the list of available data sources.

Then let's enter the details of our PostgreSQL database, including the host, port, database name, username, and password. Once we've entered the details, let's click the "Save & Test" button to test the connection.

## Step 2: Create a device status panel

Now that we've connected Grafana to your PostgreSQL database, we can create our dashboard. The first thing we'll create is a device status panel that displays the status of our IoT devices.

1. To create a device status panel, let's first click the "Dashboard" icon in the left sidebar and select "New dashboard". 

2. Then, let's select "Stat" type visualization. 

3.  In the "Query" tab, enter the following SQL query:
	```sql
	SELECT "device_id",
	  -- CASE WHEN MAX("record_time") >= NOW() - INTERVAL '15 minutes' THEN 1 ELSE 0 END as status
	  CASE WHEN MAX("record_time") BETWEEN $__timeFrom() AND $__timeTo() THEN 1 ELSE 0 END as status
	FROM sensor
	GROUP BY "device_id"
	ORDER BY "device_id" 
	-- ORDER BY "status" DESC, "device_id" ASC
	```
	Here, we are selecting the $device_id$ column and setting a status for each based on time period selected on the time filter. Here, the `$__timeFrom()` and `$__timeTo()` variaables help us to connect the query with the Grafana filter.
	
	If you want a fixed time, say, last 15 minutes, you can use the second query I commented out. Like this: `CASE WHEN MAX("record_time") >= NOW() - INTERVAL '15 minutes' THEN 1 ELSE 0 END as status`.
	
	You can order the devices by names (what I did here), or can sort by online and offline devices (commented out line).

4. We can set a title under the `Panel Options` on the right panel. Under the `Value Options` section, let's select `status` from the `Fields` drop-down menu.
5. Under the `Value Mappings` section, let's add two values "1" and "0". The text for value 1 should be "online" and "offline" for value 0.  Let's also set the colors as we want for both. In my case, I chose "green" for online status and "red" for offline.
6. Under the `Threshold`, let's add a value 0 and choose color "red". There is a by default "Base" with green. So, we do not need to add another.
7. Under the `Standard options` section, let's select `From thresholds (by value)` from the `Color Scheme` drop-down menu.

Alright! Let's run the query and we will get something like the following. 

<figure>
  <a href="https://live.staticflickr.com/65535/52710180067_dcaeb9dfb1_o.png"><img src="https://live.staticflickr.com/65535/52710180067_dcaeb9dfb1_o.png"></a>
</figure>
<br/>


Here, I was collecting data for four devices, and selected last 24 hours to check which were online and which were offline during this period. You can choose any period from current menu and figure out the status of each device.

You can read my other post related to Grafana dashboards:
[How to Create a New Drop-Down Menu/Filter in Grafana Based on PostgreSQL Table Column](https://shantoroy.com/monitoring/add-a-drop-down-filter-in-Grafana/)

That's all for today!Cheers!!! 😎
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MTE0NTIxMjEsLTI2NjU2OTMyMl19
-->