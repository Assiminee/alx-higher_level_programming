#!/usr/bin/python3
for i in range(100):
    sep = ", "

    prefix = ""

    if i < 10:
        prefix = "0"

    if i == 99:
        sep = "\n"

    print("{:s}{:d}".format(prefix, i), end=sep)
