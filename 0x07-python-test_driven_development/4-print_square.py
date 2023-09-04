#!/usr/bin/python3
"""4-print_square module."""


def print_square(size):
    """
    Print a square with the character '#'.

    Args:
        size (int): The side length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.

    Returns:
        None
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print('#' * size)
