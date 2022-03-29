#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
from csv import DictReader
import json
import pandas as pd
import re

#use pandas to read the data
airport = pd.read_csv('airports.csv')

# creating a new csv file excluding data with word 'closed'
newFile = airport[(airport['type'] != 'closed')]
newFile.to_csv('newAirportData.csv')
newAirportfile = pd.read_csv('newAirportData.csv')
newAirportfile

# filtering the new file out for GB airports
GBfile = newAirportfile[(newAirportfile['iso_country'] == 'GB')]

#write the new data onto new file
GBfile.to_csv('newGBData.csv')


#read the new data to add frequency data on
airportGB = pd.read_csv('newGBData.csv')

#open the frequency file and merge columns with same data together
freq = pd.read_csv('airport-frequencies.csv')

#this merges airport data using the 'ident' column which matches frequecy file 'airport_ident'
airportPlusfreq = pd.merge(airportGB,freq, left_on = 'ident',right_on =  'airport_ident')

# the new mergerd data is written to a new file
airportPlusfreq.to_csv('airportGBFrequecy.csv') 


file = pd.read_csv('airportGBFrequecy.csv')

file
           


    


# In[4]:






                           
            


# In[170]:



   
   


# In[171]:


#use pandas to read the data
airport = pd.read_csv('airports.csv')
cols = ['type_x','small_airport','medium_airport', 'large_airport']
airport[cols]


# In[ ]:




