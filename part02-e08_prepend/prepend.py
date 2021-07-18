#!/usr/bin/env python3

class Prepend(object):
    '''
    Create a class called Prepend. 
    We create an instance of the class by giving a string as a parameter to the initializer. 
    The initializer stores the parameter in an instance attribute start. 
    The class also has a method write(s) which prints the string s prepended with the start string. 
    '''
    def __init__(self, string):
        self.start = string

    def write(self, s):
        print(self.start + s)     

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
