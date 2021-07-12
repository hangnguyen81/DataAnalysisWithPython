#!/usr/bin/env python3
def triple(x): 
    #multiplies its parameter by three
    x = x*3
    return x
        
def square(x):
    #raises its parameter to the power of two
    x = x**2
    return x
    
def main():
    for i in range(1,11):
        t = triple(i)
        s = square(i)
        if s>t:
            break
        print('triple({})=={}'.format(i,t),'square({})=={}'.format(i,s))

if __name__ == "__main__":
    main()
