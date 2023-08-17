#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda l: [l[0] ** 2, l[1] ** 2, l[2] **2], matrix))
