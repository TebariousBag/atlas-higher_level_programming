#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv  # get args[]
    total = 0  # holder for total
    
    for arg in args:
        total += int(arg)
    print(f"{total}")
    