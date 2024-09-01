#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:  # if list empty
        return (None)
    my_list.sort()  # sorts in ascending order
    return (my_list[-1])  # return the last, which is now the largest
