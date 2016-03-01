import matplotlib.pyplot as plt
import matplotlib

import pandas as pd
import numpy as np

import datetime

def parse_file(path):
    orig_data = pd.read_csv(path, parse_dates=['Created Date'], low_memory=False)
    return(orig_data)

def build_plot(df,x_var,y_var,color):
    plt.scatter(df[x_var], df[y_var], c=color)
    plt.grid(True)
    plt.legend()
    plt.show()
    
def convert_datetime_to_date(x):
    if isinstance(x, datetime.datetime):
        return datetime.datetime.date(x)
    return x 
        
def build_plots_for_complaints(df):
    df = df[  ( df['Created Date'].notnull() ) & ( df['Complaint Type'].notnull() ) & ( df['Complaint Type'] == 'Noise - Street/Sidewalk') ]
    df['Created Date'] = df['Created Date'].apply(lambda x: convert_datetime_to_date(x))
    
    # filter out rows that have NaN (null) Complaint Types, AND only give me rows that have noise complaints
    
    complaints_grped_by_date = df.groupby('Created Date') # keying by complaint (grouping = keying)
    
    data = { 'dates' : [], 'complaints' : [] } # this dictionary will populate in the group
    for date, group in complaints_grped_by_date:
        data['dates'].append(date) # get me key name (group name)
        data['complaints'].append(len(group)) # get me length of group
        
    plt.scatter(data['dates'], data['complaints'], c="purple") # graph
    plt.grid(True)
    plt.legend()
    plt.show()

path = '../../assets/dataset/311-service-requests.csv'
df = parse_file(path)
df.head() # show first rows of data_frame
df.tail(3) # show last three rows
build_plot(df, x_var = 'Longitude', y_var = 'Latitude', color = "purple") # run build_plot function
build_plots_for_complaints(df) # run build_plots_for_complaints function
