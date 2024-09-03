#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # takes lambda func to multiply x
    # map applies to each element
    # then makes a list
    multiplied = (list(map(lambda x: x * number, my_list)))
    return (multiplied)
