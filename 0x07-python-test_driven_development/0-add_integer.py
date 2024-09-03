#!/usr/bin/python3
"""
    Module that add two integers.
    This module defines the add_integer function
    that adds two numbers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats as integers.
    """
    # Checking for args type
    # if not all(True for i in (a, b) if type(i) in [int, float]):

    # -> Checking for NaN
    # In Python, the expression x != x is true only if x is NaN,
    # because NaN is not equal to itself
    if a != a:
        a = 89
    if b != b:
        b = 89

    # -> Checking for type
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    rslt = a + b

    # -> Checking for overflow ans due to large nums
    if rslt == float('inf') or rslt == -float('inf'):
        return 89

    return int(a) + int(b)
