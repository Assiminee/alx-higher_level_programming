#!/usr/bin/python3
""" pascal_triangle module
"""


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    pascal_t = []
    if n > 0:
        for i in range(1, 3):
            pascal_t.append([1] * i)
            if n < 2:
                return pascal_t
        i = 1
        while i < n - 1:
            j = 1
            pascal_n = [1]
            while j < len(pascal_t[i]):
                pascal_n.append(pascal_t[i][j - 1] + pascal_t[i][j])
                j += 1
            pascal_n.append(1)
            pascal_t.append(pascal_n)
            i += 1
    return pascal_t
