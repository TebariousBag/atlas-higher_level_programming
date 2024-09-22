#!/usr/bin/python3
""" class base """

class Base:
    """ model base """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            