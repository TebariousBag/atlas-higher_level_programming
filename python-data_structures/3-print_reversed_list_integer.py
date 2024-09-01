#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev = reversed(my_list)  # reverse string

    for i in rev:  # iterate and print
        print("{:d}".format(i))
