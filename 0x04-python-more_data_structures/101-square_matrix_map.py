#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda num: num**2, row)), matrix))
    # The first map takes a row out of the matrix variable and passes it
    # to the next map. The nested map then extracts each element of the
    # row passed to it, squares it, then returns it to the outer map to create
    # a matrix with each element squared
