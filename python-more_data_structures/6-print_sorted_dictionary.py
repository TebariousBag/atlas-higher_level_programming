#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted = list(a_dictionary.keys())
    # get list of keys
    sorted.sort()
    # sort them
    for key in sorted:
        print("{}: {}".format(key, a_dictionary[key]))
        # print top level key, then lower key
