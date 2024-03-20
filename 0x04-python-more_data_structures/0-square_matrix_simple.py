#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            sqr_el = matrix[i][j] * matrix[i][j]
            new_matrix[i].append(sqr_el)
    return new_matrix
