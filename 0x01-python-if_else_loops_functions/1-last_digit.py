#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

sign = 1

if number < 0:
    sign = -1

last_dig = (number * sign) % 10

if last_dig == 0:
    comp = "and is 0"
else:
    if last_dig > 5:
        comp = "and is greater than 5"
    elif last_dig < 6:
        comp = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {:s}".format(number, last_dig, comp))
