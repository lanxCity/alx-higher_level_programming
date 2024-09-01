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

    def __init__(self, size=0):
        """
        Initializes a new Square object.
        Args:
            size (int): Size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def __repr__(self):
        """ int: size of the square """
        return self.__size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """ int: size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
