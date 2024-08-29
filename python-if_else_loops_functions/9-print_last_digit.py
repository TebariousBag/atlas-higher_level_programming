#!/usr/bin/python3
def print_last_digit(number):
    print(abs(number) % 10, end="")  # print last digit without newline
    return (abs(number) % 10)  # return the last one
