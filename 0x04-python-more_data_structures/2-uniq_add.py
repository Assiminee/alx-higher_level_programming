#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        total = 0
        unique = set(my_list)
        for num in unique:
            total += num
        return total
