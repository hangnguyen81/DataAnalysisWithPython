#!/usr/bin/env python3


def integers_in_brackets(s):
    #finds from a given string all integers that are enclosed in brackets.
  
    import re
    regex = r'\[\s*([+-]?\d+)\s*\]'
    result = list(map(int,re.findall(regex,s)))
    return result

def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
