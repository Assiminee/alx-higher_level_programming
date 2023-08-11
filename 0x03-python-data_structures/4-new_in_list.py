#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = []
    newList.extend(my_list)
    if 0 < idx < len(my_list):
        newList[idx] = element
    return newList
