#!/usr/bin/python3
""" from json string to obj """
import json


def from_json_string(my_str):
    """ return obj represented by json string """
    return json.loads(my_str)
