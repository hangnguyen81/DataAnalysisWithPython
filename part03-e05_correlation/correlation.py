#!/usr/bin/env python3

'''
Load the iris dataset using the provided function load() in the stub solution. 
The four columns of the returned array correspond to
- sepal length (cm)
- sepal width (cm)
- petal length (cm)
- petal width (cm)

Part 1. What is the Pearson correlation between the variables sepal length and petal length. 
Compute this using the scipy.stats.pearsonr function. 
It returns a tuple whose first element is the correlation. 
Write a function lengths that loads the data and returns the correlation.

Part 2. What are the correlations between all the variables. 
Write a function correlations that returns an array of shape (4,4) containing the correlations. 
Use the function np.corrcoef. Which pair of variables is the most highly correlated?

Note the input formats of both functions pearsonr and corrcoef.
'''

from os import stat
import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    sepal_length = data[:,0]
    petal_length = data[:,2]
    r = scipy.stats.pearsonr(sepal_length,petal_length)[0]
    return r

def correlations():
    data = load()
    return data.T #np.corrcoef(data.T)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
