#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)  # lenght
    new = ()
    
    if length == 0:  # if length is 0, first char is None
        new = 0, "None"
    else:
        new = length, sentence[0]  # length, char at 0
    return (new)  # lenght, first char
