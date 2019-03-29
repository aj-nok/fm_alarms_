# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:00:27 2019

@author: aj-nok
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


data = pd.read_csv('fm_alarms_18012019_085951.csv', usecols=['CONSEC_NBR','EVENT_TIME'], parse_dates=['EVENT_TIME'])
                                                                   #importing csv and parsing date fields

  
data.set_index('EVENT_TIME',inplace=True)                          #plotting date
fig, ax = plt.subplots(figsize=(25,8))
data.plot(ax=ax)

