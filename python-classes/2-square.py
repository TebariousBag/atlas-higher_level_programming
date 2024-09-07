#!/usr/bin/python3

""" Define a class square """


class Square:
    """ Square """
    def __init__(self, size):
        """ Initialize square
        Arg:
            size: the size of square """
        
        """ isinstance(object, type)
            check if size is not int,
            and check if value less than 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """ its okay to assign value """
        self.__size = size
