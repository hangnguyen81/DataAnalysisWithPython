#!/usr/bin/env python3
'''
Write function vector_lengths that gets a two dimensional array of shape (n,m) as a parameter. 
Each row in this array corresponds to a vector. 
The function should return an array of shape (n,), that has the length of each vector in the input. 
The length is defined by the usual Euclidean norm. Don’t use loops at all in your solution. 
Instead use vectorized operations. You must use at least the np.sum and the np.sqrt functions. 
You can’t use the function scipy.linalg.norm. Test your function in the main function.
'''

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a = a**2
    result = np.sqrt(np.sum(a, axis=1))
    return result

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,5))
    print("a:", a, sep='\n')
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
