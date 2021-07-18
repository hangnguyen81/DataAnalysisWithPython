#!/usr/bin/env python3

class Rational(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x}/{self.y}"

    def __mul__(num1, num2):
        return Rational(num1.x*num2.x, num1.y*num2.y)

    def __truediv__(num1, num2):
        return Rational(num1.x*num2.y, num1.y*num2.x)

    def __add__(num1, num2):
        return Rational(num1.x*num2.y + num2.x*num1.y, num1.y*num2.y)

    def __sub__(num1, num2):
        return Rational(num1.x*num2.y - num2.x*num1.y, num1.y*num2.y)

    def __eq__(num1, num2):
        return num1.x == num2.x and num1.y == num2.y

    def __gt__(num1, num2):
        return num1.x*num2.y > num2.x*num1.y

    def __lt__(num1, num2):
        return num1.x*num2.y < num2.x*num1.y

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
