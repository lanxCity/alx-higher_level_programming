#!/usr/bin/python3
""" Intro to python object oriented programming """


class Square:
    """
    A class representing a square shape.

    This class provides a blueprint for creating square objects.
    Squares are geometric shapes with four equal sides
    and four right angles.

    Attributes:
        __size (int): Size of a square
        __position ()
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object.
        Args:
            size (int): Size of a square

            positon (tuple): Position of "my_print" function
            with x, y coordinate
        """
        # -> Size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        # Position
        if not isinstance(position, tuple) or len(position) != 2 \
                or min(position) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    # Getter and setter for size
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

    # Getter and setter for position
    @property
    def position(self):
        """ tuple: position of the square """
        return self.__position

    @position.setter
    def position(self, value):

        if isinstance(value, tuple) and len(value) == 2:
            if min(value) >= 0:
                self.__position = value
                return

        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return

        x_axis, y_axis = self.position

        # For y-axis
        # if y_axis <= 1:
        for _ in range(y_axis):
            print()

        # For x-axis
        for _ in range(self.size):
            print((' ' * x_axis) + ('#' * self.size))
