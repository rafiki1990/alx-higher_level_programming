#!/usr/bin/python3
"""
adding two integers
"""


def add_integer(a, b=98):
    """Compute and returns the sum of two numbers

    Args:
        a (integer): A number to be added.
        b (integer): A number to be added.
    Returns:
        integer: a number representing the sum of a and b
    Raises:
        TypeError: if either a or b is not an int or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    else:
        a = int(a)
        b = int(b)
        return a + b
