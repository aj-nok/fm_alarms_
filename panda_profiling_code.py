# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:24:10 2019

@author: aj-nok
"""

import pandas as pd
import pandas_profiling 

df=pd.read_csv('C:/Users/aj-nok/Desktop/fm_alarms_18012019_085951.csv')
#parse_dates=['ALARM_TIME','ACK_TIME','CANCEL_TIME','EVENT_TIME','INSERT_TIME','TERMINATED_TIME']
profile = pandas_profiling.ProfileReport(df)
profile.to_file(outputfile="C:/Users/aj-nok/Desktop/profiling_output.html")
