#!/usr/bin/python3
""" write to file """


def write_file(filename="", text=""):
    """ writes text to file and returns 
    number of char written
    """
    with open(filename, 'w+') as f:
        f.write(text)
    return len(text)
