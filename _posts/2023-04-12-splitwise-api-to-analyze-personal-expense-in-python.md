---
layout: single
title: "Splitwise API for Personal Expenditure Analytics in Python"
excerpt: "Do you want a quick and easy way to extract, analyze, and visualize your expenditure data from Splitwise?  Splitwise has an API that allows you to extract your expenditure data and use it to gain valuable insights into your spending habits. In this blog post, I'll walk you through how to use the Splitwise API in Python to access your expense data and perform data analysis to gain a better understanding of your personal finances."
seo_title: "How to Use the Splitwise API for Personal Expenditure Analytics in Python"
seo_description: "Learn how to use the Splitwise API in Python to extract, analyze, and visualize your personal expenditure data. Get a detailed walkthrough on integrating the API with Python and accessing your expense data to gain insights into your spending habits."
header:
  image: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
  teaser: "https://live.staticflickr.com/65535/52766618900_226fb0f322_o.png"
categories:
  - python
tags:
  - python
  - splitwise
  - api
  - analytics
  - data
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---
Are you looking to gain a better understanding of your personal expenses and track your spending habits? 

Well, if you are using the Splitwise app for expense management within groups, you will find this post helpful. 

In this blog post, I'll walk through how to use the Splitwise API to analyze personal expenses and create useful visualizations using Python. I'll cover everything from setting up the API credentials to generating informative graphs that can help you better understand your spending patterns. 

Alright! Let's get started...

## Personal Data Analytics Class
### Importing Modules
The following code starts with importing necessary modules for the project. The first two lines import the `splitwise` module and `Splitwise` class from it.

The `splitwise` module provides a Python wrapper for the Splitwise API, which allows users to interact with the Splitwise platform programmatically.

Next, the code imports `matplotlib` library and its `pyplot` module as `plt`. This is a popular data visualization library in Python, used to create interactive and informative graphs and charts.

The next lines import various date-related modules from `matplotlib` and `datetime` libraries, which are used to manipulate dates and times for plotting purposes.

Lastly, the code imports the `pandas` library as `pd`, which is a powerful and flexible data analysis and manipulation tool. It provides easy-to-use data structures and data analysis tools for handling and analyzing data efficiently.
```py
# import modules
import splitwise
from splitwise import Splitwise
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
import datetime
from datetime import date, datetime, timedelta
import pandas as pd
```

### Initialize the Class
The given code defines a class called `ExpenseTracker` with a constructor method `__init__`.

`__init__` method takes in three parameters `CONSUMER_KEY`, `CONSUMER_SECRET`, and `API_KEY`. These parameters are used to authenticate the API of the Splitwise application.

Inside the constructor method, `self.sw` object is initialized by calling `Splitwise` constructor. The three parameters `CONSUMER_KEY`, `CONSUMER_SECRET`, and `API_KEY` are passed to `Splitwise` constructor to create an instance of Splitwise API.

```py
class ExpenseTracker:
    
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, API_KEY):
        self.sw = Splitwise(CONSUMER_KEY, CONSUMER_SECRET, api_key=API_KEY)
        self.expenses = []
```

### Fetch expense Data
This is a method called `get_expenses` which is used to retrieve expenses from the Splitwise API. The method takes an optional argument `target_days` which specifies the number of days to retrieve expenses for (default is 365 days).

The method starts by initializing some variables such as the current page number and the page size. It also sets the start and end dates based on the `target_days` parameter.

