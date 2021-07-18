#!/usr/bin/env python3
'''
Write function first_half_second_half that gets a two dimensional array of shape (n,2*m) as a parameter. 
The input array has 2*m columns. 
The output from the function should be a matrix with those rows from the input 
that have the sum of the first m elements larger than the sum of the last m elements on the row. 
Your solution should call the np.sum function or the corresponding method exactly twice.
'''
import numpy as np

def first_half_second_half(a):
    m = a.shape[1]//2
    first_half = np.sum(a[:,0:m], axis=1)
    second_half =np.sum(a[:,m:], axis=1)
    mask = first_half > second_half
    return a[mask]

def main():
    a = np.array([[1, 3, 4, 2],[2, 2, 1, 2],[5,4,2,3]])
    print(first_half_second_half(a))

'''
#model solution
def first_half_second_half(a):
    a1, a2 = np.split(a, 2, axis=1)
    mask = np.sum(a1, axis=1) > np.sum(a2, axis=1)
    return a[mask]
 
def main():
    m=4
    n=10
    np.random.seed(0)
    a = np.random.randn(n, 2*m)
    np.set_printoptions(linewidth=1000)
    print("a:\n", a)
    print("result:\n", first_half_second_half(a))
'''    

if __name__ == "__main__":
    main()
