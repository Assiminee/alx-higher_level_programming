#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    if my_list:
        unique = set(my_list)
        for num in unique:
            total += num
    return total
