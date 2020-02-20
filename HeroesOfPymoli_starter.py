#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[18]:


# Dependencies and Setup
import pandas as pd
import numpy as np


# In[19]:


# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[20]:


purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[25]:


T_players = len(purchase_data["SN"].value_counts())


# In[27]:


T_players_df = pd.DataFrame({"Total Players":[T_players]})
T_players_df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[45]:


Unique_items = len(purchase_data["Item ID"].unique())
Average = purchase_data["Price"].mean()
purchases = len(purchase_data["Price"])
Total_revenue = sum(purchase_data["Price"])

purchase_data_df = pd.DataFrame({"Number of Unique Items": [Unique_items],
                              "Average Price": Average,
                              "Number of Purchases": purchases,
                              "Total Revenue": Total_revenue})

purchase_data_df["Average Price"] = purchase_data_df["Average Price"].map("${:.2f}".format)
purchase_data_df["Total Revenue"] = purchase_data_df["Total Revenue"].map("${:.2f}".format)

purchase_data_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[81]:


#drop duplicates
gender_data = purchase_data.loc[:,["Gender", "SN"]]
gender_data = gender_data.drop_duplicates()

#total for each gender
gender_total = gender_data["Gender"].value_counts()

#percentage
percent = gender_total /T_players*100

#summary table
purchase_data_df = pd.DataFrame({"TOTAL COUNT": gender_total,
                              "TOTAL PERCENTAGE OF PLAYERS":percent})
purchase_data_df.head()



# reduce decimal points
purchase_data_df["TOTAL PERCENTAGE OF PLAYERS"] = purchase_data_df["TOTAL PERCENTAGE OF PLAYERS"].map("{:.2f}".format)
purchase_data_df.head()



# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[87]:


purchase_count = purchase_data.groupby(["Gender"]).sum()["Price"]
purchase_count


average_price = purchase_data.groupby(["Gender"]).mean()["Price"]
#genderaverage = genderaverage.round(2)
average

Total_counts = purchase_data.groupby(["Gender"]).count()["Price"]
Total_counts

purchase_data_df = pd.DataFrame({"Purchase count":gender_total, "Average Purchase Price": average_price,"Total Purchase Price":purchase_count,
                                 "Normalized Totals": Total_counts})

#Clean up formatting and reorder columns
purchase_data_df["Average Purchase Price"] = purchase_data_df["Average Purchase Price"].map("${:,.2f}".format) 
purchase_data_df["Total Purchase Price"] = purchase_data_df["Total Purchase Price"].map("${:,.2f}".format) 
purchase_data_df["Normalized Totals"] = purchase_data_df["Normalized Totals"].map("${:,.2f}".format) 
#Reorder Columns
#gender_analysis = gender_analysis[["Average Purchase Price", "Total Purchase Price", "Normalized Totals"]]

purchase_data_df.head()


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[139]:


bins= [0, 10, 15, 20, 25, 30, 35, 40, 200]
groups =["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", ">40"]

purchase_data["age group"] = pd.cut(purchase_data["Age"], bins, labels=groups)
purchase_data

purchase_totals = purchase_data["age group"].value_counts()

purchase_percent = purchase_totals / T_players * 100

purchase_data_df = pd.DataFrame({"Total Count": purchase_totals, "Percent of Players": purchase_percent})

purchase_data_df.head()


# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[145]:


purchase_data["age group"] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)


purchasecount = purchase_data.groupby(["age group"]).sum()["Price"]
purchasecount

averageprice = purchase_data.groupby(["age group"]).mean()["Price"]
averageprice

totalpurchase = purchase_data.groupby(["age group"]).count()["Price"]
totalpurchase

#summary table
purchase_data_df = pd.DataFrame({"Purchase Count": purchasecount, "Average Purchase Price": averageprice, "Total Purchase Value": totalpurchase})

purchase_data_df.head()


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[8]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[9]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[10]:




