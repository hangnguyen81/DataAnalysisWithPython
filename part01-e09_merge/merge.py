#!/usr/bin/env python3

def merge(L1, L2):
    list_merge = []
    list_l1l2 = L1 + L2
    while list_l1l2:
        # take the min value of list
        temp = min(list_l1l2)
        # add to new list
        list_merge.append(temp)
        #remove from mergedlist
        list_l1l2.pop(list_l1l2.index(temp))
    return list_merge

    """ model solution
    def merge(L1, L2):
    result = []
    i, j = 0, 0
    # i = j = 0 would also work but leads to bad behaviour with mutable types so not recommended.
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1
    if i < len(L1):
        result.extend(L1[i:])
    else:
        result.extend(L2[j:])
    return result
    """

def main():
    L1 = [1,4,7,8]
    L2 = [3,4,7,9]
    print(merge(L1,L2))

if __name__ == "__main__":
    main()
