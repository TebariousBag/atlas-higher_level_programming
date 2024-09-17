#!/usr/bin/python3
""" rectangle """


class Rectangle(BaseGeometry):
    """ inherit """

    def __init__(self, width, height):
        """ new rectangle """
        self.integer_validator('width', width)
        self._width = width
        self.integer_validator('height', height)
        self_height = height
