#!/usr/bin/python3
# print all possible combos of 2 digits
# first 0-9
for first in range(0, 10):
# second first+1 - 9
    for second in range(first+1, 10):
        if first is 8 and second is 9:
            print(f"{first}{second}")
        else:
            print(f"{first}{second}", end=", ")
