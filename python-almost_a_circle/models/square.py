#!/usr/bin/python3
""" class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ square constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str represtation """
        return "[Square] ({}) {}/{} - {}".format
        (self.id, self.x, self.y, self.height)
