#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cpy = matrix[:]
    counter = 0

    for row in matrix_cpy:
        matrix_cpy[counter] = list(map((lambda x: x * x), row))
        counter += 1

    return matrix_cpy

    '''
    for i in range(len(matrix_cpy)):
        new_matrix[len(new_matrix):] = [[]]

        for j in range(len(matrix_cpy[i])):
            sqr_el = matrix_cpy[i][j] * matrix_cpy[i][j]
            new_matrix[i][len(new_matrix[i]):] = [sqr_el]
    return new_matrix
    '''
