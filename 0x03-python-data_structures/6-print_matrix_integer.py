#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix and matrix[i]:
                print("{:d}".format(matrix[i][j]), end="")

                if j < (len(matrix[i]) - 1):
                    print("", end=" ")
                else:
                    print("")

                if (i == len(matrix) - 1) and j == (len(matrix[i]) - 1):
                    return
    print("")
    return
