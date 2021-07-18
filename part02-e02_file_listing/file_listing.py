#!/usr/bin/env python3

import re
import sys
#-rwxr-xr-x 1 jttoivon hyad-all    2356 Dec 11 11:50 add_colab_link.py

def file_listing(filename="src/listing.txt"):
    result = []
    with open(filename,'r') as f:
        for line in f:
            regex = r'(\d+)\s+([A-Za-z]{3})\s+(\d+)\s+(\d{2}):(\d{2})\s+(.+)'
            found_str = re.findall(regex,line)
            temp = (int(found_str[0][0]),found_str[0][1],int(found_str[0][2]),int(found_str[0][3]),int(found_str[0][4]),found_str[0][5])
            result.append(temp)
    return result

def main():
    filename = sys.path[0] + '/listing.txt'
    print(file_listing(filename))

if __name__ == "__main__":
    main()
