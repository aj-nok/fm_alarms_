# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:00:27 2019

@author: aj-nok
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


data = pd.read_csv('fm_alarms_18012019_085951.csv', usecols=['CONSEC_NBR','EVENT_TIME'], parse_dates=['EVENT_TIME'])
data=data.sort_values('CONSEC_NBR')
data.set_index('EVENT_TIME',inplace=True)

#data1 = pd.read_csv('fm_alarms_18012019_085951.csv', usecols=['INSERT_TIME','CONSEC_NBR'], parse_dates=['INSERT_TIME'])
#data1=data1.sort_values('CONSEC_NBR')
#data1.set_index('INSERT_TIME',inplace=True)

fig, ax = plt.subplots(figsize=(25,8))
data.plot(ax=ax)
#ax.yaxis_date()
#data1.plot(ax=ax)


#ax.xaxis.set_major_locator(mdates.WeekdayLocator())
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
