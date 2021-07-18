#!/usr/bin/env python3
'''
Write function subfigures that creates a figure that has two subfigures (two axes in matplotlib parlance). 
The function gets a two dimensional array a as a parameter. 

In the left subfigure draw using the plot method a graph, 
whose x coordinates are in the first column of a and the y coordinates are in the second column of a. 

In the right subfigure draw using the scatter method a set of points whose x coords are again in the first column 
of a and whose y coordinates are in the second column of a. 

Additionally, the points should get their color from the third column of a, 
and size of the point from the fourth column of a. 
For this, use the c and s named parameters of scatter, respectively
'''
import numpy as np
import matplotlib.pyplot as plt
'''
def subfigures(a):
    
    col1 = a[:,0]
    col2 = a[:,1]
    col3 = a[:,2]
    col4 = a[:,3]
    # The left subfigure
    plt.subplot(1,2,1)
    plt.plot(col1,col2)

    # the right subfigure
    plt.subplot(1,2,2)
    plt.scatter(col1, col2,c=col3,s=col4)
    plt.show()
    return plt

def main():
    #np.random.seed(0)
    #a=np.random.randint(0,10, (2,2))
    a = np.array([[5,1,25,25],[3,3,50,25]])
    subfigures(a)
'''
#model solution
def subfigures(a):
    fig, ax = plt.subplots(1,2, figsize=(6,3))
    ax[0].plot(a[:,0], a[:,1])
    ax[1].scatter(a[:,0], a[:,1], c=a[:,2], s=a[:,3])
    plt.show()
 
def main():
    n = 10
    a = np.random.randint(0, 10, (n, 3))
    print(a)
    print(a.dtype)
    print(a.shape)
    a = np.concatenate([np.arange(n)[:, np.newaxis], a], axis=1)
    subfigures(a)
if __name__ == "__main__":
    main()
