#!/usr/bin/python3
"""
Function that searches for the peak element in
a list of integers
"""


def find_peak(int_list):
    """ Returns peak value of list of unsorted integers
    """
    if not int_list:
        return None
    left = 0
    right = len(int_list) - 1
    while left < right:
        mid = (left + right) // 2
        if int_list[mid] >= int_list[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return int_list[left]
