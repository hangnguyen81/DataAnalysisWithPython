#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys

def swap(s):
    w = s.split()
    result = w[1] + ' ' + w[0]
    return result

def cleaning_data():
    #filepath = sys.path[0] + '/presidents.tsv'
    filepath = 'src/presidents.tsv'
    data = pd.read_csv(filepath, sep='\t')
    # Clean President column
    data["President"] = data["President"].str.replace(r"(\w+), *(\w+)", r"\2 \1").str.title()
    #data['President'] = data['President'].replace(r',','',regex=True)
    #data['President'] = data['President'].str.title()

    #clean Start column
    data['Start'] = data['Start'].apply(lambda x : x[:4])

    #clean Last column
    data['Last'] = data['Last'].replace('-',np.nan)

    #clean the Seasons column
    con = data['Seasons'] != 'two'
    data['Seasons'] = data['Seasons'].where(con,2)
    
    data["Vice-president"] = data["Vice-president"].str.replace(r"(\w+), *(\w+)", r"\2 \1").str.title()
    #data['Vice-president'] = data['Vice-president'].replace(r',','',regex=True)
    #data['Vice-president'] = data['Vice-president'].str.title()

    data = data.astype({'President':object, 'Start':int, 'Last':float, 'Seasons':int, 'Vice-president':object})
    return data

def main():
    df = cleaning_data()
    print("Shape:", df.shape)
    print("dtypes:", df.dtypes)
    print("Columns:", df.columns)
    print(df.head())
if __name__ == "__main__":
    main()
