#!/usr/bin/python3
""" same class or inherit from """


def is_kind_of_class(obj, a_class):
    """ is instance """

    if isinstance(obj, a_class):
        return True
    return False
