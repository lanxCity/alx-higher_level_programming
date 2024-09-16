#!/usr/bin/python3
"""
    A function that prints a text with 2 new lines
"""


def text_indentation(text):
    """
    Args:
        text str: a string of characters

    Returns:

    """
    if type(text) is not str:
        TypeError('text must be a string')

    new_line = True
    for i in text:
        print(i if new_line and i != ' ' else '',
              end='')
        new_line = False

        if i in '.?:':
            print('\n')
            new_line = True
