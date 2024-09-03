#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    # print value of int
    for int in range(x):
        try:
            print("{:d}".format(int))
            counter += 1
        except (TypeError, ValueError):
        # dont print if value or type error
            pass
    print()
    return (counter)
