#!/usr/bin/python3
""" reads text file and prints to stdout """


def read_file(filename=""):
    """ read text file and print """
    with open(filename) as f:
        for line in f:
            print(line, end='')
