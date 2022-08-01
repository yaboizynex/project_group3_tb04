#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd 

def coh_function(forex):
    #read input data
    df = pd.read_csv('csv_reports/Cash_on_Hand.csv')
    
    #extract 2 columns from 
    df = df[['Day', "Amount"]]
    #print(df.head())
    #print()
    
    
    #calculate the unique ordered days
    days=set(df['Day'])
    
    #calculate sums of amount for each day
    data=df.groupby(['Day']).sum()
    
    #print(data)
    #print()
    
    df=data
    
    #how many row (how many days) we have
    rows_count = len(df.index)
    
    #array with previous  day's summarised amount
    prev=df['Amount'][0:rows_count-1].to_numpy()
    
    #array with next day's summarised amount
    next=df['Amount'][1:rows_count].to_numpy()
    
    #difference
    diff=next - prev
    #print(diff)
    
    prev=df['Amount'][0:rows_count].to_numpy()
    
    #convert to list
    days=list(days)
    #print(days[0],': NaN')
    #for i in range(1,len(days)):
        #print(days[i],': ', diff[i-1], '  prev: ', prev[i])
    
    #compare summarised amount for each day
    flag=False; #not found
    for i in range(0,len(days)):
        try:
            if diff[i]<0:
                flag=True #found
                print('[CASH DEFICIT] DAY: %.1f, AMOUNT: %.1f' % (days[i+1], prev[i+1]))
        except:
            continue
    
    
    if not flag:
        print('CASH OF EACH DAYS IS HIGHER THAN THE PREVIOUS DAY')
