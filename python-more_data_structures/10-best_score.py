#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        score = max(a_dictionary, key=a_dictionary.get)
        return (score)
    # get the key from adict that is max value
    return (None)