The method then enters a loop that retrieves expenses from the API using the `getExpenses` method from the `splitwise` module. It passes the `dated_after` and `dated_before` parameters to specify the date range, `limit` parameter to specify the number of expenses to retrieve in a single request, and `offset` parameter to specify the starting point of the expenses to retrieve.
```py
    def get_expenses(self, target_days=365):
        current_page_num = 0
        page_size = 100
        end_date = date.today()
        start_date = end_date - timedelta(days=target_days)
        
        while True:
            curr_page_expenses = self.sw.getExpenses(
            dated_after=start_date,
            dated_before=end_date,
            limit=page_size,
            offset=current_page_num * page_size,
            )
            if len(curr_page_expenses) == 0:
                break
            current_page_num = current_page_num + 1
            self.expenses = self.expenses + curr_page_expenses
        return self.expenses
```
The retrieved expenses are then added to the `self.expenses` list which is an instance variable of the `ExpenseTracker` class. This process continues until there are no more expenses to retrieve.

Finally, the method returns the list of expenses retrieved from the API.

### Process the Fetched Data
The following code processes all field data and construct a dataframe for our convenience. More details of methods of data extraction are available here on [Splitwise Python SDK](https://github.com/namaggarwal/splitwise).
```py
    def process_expense(self):
        # get current user ID
        my_user_id = self.sw.getCurrentUser().getId()
        
        my_expenses = []
        for expense in self.expenses:
            for user in expense.users:
                if user.id == my_user_id and expense.deleted_at is None and expense.description != "Payment":
                    my_expenses.append(expense)
            
        data = {'id': [], 'group':[], 'description': [], 'amount': [], 'my_cost':[], 'person':[],\
                            'currency': [], 'date': [], 'category': []}
        
        
        for expense in my_expenses:
            try:
                data['id'].append(expense.id)
            except Exception as e:
                print(e)
                data['id'].append("0")
                
            try:
                data['group'].append(s.getGroup(expense.group_id).name)
            except Exception as e:
                print(e)
                data['group'].append("0")
            
            try:
                data['description'].append(expense.description)
            except Exception as e:
                print(e)
                data['description'].append("0")
            
            try:
                data['amount'].append(expense.cost)
            except Exception as e:
                print(e)
                data['amount'].append("0")
            
            try:
                data['my_cost'].append(next((user.getNetBalance() \
                                            for user in expense.getUsers() if user.id == my_user_id), 0))
            except Exception as e:
                print(e)
                data['my_cost'].append("0")
            
            try:
                data['person'].append(next((user.getFirstName()+" "+user.getLastName() \
                                            for user in expense.getUsers() if user.id != my_user_id), 0))
            except Exception as e:
                print(e)
                data['person'].append("0")
                
            try:
                data['currency'].append(expense.currency_code)
            except Exception as e:
                print(e)
                data['currency'].append("0")
            
            try:
                data['date'].append(expense.date)
            except Exception as e:
                print(e)
                data['date'].append("0")
                
            try:
                data['category'].append(expense.category.name)
            except Exception as e:
                print(e)
                data['category'].append("0")
        
        # create dataframe
        self.df = pd.DataFrame(data)
        return self.df
```

### Fix Data Types
Since all data are in string format, we need to change some for our convenience.
```py
    # fix data types since by default all are in string formats
    def fix_datatypes(self):
        self.df['my_cost'] = pd.to_numeric(self.df['my_cost'])
        self.df['my_cost'] = self.df['my_cost'].abs()
        self.df.date = pd.to_datetime(self.df.date)
        self.df.amount = pd.to_numeric(self.df.amount)
```

### Get Group Information
Since I wanted to have analysis based on each group I belong to, I extracted group names and expenses.
```py
    # return all group names in a list
    def get_group_names(self):
        return self.df["group"].to_list()
    
    # filter expense data based on particular group
    def get_group_expense(self, group_name):
        group_df = self.df.loc[self.df["group"] == group_name]
        return group_df
```


### Visualization
Now, it's visualization time. The code contains several functions that generate different types of visualizations based on the expense data. Here are short summaries of each function:

1.  `plot_monthly_group_expense`: Plots the total group expense per month for a given group.
2.  `plot_all_categorical_expense`: Plots the expense by category for all expenses.
3.  `plot_group_categorical_expense`: Plots the expense by category for a given group.
4.  `plot_monthly_personal_expense`: Plots the total personal expense per month for all expenses.
5.  `plot_monthly_personal_group_expense`: Plots the total personal expense per month for a given group.
6.  `plot_weekly_personal_expense`: Plots the total personal expense per week using a bar chart with dates on the x-axis.
```py
    #################################### VISUALIZATION #####################################
    
    def plot_monthly_group_expense(self, group_name):
        group_df = self.get_group_expense(group_name)
        group_df['amount'].groupby(group_df['date'].dt.to_period('M')).sum().plot(kind='bar')
    
        plt.xlabel('Month')
        plt.ylabel('Amount in USD')
        plt.title('Total group Expense per month')
        plt.show()
        
    
    def plot_all_categorical_expense(self):
        category_grp = self.df.groupby(self.df['category'])
        category_grp.amount.sum().plot(kind='bar')
        
        plt.ylabel('Amount in USD')
        plt.title('Expense by Category')
        plt.show()
        
        
    def plot_group_categorical_expense(self, group_name):
        group_df = self.get_group_expense(group_name)
        category_grp = group_df.groupby(group_df['category'])
        category_grp.amount.sum().plot(kind='bar')
        
        plt.ylabel('Amount in USD')
        plt.title('Expense by Category')
        plt.show()
        
        
    def plot_monthly_personal_expense(self):
        self.df['my_cost'].groupby(self.df['date'].dt.to_period('M')).sum().plot(kind='bar')
    
        plt.xlabel('Month')
        plt.ylabel('Amount in USD')
        plt.title('Total personal Expense per month')
        plt.show()
        
    
    def plot_monthly_personal_group_expense(self, group_name):
        group_df = self.get_group_expense(group_name)
        group_df['my_cost'].groupby(group_df['date'].dt.to_period('M')).sum().plot(kind='bar')
    
        plt.xlabel('Month')
        plt.ylabel('Amount in USD')
        plt.title('Total personal group Expense per month')
        plt.show()
        
        
    def plot_weekly_personal_expense(self):
        # # https://matplotlib.org/1.5.3/examples/pylab_examples/finance_demo.html
        mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
        alldays = DayLocator()              # minor ticks on the days
        weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
        dayFormatter = DateFormatter('%d')      # e.g., 12

        ax = plt.subplot(111)
        ax.bar(self.df.date, self.df.my_cost)
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
        ax.xaxis.set_major_formatter(weekFormatter)
        plt.show()
```

## Full Code
The full code is available here...
<script src="https://gist.github.com/shantoroy/1d6d3f35d9530437fa7205e3780d53fd.js"></script>

## usage
The following code imports the ExpenseTracker class from the class module. Here, we create an instance of the ExpenseTracker class and passes the Splitwise API authentication keys as arguments. 

Then it calls the `get_expenses()` method with the argument `target_days` set to 365, which retrieves all the expenses from the past year (365 days). This code is meant to be run from the command line, and it retrieves the expenses and outputs them to the console.
```py
#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   main.py
@Time    :   2023/03/09
@Version :   1.0
@Contact :   sroy10@uh.edu
@Desc    :   Main Namespace for Splitwise App
'''

# import modules
from my_splitwise import ExpenseTracker

    
if __name__ == '__main__':
    CONSUMER_KEY = '<Put your Consumer Key>'
    CONSUMER_SECRET = '<Put Your Consumer Secret>'
    API_KEY = '<Put your API Key>'
    
    my_sw = ExpenseTracker(CONSUMER_KEY,CONSUMER_SECRET,API_KEY)
    # change number of days for your convenience
    my_sw.get_expenses(target_days=365)
```

That's all for today! Cheers guys!!! 🤘


___

___

<iframe src="https://shantoroy.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>

I am also writing on Medium. You can [follow me here](https://medium.com/@shantoroy).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MzQ5NjYzODFdfQ==
-->