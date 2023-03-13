---
layout: single
title: "How to Select Multiple Options from Drop-Down Menu/Filter (Query Variable) in Grafana Based on PostgreSQL Table Column"
excerpt:  "In this tutorial, I will show you how to select multiple options from a drop-down menu/filter (Query Variable) in Grafana based on a PostgreSQL table column. This feature is helpful when we want to filter the data based on more than one condition, and it is particularly useful when we have a large dataset."
seo_title:  "How to Select Multiple Options from Drop-Down Menu/Filter (Query Variable) in Grafana Based on PostgreSQL Table Column"
seo_description:  "Learn how to filter data in Grafana based on multiple conditions using a drop-down menu/filter (Query Variable). This tutorial covers the steps to create a PostgreSQL table column filter in Grafana, making it easier to analyze large datasets."
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
---
Grafana is a popular open-source data visualization and analytics platform that enables creating dashboards and monitoring metrics from various data sources, for example, a database.

One of the useful features of Grafana is the ability to create drop-down panels that enable selecting specific values to filter data in other panels on the dashboard.

Earlier, in this [post](https://shantoroy.com/monitoring/add-a-drop-down-filter-in-Grafana/), I have shown how to create a drop-down menu to select stat for a  particular device for my IoT project where I have over 200 devices constantly sending data to to the broker. 

[How to Create a New Drop-Down Menu/Filter in Grafana Based on PostgreSQL Table Column](https://shantoroy.com/monitoring/add-a-drop-down-filter-in-Grafana/)

However, the only issue was I could check sensor data visualization for only one device. Now, how about checking status for a group or cluster of devices!?

Let's say five devices have similar properties, and we want to check stats at the same time. So, now, we need to have the option to select multiple devices from the drop-down menu.

It's all the same procedure as mentioned in my previous post. Except for, we need to select the option for `allowing multiple selections` when creating a Query variable.

And then use something like `<column_name> in ($<variable_name>)`. In the folowing example, it's `"device_id" IN ($Devices)`.
```sql
SELECT $__timeGroup(record_time, '24h') as time,col1,col2,col3,col4
FROM sensor 
WHERE $__timeFilter(record_time) AND 
  "record_time" > (date_trunc('day', CURRENT_DATE - INTERVAL '15 day')) AND
  "record_time" < (date_trunc('day', now())) AND "device_id" IN ($Devices) 
GROUP BY time,col1,col2,col3,col4
ORDER BY time
```

Grafana is a powerful data visualization and analytics tool that allows us to create custom dashboards and monitor metrics from various data sources.

In this tutorial, we have worked on selecting multiple options from the drop-down menu/filter. Grafana is a pretty cool tool for monitoring and instant data analysis or visualization. 

More tutorials to come in the future! Until then, cheers!!! 😎
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgyMzczMTc0M119
-->