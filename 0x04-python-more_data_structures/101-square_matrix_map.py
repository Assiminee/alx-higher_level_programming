#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_list = list(map(lambda l: list(map(lambda x: x**2, l)), matrix))
    return new_list
