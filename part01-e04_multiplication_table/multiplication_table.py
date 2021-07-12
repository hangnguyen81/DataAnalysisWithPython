#!/usr/bin/env python3


def main():
    """
    for i in range(1,11):
        print('\n{:4}'.format(i), end='')
        j = i + 1
        for j in range(2,11):
            print('{:4}'.format(i*j), end='')
    """
    #model solution
    for r in range(1, 11):
        for c in range(1, 11):
            print(f"{r*c:4d}", end="")
            #print('{:4d}'.format(r*c), end="")
        print()  

if __name__ == "__main__":
    main()
