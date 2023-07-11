#!/usr/bin/python3
matrix = [[1,2,3],[1,2,3]]
def square_matrix_simple(matrix=[]):
    new_matrix = lambda matrix: matrix**2
    return new_matrix
matrix1=square_matrix_simple(matrix)
print(matrix1)
