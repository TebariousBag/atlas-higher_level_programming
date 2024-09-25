#!/usr/bin/python3
""" class base """
import json

class Base:
    """ model base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        tojson = json.dumps(list_dictionaries)
        return tojson
