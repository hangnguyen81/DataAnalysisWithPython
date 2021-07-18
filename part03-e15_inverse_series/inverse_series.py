#!/usr/bin/env python3
'''
Write function inverse_series that get a Series as a parameter 
and returns a new series, whose indices and values have swapped roles. 
Test your function from the main function.

What happens if some value appears multiple times in the original Series? 
What happens if you use this value to index the resulting Series?
'''

import pandas as pd

def inverse_series(s):
    return pd.Series(s.index,s.values)

def main():
    s = pd.Series([3,4,5,4], index=list('abca'))
    print('Original')
    print(s)
    print('Inverse')
    print(inverse_series(s))

if __name__ == "__main__":
    main()
