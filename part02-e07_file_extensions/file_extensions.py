#!/usr/bin/env python3
import re
import sys

def file_extensions(filename):
    '''
    Write function file_extensions that gets as a parameter a filename. 
    It should read through the lines from this file. Each line contains a filename. 
    Find the extension for each filename. The function should return a pair, 
    where the first element is a list containing all filenames with no extension 
    (with the preceding period (.) removed).The second element of the pair is a dictionary 
    with extensions as keys and corresponding values are lists with filenames having that extension.
    '''
    with open(filename, 'r') as f:
        lines = f.readlines()

    empty = []
    list_extent = {}
    for line in lines:
        line = line.rstrip()
        regex = r'\w*.(\w*)\Z'
        mo = re.findall(regex, line)
        if mo:
            extentsion = mo[0]
            if extentsion == '':
                empty.append(line)
            elif extentsion in list_extent:
                list_extent[extentsion].append(line)
            else:
                list_extent[extentsion] = [line]

    return (empty, list_extent)

def main():
    filename = sys.path[0] + '/filenames.txt'
    empty, list_extent = file_extensions(filename)
    print(f'{len(empty)} files with no extension')
    for i in sorted(list_extent.keys()):
        print(f'{i} {len(list_extent[i])}')

if __name__ == "__main__":
    main()
