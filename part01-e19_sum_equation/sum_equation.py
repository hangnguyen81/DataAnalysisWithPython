#!/usr/bin/env python3

def sum_equation(L):    
    if (L == []):
        result = "0 = 0"
    else:
        sum = 0
        for l in L:
            sum = sum + l      
        new_list = [str(l) for l in L]
        result = " + ".join(new_list)
        result = result + " = " + str(sum)
    return result

def main():
    L = [1,5,7]
    #L=[]
    print(sum_equation(L))

if __name__ == "__main__":
    main()
