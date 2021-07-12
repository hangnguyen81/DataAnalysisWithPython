#!/usr/bin/env python3

def transform(s1, s2):
    w1 = s1.split()
    w2 = s2.split()
    result = []
    for x,y in zip(map(int,w1),map(int,w2)):
        result.append(x*y)
    return result
    # model solution
    #return [ a*b for (a, b) in zip(map(int, s1.split()), map(int, s2.split())) ]

def main():
    print(transform("1 5 3", "2 6 -1"))
if __name__ == "__main__":
    main()
