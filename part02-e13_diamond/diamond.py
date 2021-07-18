#!/usr/bin/env python3
'''
Create a function diamond that returns a two dimensional integer array where the 1s form a diamond shape. 
Rest of the numbers are 0. The function should get a parameter that tells the length of a side of the diamond. 
Do this using the eye and concatenate functions of NumPy and array slicing.
'''
import numpy as np
from numpy.core.records import array

def diamond(n):
    inital_array = np.eye(n, dtype=int)
    half_diamond = np.concatenate((inital_array[::-1],inital_array[:,1:]), axis=1)
    full_diamond = np.concatenate((half_diamond[:-1],half_diamond[::-1]), axis=0) 
    return full_diamond

def main():
    print(diamond(4))

if __name__ == "__main__":
    main()
