#!/usr/bin/python3
def uppercase(str):
    sep = ""
    for i in range(len(str)):
        if i == len(str) - 1:
            sep = "\n"
        if not 97 <= ord(str[i]) <= 122:
            print("{:s}".format(str[i]), end=sep)
        else:
            print("{:s}".format(chr(ord(str[i]) - 32)), end=sep)
