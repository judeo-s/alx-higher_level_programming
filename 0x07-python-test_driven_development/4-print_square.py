#!/usr/bin/python3

"""
A module with a function that prints a square with the character '#'
"""


def print_square(size: "int | float") -> None:
    """
    Prints a square with the character '#'.
    Args:
        size: int/float
    """
    if type(size) not in [float] and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    try:
        size = int(size)
    except Exception as err:
        raise err
    else:
        for _ in range(size):
            print("#" * size)
