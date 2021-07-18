#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    x1 = np.array([2,4,6,7])
    y1 = np.array([4,3,5,1])
    x2 = np.array([1,2,3,4])
    y2 = np.array([4,2,3,1])

    plt.plot(x1,y1, 'b-')
    plt.plot(x2,y2, 'y-')
    plt.axes([1,7,1,5])
    plt.title('Multiple graphs by Pyplot')
    plt.xlabel('X range')
    plt.ylabel('Y range')
    plt.show()
    pass

if __name__ == "__main__":
    main()
