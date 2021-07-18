#!/usr/bin/env python3

from string import punctuation
import sys
import re

def word_frequencies(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        
    word_count = {}

    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip(punctuation)
            if word in word_count.keys():
                word_count[word] = word_count[word] + 1
            else:
                word_count[word] = 1
    return word_count

def main():
    filename =sys.path[0] + '/alice.txt'
    for word, count in word_frequencies(filename).items():
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
