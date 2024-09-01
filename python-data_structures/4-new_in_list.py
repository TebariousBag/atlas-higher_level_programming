#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:  # base case
        return (my_list)
    else:
        new = my_list[:]  # create a new copy
        new[idx] = element
        return (new)
