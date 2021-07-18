#!/usr/bin/env python3

import sys

def file_count(filename):
    '''
    The function should read the file, count the number of lines, words, and characters in the file, 
    and return a triple with these count in this order. You get division into words by splitting at whitespace. 
    You don’t have to remove punctuation.
    '''
    with open(filename, 'r') as f:
        lines = f.readlines()

    line_count = len(lines)

    word_count = 0
    character_count = 0
    for line in lines:
        try:
            words = line.split()
            word_count = word_count + len(words)
            character_count = character_count + len(line) 
        except:
            continue

    return (line_count, word_count, character_count)

def main():
    '''
    filename =sys.path[0] + '/test.txt'
    print(file_count(filename))
    '''
    for file in sys.argv[1:]:
        line_count, word_count, character_count = file_count(file)
        print(f"{line_count}\t{word_count}\t{character_count}\t{file}")

if __name__ == "__main__":
    main()
