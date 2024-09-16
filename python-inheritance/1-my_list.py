#!/usr/bin/python3
""" class that inherits from list """


class Mylist(list):
    """ prints int list sorted """
    def print_sorted(self):
        """ print in ascending order """
        print(sorted(self))
