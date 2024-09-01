#!/usr/bin/python3
def no_c(my_string):
    new = ""
    c = ""  # saving c's
    for i in my_string:
        if i == 'c' or i == 'C':  # save c's here
            c += i
        else:
            new += i  # str w/o c's
    return (new)
