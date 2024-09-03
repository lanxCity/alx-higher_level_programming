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

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)
    return a + b
