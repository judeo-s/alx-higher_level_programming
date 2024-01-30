#!/usr/bin/python3

"""
A module with a function that divides all elements of a matrix.
It checks the arguments being passed the function.
It also raises exceptions to handle errors.
"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix.
    Args: list and int
    Returns: list"""

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) not in [list]:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    row_size = len(matrix[0])
    for i in range(len(matrix)):
        if row_size != len(matrix[i]):
            raise TypeError(
                    "Each row of the matrix must have the same size"
                    )

        if type(matrix[i]) not in [list]:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(
                        "matrix must be a matrix "
                        "(list of lists) of integers/floats"
                    )
    return list(
        map(lambda row: list(map(lambda x: round(x / div, 2), row)), matrix)
    )
