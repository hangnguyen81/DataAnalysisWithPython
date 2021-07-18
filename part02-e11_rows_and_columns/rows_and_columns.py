#!/usr/bin/env python3

import numpy as np
'''
Write two functions, get_rows and get_columns, that get a two dimensional array as parameter. 
They should return the list of rows and columns of the array, respectively. 
The rows and columns should be one dimensional arrays. 
'''

def get_rows(a):
    rows = a.shape[0]
    list_rows = []
    for i in range(0,rows):
        item = a[i] # or a[i]
        list_rows.append(item)

    return list_rows


def get_columns(a):
    a = a.T
    cols = a.shape[0]
    list_cols = []
    for i in range(0,cols):
        item = a[i]
        list_cols.append(item)
    return list_cols

'''
#model solution
def get_rows(a):
    result = [row for row in a]
    return result
 
def get_columns(a):
    result = [row for row in a.T]
    return result
'''    

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
