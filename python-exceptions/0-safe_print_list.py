#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    # in range of x
    for counter in range(x):
        try:
            # print element of list
            print(f"{my_list[counter]}")
            counter += 1
            # increase counter
        except IndexError:
            # if encountering an error break
            break
        print()
        return (counter)
