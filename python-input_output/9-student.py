#!/usr/bin/python3
""" student to json """


class Student:
    """ class student """
    def __init__(self, first_name, last_name, age):
        """ values of student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self):
        """ retrieve dict of student """
        return self.__dict__
