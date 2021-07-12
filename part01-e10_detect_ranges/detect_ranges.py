#!/usr/bin/env python3

def detect_ranges(L):
	input_list = sorted(set(L))
	detect_list = []
	temp = []
	i = 0
	while input_list:
		if len(input_list) == 1:
			detect_list.append(input_list[0])
			input_list.pop(0)
		elif (i < len(input_list)-1) and (input_list[i+1] == input_list[i]+1):
			temp.append(input_list[i])
			i = i + 1
		elif len(temp) == 0:
			detect_list.append(input_list[i])
			input_list.pop(i)
			i = 0
		else: 
			temp.append(input_list[i])
			detect_temp =(temp[0],temp[-1]+1)
			temp=[]
			detect_list.append(detect_temp)
			del input_list[:i+1]
			i=0

	return detect_list


def main():
    L = [11, 2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
