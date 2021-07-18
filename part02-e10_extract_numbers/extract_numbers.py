#!/usr/bin/env python3

def extract_numbers(s):
    '''
    Write a function extract_numbers that gets a string as a parameter. 
    It should return a list of numbers that can be both ints and floats. 
    Split the string to words at whitespace using the split() method. 
    Then iterate through each word, and initially try to convert to an int. 
    If unsuccesful, then try to convert to a float. If not a number then skip the word.
    '''
    words = s.split()
    list_number = []
    for w in words:
        try:
            x = int(w)
            list_number.append(x)
        except: 
            try:
                x = float(w)
                list_number.append(x)
            except:
                continue
    return list_number
    '''
    # model solution
    def extract_numbers(s):
    result=[]
    for word in s.split():
        try:
            result.append(int(word))
        except ValueError:
            try:
                result.append(float(word))
            except ValueError:
                pass
    return result
    '''

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
