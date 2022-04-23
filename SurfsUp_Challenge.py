#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import numpy as np
import pandas as pd
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# In[2]:


engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[3]:


# Create our session (link) from Python to the DB
session = Session(engine)


# ## D1: Determine the Summary Statistics for June

# In[4]:


# 1. Import the sqlalchemy extract function.
from sqlalchemy import extract
import datetime as dt
# 2. Write a query that filters the Measurement table to retrieve the temperatures for the month of June.

juneTemps = session.query(Measurement.date, Measurement.tobs).filter(extract('month',Measurement.date) ==6).all()

print(juneTemps)


# In[5]:


#  3. Convert the June temperatures to a list.
juneTempsList = list(juneTemps)


# In[6]:


# 4. Create a DataFrame from the list of temperatures for the month of June.
juneTempsDf = pd.DataFrame(juneTempsList, columns=['date','June Temps'])
juneTempsDf.set_index(juneTempsDf['date'], inplace=True)


# In[7]:


# 5. Calculate and print out the summary statistics for the June temperature DataFrame.
juneTempsDf.describe()


# ## D2: Determine the Summary Statistics for December

# In[8]:


# 6. Write a query that filters the Measurement table to retrieve the temperatures for the month of December.
decTemps = session.query(Measurement.date, Measurement.tobs).filter(extract('month',Measurement.date) ==12).all()
print(decTemps)


# In[9]:


# 7. Convert the December temperatures to a list.
decTempsList = list(decTemps)


# In[10]:


# 8. Create a DataFrame from the list of temperatures for the month of December. 
decTempsDf = pd.DataFrame(decTempsList,  columns=['date','Dec Temps'])


# In[11]:


# 9. Calculate and print out the summary statistics for the Decemeber temperature DataFrame.
decTempsDf.describe()

