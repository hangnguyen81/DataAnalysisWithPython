#!/usr/bin/python3
'''
Write function meeting_lines that gets the coefficients of two lines as parameters 
and returns the point where the two lines meet. 
The equations for the lines are y=a1x+b1 and y=a2x+b2. Use the np.linalg.solve function. 
Create a main function to test your solution.
'''

import numpy as np
from scipy.linalg import solve

def meeting_lines(a1, b1, a2, b2):
    x, y = solve([[a1,-1],[a2,-1]], [-b1,-b2])
    return x,y

'''
#model solution
def meeting_lines(a1, b1, a2, b2):
    A=np.array([[-a1,1],[-a2,1]])
    b=np.array([b1,b2])
    sol = np.linalg.solve(A, b)
    return sol
'''

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
