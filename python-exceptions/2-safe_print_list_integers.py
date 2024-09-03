#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    # print value of int
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]))
            counter += 1
        except (TypeError, ValueError):
        # dont print if value or type error
            continue
    print()
        # newline
    return (counter)