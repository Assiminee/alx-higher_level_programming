#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        sep = " "
        for i in range(len(row)):
            if i == len(row) - 1:
                sep = "\n"
            print("{:d}".format(row[i]), end=sep)
