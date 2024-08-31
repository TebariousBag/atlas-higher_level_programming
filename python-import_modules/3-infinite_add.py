#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv  # get args[]
    total = 0  # holder for total

    if len(args) > 1:  # if more than 1 arg
        for arg in args:
            if arg != args[0]:  # need to skip past name
                total += int(arg)
    print(f"{total}")
