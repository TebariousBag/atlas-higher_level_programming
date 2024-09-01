#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) -1:  #if neg or out of range return og
        return (my_list)
    else:
        my_list[idx] = element  # replace element at idx
        return (my_list)
