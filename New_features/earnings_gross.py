# -*- coding: utf-8 -*-
"""earnings_gross.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZwjrM3lr-wz8Fy6m_cRCb_hce1wAkq-y
"""

import pandas as pd #data processing

file='final.csv' #load the current dataset 
earn = pd.read_csv(file)
print(earn.describe()) #statistics

"""Adding a new geature- earnings_gross- the amount of money that could be earned during the trip, including waiting time

references :
https://www.destatis.de/EN/Themes/Labour/Earnings/Earnings-Earnings-Differences/_node.html

24.44 €
hourly gross earnings in Germany

"""

#add the new column for future feature
earn['earnings_gross'] = 0.00 #make it a float

"""populate the column with the values according to a formula: hourly gross earnings*(total travel time in hours+total waiting time in hours)"""

for i in range(0, len(earn)): #iterate
    earn['earnings_gross'][i] = 24.44 * (earn['totaltraveltimeinhours'][i] + earn['totalwaitingtime'][i])#apply computations

earn # check the dataframe

#round 'earnings' in euros up to 2 decimals after comma
def round(d):
  d=d.round({'earnings_gross': 2})
  return d

earnew = round(earn)
earnew

earnew.drop('Unnamed: 0', axis=1, inplace=True)
earnew

#download the new file for sharing with the team
from google.colab import files
earnew.to_csv('final+.csv') 
files.download('final+.csv')
