# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:17:00 2019

@author: bradw
"""

import quandl
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt


#Data import from Quandl API
#df = pd.DataFrame(quandl.get("EOD/AAPL", authtoken="SAsM3P3YGsmFwxsDsyu6"))

#Sending data to AAPL pickle
#df.to_pickle('AAPL_pickle')

#Reading ('AAPl pickle')
df = pd.read_pickle('AAPL_pickle')

df = pd.DataFrame(df['Adj_Close'])

df['Return'] = (df['Adj_Close'] - df['Adj_Close']).shift(1) / df['Adj_close'].shift(1)

df['Log Return'] = log(df['Return'])

#Creating 12 months previous data
df1 = df.loc['2018-1-30':'2019-1-31']

#Checking time frame, confirmed 252 trading days
df1.info()
df1_stats = df1.describe()

#Setting up randn with mean and sd from sample
def price_append(T,n):
    mean = (df1_stats.iloc[1,1])
    sd = df1_stats.iloc[2,1]    
    N = 0
    while n > N:
        price = df1.iloc[-1,0]
        t = 1
        pX = []
        pY = []
        while T > t:
            price = price + (price * (sd * (random.randn()) + mean))
            pX.append(t)
            pY.append(price)
            t+=1
            fig = plt.plot(pX,pY)
        N+=1 
        print('Ran Simulation No.'+str(N))
    
#price_append(1008,10)
plt.show()
print('Script Finished')