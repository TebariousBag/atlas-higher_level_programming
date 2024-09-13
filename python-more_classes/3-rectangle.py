#!/usr/bin/python3
""" Define a Rectangle class """


class Rectangle:
    """ Rectangle """

    def __init__(self, width=0, height=0):
        """ initialize rectangle
    Args:
        width (int): width
        height (int): height
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """ get width """
        return self._width

    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """ get height """
        return self._height

    @height.setter
    def height(self, value):
        """ set height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """ are of rectangle """
        return (self._width * self._height)

    def perimeter(self):
        """ perimeter of rectangle """
        if self._width == 0 or self._height == 0:
            return (0)
        return (2*(self._width + self.height))

    def __str__(self):
        """ printable rectangle of # symbols """
        
        rectangle = []
        if self._width is 0 or self.height is 0:
            return ("")
        for i in range(self._height):
            rectangle.apppend("#" * self._width)
        return ("\n".join(rectangle))
        