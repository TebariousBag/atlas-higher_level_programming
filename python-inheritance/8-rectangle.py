#!/usr/bin/python3
""" rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherit """

    def __init__(self, width, height):
        """ new rectangle """
        self.integer_validator('width', width)
        self._width = width
        self.integer_validator('height', height)
        self_height = height
