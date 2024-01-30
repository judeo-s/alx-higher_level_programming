#!/usr/bin/python3

"""
Module with a function that adds two numbers. It checks the arguments given.
as operands before trying to add them. An exception is raised when an error
is encountered. These exception includes TypeError when a/b is not an int.
"""


def add_integer(a, b=98):
    """A function that adds two integers
    Args: int
    Returns: int"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
