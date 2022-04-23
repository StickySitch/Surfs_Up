#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


import datetime as dt


# # Reflect Tables into SQLAlchemy ORM

# In[4]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# 

# In[4]:





# In[5]:


# reflect an existing database into a new model
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(engine,reflect=True)


# In[6]:


# We can view all of the classes that automap found
Base.classes.keys()


# In[7]:


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[8]:


# Create our session (link) from Python to the DB
session = Session(engine)


# # Exploratory Climate Analysis

# In[9]:


# Design a query to retrieve the last 12 months of precipitation data and plot the results. 
#Starting from the last data point in the database. 

# Calculate the date one year from the last date in data set.
prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
# Perform a query to retrieve the data and precipitation scores
results = []
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
#print(results)
# Save the query results as a Pandas DataFrame and set the index to the date column
resultsDf = pd.DataFrame(results, columns=['date','precipitation'])
# Sort the dataframe by date
resultsDf.set_index(resultsDf['date'], inplace=True)
# Use Pandas Plotting with Matplotlib to plot the data
print(resultsDf)


# In[10]:


print(resultsDf.to_string(index=False))


# In[11]:


resultsDf = resultsDf.sort_index()


# In[12]:


print(resultsDf.to_string(index=False))


# In[13]:


# Displaying daily precipitation on bar graph
resultsDf.plot()


# In[14]:


# Use Pandas to calcualte the summary statistics for the precipitation data
resultsDf.describe()


# In[15]:


# How many stations are available in this dataset?
session.query(func.count(Station.station)).all()


# In[16]:


# What are the most active stations?
# List the stations and the counts in descending order.
session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()


# In[17]:


# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature most active station?
session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.station == 'USC00519281').all()


# In[18]:


# Choose the station with the highest number of temperature observations.
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram
results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prev_year).all()
df = pd.DataFrame(results, columns=['tobs'])
print(df)


# In[19]:


df.plot.hist(bins=12)
plt.tight_layout()


# In[20]:


# Write a function called `calc_temps` that will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates


# # Challenge

# In[20]:




