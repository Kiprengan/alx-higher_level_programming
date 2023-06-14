#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtrix = []
    for m in matrix:
        new_matrix.append([k ** 2 for k in m])
    return new_matrix
