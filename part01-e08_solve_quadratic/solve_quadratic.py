#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    t = math.sqrt(b**2 - 4*a*c)
    x1 = ((-b) + t )/(2*a)
    x2 = ((-b) - t)/(2*a)
    return (x1,x2)


def main():
    print('Quadratic equation result is (%.1f,%.1f)' %solve_quadratic(-2,2,1))

if __name__ == "__main__":
    main()
