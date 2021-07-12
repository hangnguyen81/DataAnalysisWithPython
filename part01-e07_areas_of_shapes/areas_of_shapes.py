#!/usr/bin/env python3

import math


def main():
    while 1:
        chosen = input('Choose a shape (triangle, rectangle, circle):')
        chosen = chosen.lower()
        if chosen == '':
            break
        elif chosen == 'triangle':
            b=int(input('Give base of the triangle:'))
            h=int(input('Give height of the triangle:'))
            area = (b * h)/2
            print(f"The area is {area}")
        elif chosen == 'rectangle':
            w = int(input('Give width of the rectangle:'))
            h = int(input('Give height of the rectangle'))
            area = w * h
            print(f"The area is {area}")
        elif chosen == 'circle':
            r = int(input('Give radius of the circle:'))
            area = math.pi * r**2
            print(f"The area is {area}")
        else:
            print('Unknown shape!')


if __name__ == "__main__":
    main()
