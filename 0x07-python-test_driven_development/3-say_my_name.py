#!/usr/bin/python3
"""
    A function that prints full name
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name str: A string of alphabet
        last_name str: A string of alphabet

    Returns:
        str: the combination of first and last names (full name)
    """

    if not first_name:
        raise TypeError('first_name must be a string')
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    # if first_name.isalpha() and last_name.isalpha():
    print(f'My name is {first_name} {last_name}')
