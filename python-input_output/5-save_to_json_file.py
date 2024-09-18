#!/usr/bin/python3
""" save to json file """
import json


def save_to_json_file(my_obj, filename):
    """ write obj to text file """
    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
