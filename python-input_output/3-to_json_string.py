#!/usr/bin/python3
""" function returns json rep of object (string) """
import json


def to_json_string(my_obj):
    """ return JSON rep of my_obj """
    return json.dumps(my_obj)
