#!/usr/bin/python3

"""
Define a class square
"""


class Square:
    """
    Square
    """
    def __init__(self, size=0, position=(0,0)):
        """ Initialize square
        Arg:
            size: the size of square """
        self._size = size
        self._position = position
    """ retrieve size """
    @property
    def size(self):
        """ size of square """
        return (self._size)
    """ set the size here """
    @size.setter
    def size(self, value):
        """ isinstance(object, type) check if value is not int,
        and check if value less than 0"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        """ its okay to assign value """
        self._size = value

    @property
    def area(self):
        """ Return area of square, size * size. Public Instance """
        return (self._size * self._size)
    
    @property
    def position(self):
        """ get position """
        return (self._position)

    @position.setter
    def position(self, value):
        """ set position of square """
        self._position = value
        
    def my_print(self):
        """ print square of # """
        for row in range(self._size):
            for col in range(self._size):
                print("#", end="")
            print()
        if self._size == 0:
            print("")
