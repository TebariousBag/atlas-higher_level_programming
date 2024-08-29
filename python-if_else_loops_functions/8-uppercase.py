#!/usr/bin/python3
def uppercase(str):
    newstr = ""  # create empty string
    for letter in str:
        upper = ord(letter)  # turn numeric
        upper = upper - 32  # turn to upper
        if letter >= 'a' and letter <= 'z':
            newstr = newstr + chr(upper)  # add the eppercase character
        else:
            newstr = newstr + letter  # add letter to string
    print("{}".format(newstr))  # print string
