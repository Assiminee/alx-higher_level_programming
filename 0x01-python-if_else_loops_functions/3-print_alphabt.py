#!/usr/bin/python3
for i in range(97, 123):
    c = chr(i)
    if c == "q" or c == "e":
        continue
    print("{:s}".format(c), end="")
