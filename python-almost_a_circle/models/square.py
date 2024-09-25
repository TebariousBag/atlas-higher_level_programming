#!/usr/bin/python3
""" class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ square constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter size square """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assign args to sttributes """
        if args:
            for count, i in enumerate(args):
                if count == 0:
                    self.id = i
                if count == 1:
                    self.size = i
                if count == 2:
                    self.x = i
                if count == 3:
                    self.y = i
                else:
                    continue

        elif len(kwargs) > 0:
            for k, value in kwargs.items():
                if k == "id":
                    self.id = value
                if k == "size":
                    self.width = value
                    self.height = value
                elif k == "x":
                    self.x = value
                elif k == "y":
                    self.y = value
                else:
                    continue

    def to_json_string(list_dictionaries):
        """ return json """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        tojson = json.dumps(list_dictionaries)
        return tojson

    def __str__(self):
        """ str represtation """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height)

    def to_dictionary(self):
        """return dict of square"""
        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y
        return dict
