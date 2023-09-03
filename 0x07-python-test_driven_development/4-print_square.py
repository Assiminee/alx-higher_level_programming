#!/usr/bin/python3
"""
4-print_square module
"""


def print_square(size):
    """
    prints a square with the character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
