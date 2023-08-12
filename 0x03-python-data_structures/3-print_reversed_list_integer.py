#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print()
        return None
    i = -1
    while i >= -1 * len(my_list):
        print("{:d}".format(my_list[i]))
        i -= 1
