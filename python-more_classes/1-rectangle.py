#!/usr/bin/python3
""" Define a Rectangle class """


class Rectangle:
    """ Rectangle """
    pass
    
    def __init__(self, width=0, height=0):
        """ initialize rectangle 
    Args:
        width (int): width
        height (int): height
        """
    self.width = width
    self.height = height

    @property
    def width(self):
        """ get width """
        return self.width
    
    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """ get height """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ set height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
