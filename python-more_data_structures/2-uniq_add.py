#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_uniq = sum(set(my_list))
    # set creates a list removing duplicates
    # sum adds up the elements of list
    return (sum_uniq)
