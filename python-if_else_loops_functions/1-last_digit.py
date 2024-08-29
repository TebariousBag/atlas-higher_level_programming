#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = "and is greater than 5"
str3 = "and is 0"
str4 = "and is less than 6 and not 0"
# need to get last digit
if number >= 0:
    lastdigit = number % 10
# negative last digit
else:
    lastdigit = number % (-10)
if lastdigit == 0:
    print(f'{str1} {number} is {lastdigit} {str3}')
elif lastdigit > 5:
    print(f'{str1} {number} is {lastdigit} {str2}')
elif lastdigit < 6 != 0:
    print(f'{str1} {number} is {lastdigit} {str4}')
