#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv  # get args[]
    total = 0  # holder for total
    
    if len(arg) > 1:
        for num in range(arg):
            total += int(num)
    print(f"{total}")
    