---
layout: single
title: "How to Create a New Drop-Down Menu/Filter (Query Variable) in Grafana Based on PostgreSQL Table Column"
header:
  image: "https://live.staticflickr.com/65535/52695891576_98e68b805e_o.png"
  teaser: "https://live.staticflickr.com/65535/52695891576_98e68b805e_o.png"
categories:
  - Monitoring
tags:
  - Grafana
  - Dashboard
  - Monitoring
  - PostgreSQL
toc: false
toc_label: "Table of Contents"
toc_icon: "heart"
excerpt: "I have been managing the backend of an IoT project to handle data and show statuses via Grafana dashboard. In this tutorial, I write a step-by-step tutorial on how to create a new drop-down menu/filter (Query Variable) so that I can select a device and show stas of that one only. My comprehensive tutorial explains how to use PostgreSQL table columns to create grafana filters that will transform the way we visualize and analyze our data."
---


Grafana is a popular open-source data visualization and analytics platform that enables creating dashboards and monitoring metrics from various data sources, for example, a database. 

One of the useful features of Grafana is the ability to create drop-down panels that enable selecting specific values to filter data in other panels on the dashboard.

If there is a timestamp column on a database table and we are choosing the `time series` metrics, by default, we get a drop-down filter of selecting data for the last few minutes to months.

In this tutorial, we will see how to create a drop-down panel in Grafana that offers the unique IDs of a column in a PostgreSQL table and use the selected ID to show graphs based on SQL queries.

## Initials
* Grafana installed on your machine (usually, port:3000).
* A PostgreSQL database with a table that has a column with distinct IDs (in my example, there was a column containing unique device IDs, I wanted to pull data based on selected device ID from the drop-down menu)
* A data source in Grafana that connects to your PostgreSQL database


## Procedure
### Step 1: Create a Query Variable
The first step is to create a query variable in Grafana that retrieves the unique device IDs from your PostgreSQL table. Here's how:
1. Open your Grafana dashboard and click on the "Variables" icon in the top navigation bar.
2. Click on the "New" button to create a new variable.
3. Choose "Query" as the type of variable.
4. In the "Data Source" field, select the data source you have configured for your PostgreSQL database.
5. In the "Query" field, enter the following SQL query to retrieve the unique device IDs:
`SELECT DISTINCT "device_id" FROM mytable`
6. Replace "mytable" with the name of your PostgreSQL table and "device_id" with the column name containing the unique device IDs.
7. In the "Refresh" section, select "On Time Range Change" to ensure that the options in the drop-down are updated whenever the time range changes.
8. Click the "Save & Test" button to save the variable and test the query.

Now, we should see a list of unique device IDs returned by the query. If the query returns the expected results, let's click the "Back" button to return to the dashboard.

### Step 2: Add a Drop-Down Panel
The next step is to add a drop-down panel to your dashboard that displays the list of unique device IDs. Here's how:
1. Click on the "Add Panel" button on the dashboard and select "Singlestat".
2. In the "Singlestat" panel, go to the "Options" tab and scroll down to the "Value" section.
3. In the "Value" section, select the "Variable" option and choose the query variable you created earlier.
4. The drop-down panel is now added to your dashboard, and it will show the selected device ID.


### Step 3: Modify SQL Queries for Graph Panels
The final step is to modify the SQL queries in the other panels on the dashboard to include a filter based on the selected device ID. 
1. Go to the panel you want to modify and click on the "Edit" button in the top right corner.
2. In the "Metrics" section, modify the SQL query to include a filter based on the selected device ID. You can use the following syntax to include the filter:
`WHERE "device_id" = '$device_id'`
We need to replace "$device_id" with the name of the query variable that you created.
3. Click on the "Apply" button to save the changes.
4. Repeat these steps for all the graph panels that display data based on the selected device ID. 

Now, whenever we choose a device from the drop-down panel, the other panels on the dashboard will update to display data for that device.

That's it! Now, we have created a drop-down panel in Grafana that shows the unique IDs of a column in a PostgreSQL table and uses the selected ID to show graphs based on SQL queries.

### Concluding Remarks
Grafana is a powerful data visualization and analytics tool that allows us to create custom dashboards and monitor metrics from various data sources. 

In this tutorial, we have seen how to create a drop-down panel in Grafana that offers the unique IDs of a column in a PostgreSQL table and uses the selected ID to deliver graphs based on SQL queries. This type of filter help when we have a lot of data points. 

That's all for today! Cheers!!! 😎
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MDA0MTQ1OTgsLTk3MDk5MTcwNiwxNz
A0MjkwNjgxXX0=
-->