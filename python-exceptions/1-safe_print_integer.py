#!/usr/bin/python3
def safe_print_integer(value):
    # print value of int
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        # dont print if value or type error
        return (False)
