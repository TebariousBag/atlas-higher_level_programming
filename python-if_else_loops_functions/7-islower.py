#!/usr/bin/python3
def islower(c):
    lower = ord(c)
    # checks if character is lowercase a-z
    if lower in range(97, 123):
        return True
    else:
        return False
