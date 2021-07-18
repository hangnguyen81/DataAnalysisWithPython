#!/usr/bin/env python3
'''
Part 1.

Write a function to_grayscale that takes an RGB image (three dimensional array) 
and returns a two dimensional gray-scale image. 
The conversion to gray-scale should take a weighted sum of the red, green, and blue values, 
and use that as the value of gray. The first axis is the x, the second is y, 
and the third is the color components (red, green, blue). 
Use the weights 0.2126, 0.7152, and 0.0722 for red, green, and blue, respectively. 
These weights are so because the human eye is most sensitive to green color and least sensitive to blue color.

In the main function you can, for example, use the provided image src/painting.png. 
Display the grayscale image with the plt.imshow function. 
You may have to call the function plt.gray to set the color palette (colormap) to gray. 
(See help(plt.colormaps) for more information about colormaps.)
'''

import numpy as np
import matplotlib.pyplot as plt
import sys

def to_grayscale(a):
    w=np.array([0.2126, 0.7152, 0.0722]).reshape(1, 1, 3)
    img = a * w
    return img.sum(axis=2)

def to_red(a):
    img = a.copy()
    img[:,:,(1,2)] = 0
    return img

def to_green(a):
    img = a.copy()
    img[:,:,(0,2)] = 0
    return img

def to_blue(a):
    img = a.copy()
    img[:,:,(0,1)] = 0
    return img

def main():
    filename = sys.path[0]+'/painting.png'
    painting=plt.imread(filename)
    gray = to_grayscale(painting)
    red = to_red(painting)
    green = to_green(painting)
    blue = to_blue(painting)
    plt.imshow(painting)
    plt.figure()
    plt.gray()
    plt.imshow(gray)
    plt.subplot(3, 1, 1)
    plt.imshow(red)
    plt.subplot(3, 1, 2)
    plt.imshow(green)
    plt.subplot(3, 1, 3)
    plt.imshow(blue)
    plt.show()

if __name__ == "__main__":
    main()
