#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    print('The hypotenuse:',triangle.hypothenuse(4,5))
    print('The area: ',triangle.area(4,5))

if __name__ == "__main__":
    main()