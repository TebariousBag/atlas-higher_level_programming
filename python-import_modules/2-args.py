#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    
    numargs = len(sys.argv) - 1  # get length of args minus name

    if numargs == 0:  # base case for zero args
        print("0 arguments,")
    elif numargs == 1:  # special case for 1 arg
        print("1 argument:")
    else:
        print(f"{numargs} arguments:")
    for num in range(numargs):
        print(f"{num + 1}: {sys.argv[num + 1]}")  # have to add 1 since it starts at 0
