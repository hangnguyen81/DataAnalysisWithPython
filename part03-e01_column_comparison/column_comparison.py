#!/usr/bin/env python3
'''
Write function column_comparison that gets a two dimensional array as parameter. 
The function should return a new array containing those rows from the input 
that have the value in the second column larger than in the second last column. 
You may assume that the input contains at least two columns. 
Don’t use loops, but instead vectorized operations. Try out your function in the main function.
'''

import numpy as np

def column_comparison(a):
    mask = a[0:,1] > a[0:,-2]
    return a[mask]
    
def main():
    test = np.array([[8,9,3,8,8], [0,5,3,9,9], [5,7,6,0,4], [7,8,1,6,2], [2,1,3,5,8]])
    print('Original array:\n',test)
    print('Result: \n',column_comparison(test))

'''
# model solution
def column_comparison(a):
    mask = a[:,1] > a[:,-2]
    return a[mask]
    
def main():
    np.random.seed(0)
    a=np.random.randn(10,10)
    np.set_printoptions(linewidth=1000)
    print("a:\n", a)
    print("result:\n", column_comparison(a))
'''

if __name__ == "__main__":
    main()
