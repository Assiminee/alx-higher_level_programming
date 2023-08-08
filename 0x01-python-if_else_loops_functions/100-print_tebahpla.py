#!/usr/bin/python3
i = 122
while (i >= 97):
    step = 32
    if i % 2 == 0:
        step = 0
    print("{:s}".format(chr(i - step)), end="")
    i -= 1
