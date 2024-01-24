#!/usr/bin/python3

class Square:
    """
    A class for Square
    """

    def __init__(self, size):
        """
        Initializes the Square class

        Args:
            size: (ANY)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self) -> int:
        """
        Returns the area of the square

        Returns:
            int
        """
        return self.__size**2
