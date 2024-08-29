#!/usr/bin/python3
# print all possible combos of 2 digits
for first in range(0, 10):
    for second in range(first+1, 10):
        if first == 8 and second == 9:
            print("{}{}".format(first, second))
        else:
            print("{}{}".format(first, second), end=", ")
