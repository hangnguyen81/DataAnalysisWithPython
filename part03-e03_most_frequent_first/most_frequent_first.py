#!/usr/bin/env python3
'''
Write function most_frequent_first that gets a two dimensional array and an index c of a column as parameters. 
The function should then return the array whose rows are sorted based on column c, in the following way. 
Rows are ordered so that those rows with the most frequent element in column c come first, 
then come the rows with the second most frequent element in column c, and so on. 
Therefore, the values outside column c don’t affect the ordering in any way.
'''
import numpy as np
'''
def most_frequent_first(a, c):
    unique_in_c = a[:,c]
    values, counts = np.unique(unique_in_c, return_counts=True)
    dict_ = dict(zip(values,counts))
    # sort the number has the most frequent first
    dict_ = sorted(dict_.items(), key=lambda x: x[1], reverse=True )
    sorted_values = [i[0] for i in dict_]
    result = []
    for i in sorted_values:
        for j in a:
            if i == j[c]:
                result.append(j)
    return np.array(result)

'''
#model solution
def most_frequent_first(a, c):
    b = a[:,c]   # get column c
    _,s,t = np.unique(b, return_inverse=True, return_counts=True)
    idx = np.argsort(t[s])
    return t #a[idx][::-1]


def main():
    np.random.seed(0)
    test=np.random.randint(0,10, (10,10))
    print('Original array:\n',test)
    print()
    print('Sorted array:\n',most_frequent_first(test,9))

if __name__ == "__main__":
    main()
