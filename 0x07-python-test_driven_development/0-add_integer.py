#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Add two numbers
    Args:
        a (int, float): The first number, which can be an integer or a float.
        b (int, float): The first number, which can be an integer or a float.

    Returns:
        int, float: The sum of a and b.

    """
    # Checking for args type
    # if not all(True for i in (a, b) if type(i) in [int, float]):

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)
    return a + b







