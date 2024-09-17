#!/usr/bin/python3
""" Integer Validator """


#!/usr/bin/python3
""" improve geometry """


class BaseGeometry:
    """ raise exception with message """

    def area(self):
        """ exception with message """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validate value """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
