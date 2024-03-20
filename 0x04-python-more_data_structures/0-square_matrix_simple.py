#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cpy = matrix[:]
    counter = 0
    for row in matrix:
        matrix_cpy[counter] = list(map((lambda x: x * x), row))
        counter += 1
    return matrix_cpy
