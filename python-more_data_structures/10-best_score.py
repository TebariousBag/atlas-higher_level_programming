#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = max(a_dictionary, key=a_dictionary.get)
    if a_dictionary:
        return (max_value)
    # get the key from adict that is max value
    return (None)
