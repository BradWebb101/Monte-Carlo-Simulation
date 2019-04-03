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

#Uncomment out for first run to get pickle data
#Data import from Quandl API
#df = pd.DataFrame(quandl.get("EOD/AAPL", authtoken="SAsM3P3YGsmFwxsDsyu6"))

#Sending data to AAPL pickle
#df.to_pickle('AAPL_pickle')

#Reading ('AAPl pickle')
df = pd.DataFrame(pd.read_pickle('AAPL_pickle'))

aapl = pd.DataFrame()
aapl['Price'] = df['Adj_Close']
aapl['Log Return'] = np.log(df['Adj_Close']/df['Adj_Close'].shift(1))

#Mean and SD from 12 month previous data
aapl_12 = aapl.loc['2018-04-03':'2019-04-02','Log Return']
aapl_12 = aapl_12.describe()

#Starting AAPL price
aapl_start = df['Adj_Close'][-1]

#Running simulation
def monte_carlo_simulation(simulations, years_to_simulate):
    time = aapl_12
    start_price = aapl['Price'][-1]
    plt.figure(figsize=(20,10))
    final_price = []
    for i in range(simulations):
        start_price = aapl_start
        trading_days_simulated = 1
        mean = time.loc['mean']
        sd = time.loc['std']
        trading_days = 252
        simulated_price = []
        days_simulated = []
        for days in range(years_to_simulate * trading_days):
            price = start_price * (1+(random.normal(mean, sd)))
            simulated_price.append(price)
            days_simulated.append(trading_days_simulated)
            start_price = price
            trading_days_simulated +=1
            if trading_days_simulated == (252*years_to_simulate):
                final_price.append(price)                
        plt.plot(days_simulated, simulated_price)
    return(final_price, start_price)        
        
x = monte_carlo_simulation(1000,10)
plt.ylabel('AAPL Price')
plt.xlabel('Trading Days Simulated')
plt.rc('xtick', labelsize=30)
plt.rc('ytick', labelsize=30)
plt.show()
plt.figure(figsize=(20,10))
plt.hist(x,bins=50)
plt.show()        
    
#printing stats from experiment
print('This experiment ran ' + str(len(x[0]))+' times')
print('---------------------------------------------')
print('The max share price was $' + str(round(max(x[0]), 2)))
print('---------------------------------------------')
a = (((sum(x[0])/(len(x[0]))/aapl_start)*10000))
print('If I invested $10,000 in apple today at the end of the simulation it would be worth $' + str(round(a, 2)))





