#!/usr/bin/python3
""" student to json """


class Student:
    """ class student """
    def __init__(self, first_name, last_name, age):
        """ values of student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieve dict of student
        if sttrs is a list of strings only retrieve those
        """
        if attrs is None:
            return self.__dict__
        else:
            dict = {}
            for i in attrs:
                if i in self.__dict__.keys():
                    dict[i] = self.__dict__[i]
            return dict

    def reload_from_json(self, json):
        """ attr of json to self """
        for keys, values in json.items():
            setattr(self, keys, values)
