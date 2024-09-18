#!/usr/bin/python3
""" create obj file from json file """
import json


def load_from_json_file(filename):
    """ create obj from file """
    with open(filename) as f:
        return json.load(f)
