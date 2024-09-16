#!/usr/bin/python3
"""
    A function that prints a text with 2 new lines
"""


def text_indentation(text):
    """
    Args:
        text str: a string of characters

    Returns:
        None
    """
    if type(text) is not str:
        TypeError('text must be a string')

    new_line = True
    line = ''

    for i in range(len(text)):
        char = text[i]

        if char == ' ' and not line:
            char = ''

        line += char

        if char in ['.', '?', ':']:
            line += '\n'
            print(line)

            line = ''
    return
