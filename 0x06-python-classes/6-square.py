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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object.
        Args:
            size (int): Size of a square

            positon (tuple): Position of "my_print" function
            with x, y coordinate
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """tuple: position of the square"""
        return self.__position

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return

        x_axis, y_axis = self.position

        # For y-axis
        #if y_axis <= 1:
        for _ in range(y_axis):
            print()

        # For x-axis
        for _ in range(self.size):
            print((' ' * x_axis) + ('#' * self.size))
