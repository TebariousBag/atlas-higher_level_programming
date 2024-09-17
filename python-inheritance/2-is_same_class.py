#!/usr/bin/python3
""" same object """


def is_same_class(obj, a_class):
    """ check if object is same instance """

    if type(obj) == a_class:
        return True
    return False
