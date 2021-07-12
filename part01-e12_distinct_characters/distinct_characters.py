#!/usr/bin/env python3

def distinct_characters(L):
    dict_={}
    for l in L:
       dict_[l] = len(set(l))
    return dict_

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
