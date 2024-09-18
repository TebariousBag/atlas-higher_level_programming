#!/usr/bin/python3
""" class to json """


def class_to_json(obj):
    """ serialize """
    return obj.__dict__
