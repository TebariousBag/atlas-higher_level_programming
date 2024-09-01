#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    
    for i in my_list:
        if i % 2 == 0:  # yes divisible by 2
            list.append(True)
        else:  # no, not divisible
            list.append(False)
    return (list)
