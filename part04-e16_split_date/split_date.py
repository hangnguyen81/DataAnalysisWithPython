#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys

def split_date():
    filename = sys.path[0] + '/Helsingin_pyorailijamaarat.csv'
    #filename = 'src/Helsingin_pyorailijamaarat.csv'
    data = pd.read_csv(filename, sep=';')
   
    # drop rows contain all missing values
    df = data.dropna(axis=0, how='all')
    # drop columns that contain only missing values
    df = df.dropna(axis=1, how='all')

    #split columns Päivämäärä into 5 columns
    df_date = df['Päivämäärä'].str.split(expand=True)
    #add the headers to columns of dataframe
    headers =['Weekday', 'Day', 'Month', 'Year', 'Hour']
    df_date.columns = headers
  
    # create a mapping dictionary that contains each column to process 
    # as well as a dictionary of the values to translate.
    replace_day_month = {'Weekday':{'ma':'Mon','ti':'Tue','ke':'Wed','to':'Thu','pe':'Fri','la':'Sat','su':'Sun'},
                        'Month':{'tammi':1, 'helmi':2,'maalis':3,'huhti':4,'touko':5,'kesä':6,'heinä':7, 
                                'elo':8, 'syys':9, 'loka':10,'marras':11,'joulu': 12}
                        }
    df_date = df_date.replace(replace_day_month)

    df_date['Hour'] = df_date['Hour'].apply(lambda x: x[:2])

    df_date[['Day','Year','Hour']] = df_date[['Day','Year','Hour']].astype(int)

    return df_date
'''
#model solution
days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))
 
def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
 
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:,0]
 
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d
'''
def main():
    df = split_date()
    print("Shape:", df.shape)
    print("dtypes:", df.dtypes)
    print("Columns:", df.columns)
    print(df.head())
       
if __name__ == "__main__":
    main()
