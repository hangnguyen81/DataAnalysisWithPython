#!/usr/bin/env python3

def reverse_dictionary(d):
    """
    key_list = []
    reverse_dict = {}
 
    # take a list of key for reserve_dict
    for i in d.values():
        for j in i:
            key_list.append(j)

    key_list = list(set(key_list))

    for k in key_list:
        temp = []
        for i,j in d.items():
            if k in j:
                temp.append(i)
            reverse_dict[k] = temp
        
    return reverse_dict
"""
# model solution
    result = {}
    for key, value in d.items():
        for v in value:
            if v in result:
                result[v].append(key)
            else:
                result[v] = [key]
    return result

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(d)
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
