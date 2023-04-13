---
layout: single
title: "How to Create a Grafana Dashboard to Present individual Device Analysis using Individual Panels"
excerpt: "Learn how to create a powerful Grafana dashboard to present your device analysis with individual panels. In this tutorial, we will guide you step-by-step on how to create a dashboard with dynamic visualization using Grafana's advanced features. By the end of this post, you'll be able to create a customized dashboard that presents your device analysis in an easy-to-understand format."
seo_title: "Create a Powerful Grafana Dashboard for Device Analysis Using Individual Panels"
seo_description: "In this tutorial, you will learn how to create a dynamic Grafana dashboard with individual panels to present your device analysis. Our step-by-step guide will show you how to utilize Grafana's advanced features and customization options to create a powerful dashboard that will make your data easy to understand and visually appealing. By the end of this post, you'll have the knowledge to create a customized dashboard that will showcase your device analysis in the most effective way."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - Monitoring
tags:
  - Grafana
  - Dashboard
  - Monitoring
  - PostgreSQL
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Earlier in this [post](https://shantoroy.com/monitoring/add-a-drop-down-filter-in-Grafana/), we have seen how to select a device and see analysis in a dashboard panel.

[How to Create a New Drop-Down Menu/Filter (Query Variable) in Grafana Based on PostgreSQL Table Column](https://shantoroy.com/monitoring/add-a-drop-down-filter-in-Grafana/)

## Issue
Now, how about we want to show individual panel for each device in the same dashboard? 

One way of doing it is manually creating panels and select device ID to show analysis in corresponding panel. But, how about having 500 devices? 

It is waste of time to create 500 panels for 500 devices. Rather, we will create one panel and repeat it for selected devices.

## Create a new Query Variable
the solution is create a new query variable. We can do the following to create a query variable. 
1.  Create a query variable you created.
2.  In the "Query Options" section, set the "Query" field to `SELECT DISTINCT(<device_id>) FROM <table_name> ORDER BY <device_id> ASC`.
3.  In the "General" section, set the "Name" field to something descriptive like "Device".
4.  In the "Options" section, set the "Multi-value" option to "On".
5.  In the "Options" section, set the "Include All option" option to "On".
6.  In the "Options" section, set the "All format" field to `$__all`.
7.  Save the variable.
    
8.  Edit the query you want to use to show sensor data. Replace the hard-coded device ID with the variable name in your WHERE clause. For example, replace `"device_id" = 'your_device_id'` with `"device_id" IN($device)`.

## Enable Repeat Option
We can enable repeating options from the panel edit view. Let's do the following:

1.  Click on the Panel Title to open the Edit Panel view.
    
2.  In the Panel Edit view, click on the Repeat tab.
    
3.  Under the Repeat tab, set the following values:
    
    -   Variable name: `device`
    -   Label: `Device`
    -   Max values: set the maximum number of panels you want to display

4. Save the panel and go back to the dashboard view. You should see the drop-down manu. From there, select all devices or select the ones you want to check. New panels will show up as you select more devices.

So, that's all for today! Cheers!!!


## Related Posts
1. [How to Create a Dashboard on Grafana showing IoT Device Status](https://shantoroy.com/monitoring/create-IoT-devices-status-dashboard-on-garfana-based-on-postgresql/)
2. [How to Create a New Drop-Down Menu/Filter (Query Variable) in Grafana Based on PostgreSQL Table Column](https://shantoroy.com/monitoring/add-a-drop-down-filter-in-Grafana/)
3. [How to Select Multiple Options from Drop-Down Menu/Filter (Query Variable) in Grafana Based on PostgreSQL Table Column](https://shantoroy.com/monitoring/grafana-dashboard-select-multiple-IoT-device/)


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAyNjU2ODY5MywtMTc3NjcwODcwOF19
-->