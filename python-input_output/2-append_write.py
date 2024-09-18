#!/usr/bin/python3
""" append to file """


def append_write(filename="", text=""):
    """ append string at EoF """
    with open(filename, 'a+') as f:
        f.write(text)
    return len(text)
