#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = set_1.symmetric_difference(set_2)
    # create  new set with elements not in both
    return (diff)
