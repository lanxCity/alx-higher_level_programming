#!/usr/bin/python3
"""
    Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    # -> Type error
    if (
            # Empty matrix
            not matrix or
            # check rows data types
            (not all(isinstance(row, list) for row in matrix)) or
            # check empty rows
            (not all([True if row else False for row in matrix][:])) or
            # Check cols data type
            (not all([True if type(col) in [int, float] else False
                      for row in matrix for col in row][:]))
    ):
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')

    # -> Rows lengths
    rows_lengths = [len(row) for row in matrix]
    min_len, max_len = (min(rows_lengths), max(rows_lengths))
    if min_len != max_len:
        raise TypeError('Each row of the matrix must have the same size')

    # -> div data type
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    # -> non-zero div
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # Answer
    ans = list(map(lambda row:
                   list(map(lambda col: round(col / div, 2), row)),
                   matrix))
    return ans
