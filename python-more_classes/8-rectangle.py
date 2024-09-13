#!/usr/bin/python3
""" Define a Rectangle class """


class Rectangle:
    """ Rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initialize rectangle
    Args:
        width (int): width
        height (int): height
        """
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

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
        rectangle = ""
        if self._width == 0 or self._height == 0:
            return (rectangle)
        for i in range(self._height - 1):
            rectangle += str(self.print_symbol) * self._width + "\n"
        rectangle += str(self.print_symbol) * self._width
        return (rectangle)

    def __repr__(self):
        """ string representation """
        rectangle = ' '
        if self._width == 0 or self._height == 0:
            return (rectangle)
        return (f"Rectangle({self._width}, {self._height})")

    def __del__(self):
        """ prints when deleted """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    def bigger_or_equal(rect_1, rect_2):
        """ bigger or equal """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
