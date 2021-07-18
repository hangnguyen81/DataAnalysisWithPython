#!/usr/bin/env python3

import numpy as np
from numpy.lib.shape_base import split

'''
Create function get_row_vectors that returns a list of rows from the input array of shape (n,m), 
but this time the rows must have shape (1,m). 
Similarly, create function get_columns_vectors that returns a list of columns 
(each having shape (n,1)) of the input matrix .
'''

def get_row_vectors(a):
    n = a.shape[0]
    result = [row for row in np.split(a,n)]
    return result


def get_column_vectors(a):
    m = a.shape[1]
    result = [row for row in np.split(a,m, axis=1)]
    return result

'''
 # model solution
 def get_row_vectors(a):
    return np.split(a, a.shape[0], axis=0)
 
def get_column_vectors(a):
    return np.split(a, a.shape[1], axis=1)
'''   

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a, sep='\n')
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:\n", get_column_vectors(a),'\n')

if __name__ == "__main__":
    main()
