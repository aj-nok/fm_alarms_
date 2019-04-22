# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:52:58 2019

@author: aj-nok
"""

import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/ajas/Desktop/fm_alarms_18012019_085951.csv')

df['ALARM_TIME'] = pd.to_datetime(df['ALARM_TIME'], dayfirst=True)                      #DATE PARSING
df['CANCEL_TIME'] = pd.to_datetime(df['CANCEL_TIME'], dayfirst=True)
df['ACK_TIME'] = pd.to_datetime(df['ACK_TIME'], dayfirst=True)
df['EVENT_TIME'] = pd.to_datetime(df['EVENT_TIME'], dayfirst=True)
df['INSERT_TIME'] = pd.to_datetime(df['INSERT_TIME'], dayfirst=True)
#df['TERMINATED_TIME'] = pd.to_datetime(df['TERMINATED_TIME'], dayfirst=True)



df=df[ df['CANCEL_TIME'].notnull() & df['ALARM_TIME'].notnull() ]                       #ADDING NEW FIELD
df['diff_seconds'] = df['CANCEL_TIME'] - df['ALARM_TIME']
df['diff_seconds']=df['diff_seconds']/np.timedelta64(1,'s')


df.to_csv('C:/Users/ajas/Desktop/new_new_alarm.csv')                                     #EXPORTING CSV


