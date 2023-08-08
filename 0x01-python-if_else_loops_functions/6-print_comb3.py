#!/usr/bin/python3
for i in range(10):
    sep = ", "

    for j in range(10):
        if i == 8:
            sep = "\n"

        if i > j or i == j:
            continue
        print("{:d}{:d}".format(i, j), end=sep)
