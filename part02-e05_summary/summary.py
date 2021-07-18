#!/usr/bin/env python3

import re
import sys
import math

def summary(filename):
    with open (filename, 'r') as f:
        lines = f.readlines()
    
    list_number = []
    for line in lines:
        try:
            number = float(line.rstrip())
            list_number.append(number)
        except:
            pass
  
    # calculate sum
    total = sum(list_number)   
    # average
    n = len(list_number)
    avg = total/n
    # standard deviation
    temp = [(i - avg)**2 for i in list_number]
    std = math.sqrt(sum(temp)/(n-1))
    
    return (total,avg,std)    
 

def main():

    for i in sys.argv[1:]:
        sum, avg, std = summary(i)
        print(f"File: {i} Sum: {sum:.6f} Average: {avg:.6f} Stddev: {std:.6f}")

    # run in command line
    # python src/summary.py src/example.txt src/example2.txt src/example3.txt
if __name__ == "__main__":
    main()
