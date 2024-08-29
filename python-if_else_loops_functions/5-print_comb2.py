#!/usr/bin/python3
# numbers from 0-99
for num in range(0, 100):
    if num is 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=", ")
