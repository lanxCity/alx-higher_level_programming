#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        # new_matrix.ppend([])
        new_matrix[len(new_matrix):] = [[]]

        for j in range(len(matrix[i])):
            sqr_el = matrix[i][j] * matrix[i][j]
            # new_matrix[i].append(sqr_el)
            new_matrix[i][len(new_matrix[i]):] = [sqr_el]
    return new_matrix
