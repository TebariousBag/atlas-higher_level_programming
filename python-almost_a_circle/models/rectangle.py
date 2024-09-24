#!/usr/bin/python3
""" class rectangle """
from models.base import Base


class Rectangle(Base):
    """ rectangle from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ print rectangle with # """
        for i in range(self.y):
            print()

        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for k in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ assign arg to each attribute """
        if args:
            for count, i in enumerate(args):
                if count == 0:
                    self.id = i
                elif count == 1:
                    self.width = i
                elif count == 2:
                    self.height = i
                elif count == 3:
                    self.x = i
                elif count == 4:
                    self.y = i
                else:
                    continue
        elif len(kwargs) > 0:
            for k, value in kwargs.items():
                if k == "id":
                    self.id = value
                elif k == "width":
                    self.width = value
                elif k == "height":
                    self.height = value
                elif k == "x":
                    self.x = value
                elif k == "y":
                    self.y = value
                else:
                    continue

    def __str__(self):
        """ return print() and string() of rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
