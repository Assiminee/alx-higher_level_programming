#!/usr/bin/python3
import dis
def uppercase(str):
    for i in range(len(str)):
        step = 32

        if not 97 <= ord(str[i]) <= 122:
            step = 0

        print("{:s}".format(chr(ord(str[i]) - step)), end="")
    print()
dis.dis(uppercase)
