#!/usr/bin/python3
""" square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size):
        """ size of square """
        self.integer_validator('size', size)
        self._size = size

    def area(self):
        """ area of square """
        return self._size * self._size

    def __str__(self):
        """ string print square """
        return '[Square] {}/{}'.format(self._size, self._size)
