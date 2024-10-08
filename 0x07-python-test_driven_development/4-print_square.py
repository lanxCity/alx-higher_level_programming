#!/usr/bin/python3
"""
    A function that prints a square with the character #
"""


def print_square(size):
    """
    Args:
        size int:  the size length of the square

    Returns:
        None
    """

    if ((isinstance(size, float) and size < 0) or
            type(size) is not int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for row in range(size):
        print('#' * size)

    return
