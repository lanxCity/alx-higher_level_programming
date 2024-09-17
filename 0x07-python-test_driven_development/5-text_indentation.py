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
    if not text or not isinstance(text, str):
        raise TypeError('text must be a string')

    line = ''

    for i in range(len(text)):
        char = text[i]

        if (not line or line[-1] == '\n') and char == ' ':
            continue

        line += char

        if char in ['.', '?', ':']:
            line += '\n\n'

    print(line, end='')

    return
