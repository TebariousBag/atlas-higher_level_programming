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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs """
        filename = cls.__name__ + '.json'
        list_of_dicts = []
        if list_objs is not None:
            for item in list_objs:
                list_of_dicts.append(cls.to_dictionary(item))
        jsonstr = cls.to_json_string(list_of_dicts)
        with open(filename, 'w') as f:
            f.write(jsonstr)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        tojson = json.dumps(list_dictionaries)
        return tojson
