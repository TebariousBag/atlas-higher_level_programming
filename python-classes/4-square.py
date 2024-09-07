#!/usr/bin/python3

""" Define a class square """


class Square:
    """ Square """
    def __init__(self, size=0):
        """ Initialize square
        Arg:
            size: the size of square """
        self.__size = size
    """ retrieve size """
    @property
    def size(self):
        """ size of square """
        return (self.__size)
    """ set the size here """
    @size.setter
    def size(self, value):
        """ isinstance(object, type) check if value is not int,
        and check if value less than 0"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        """ its okay to assign value """
        self.size = value
        
    def area(self):
        """ Return area of square, size * size. Public Instance """
        return (self.__size * self.__size)
