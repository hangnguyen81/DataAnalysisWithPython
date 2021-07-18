#!/usr/bin/env python3
'''
Write function read_series that reads input lines from the user and return a Series. 
Each line should contain first the index and then the corresponding value, separated by whitespace. 
The index and values are strings (in this case dtype is object). 
An empty line signals the end of Series. Malformed input should cause an exception. 
An input line is malformed, if it is non-empty and, when split at whitespace, does not result in two parts.
'''
import pandas as pd

def read_series():
    idx = []
    val = []
    while True:
        input_lines = input('Please enter the lines:')
        if input_lines == '': 
            break
        else:
            try:
                i,v = input_lines.split()
                idx.append(i)
                val.append(v)
            except:
                print('Something is wrong in here')
                continue
    return pd.Series(val, index=idx, dtype='object')

def main():
    print(read_series())

if __name__ == "__main__":
    main()
