#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    # new dict
    for int in a_dictionary:
        # multiply each int by 2 and add to new
        new[int] = a_dictionary[int] * 2
    return (new)
