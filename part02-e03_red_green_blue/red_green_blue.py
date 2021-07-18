#!/usr/bin/env python3

import re
import sys

def red_green_blue(filename="src/rgb.txt"):
    with open(filename,'r') as f:
        lines = f.readlines()
    del lines[0]
    result = []
    for line in lines:
        regex = r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)'
        found = re.findall(regex,line)
        temp = []
        for i in range(0,4):
            temp.append(found[0][i])
        string = '\t'.join(temp)
        result.append(string)
    return result


def main():
    filename = sys.path[0]+'/rgb.txt'
    print(red_green_blue(filename))

if __name__ == "__main__":
    main()
