#!/usr/bin/env python3
''' triangle.py: This module contains two functions: hypotenuse and area'''
import math

__author__ = 'Hang Nguyen'
__version__ = '1.0'

def hypothenuse(a,b):
    '''This function returns the length of the hypothenuse 
    when given the lengths of two other sides of a right-angled triangle 
    '''
    return math.sqrt(a**2 + b**2)

def area(a,b):
    '''returns the area of the right-angled triangle, 
    when two sides, perpendicular to each other, are given as parameters.
    '''
    return 0.5*a*b


