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
        self.__width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y
    
    @width.setter
    def y(self, value):
        self._y = value
        