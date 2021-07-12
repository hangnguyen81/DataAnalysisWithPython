#!/usr/bin/env python3
# model solution
def sum_equation(L):    
    if not L:
        return "0 = 0"
    else:
        result = list(map(str, L))
    return " + ".join(result) + f" = {sum(L)}"

def main():
    L = [1,5,7]
    print(sum_equation(L))

if __name__ == "__main__":
    main()
