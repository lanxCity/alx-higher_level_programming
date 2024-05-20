#!/usr/bin/python3
""" Intro to python object oriented programming """


class Square:
    """
    A class representing a square shape.

    This class provides a blueprint for creating square objects.
    Squares are geometric shapes with four equal sides
    and four right angles.

    Attributes:
        _size (int): Size of a square
    """

    def __init__(self, size):
        """
        Initializes a new Square object.
        Args:
            size (int): Size of a square
        """
        self.__size = size
