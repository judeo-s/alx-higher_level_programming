#!/usr/bin/python3

class Square:
    """
    A class for Square
    """

    def __init__(self, size: int = 0):
        """
        Initializes the Square clase

        Args:
            size: int
        """
        self.size = size

    @property
    def size(self, size):
        """
        Updates the size of the square

        Args:
            size: (ANY)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @size.setter
    def size(self) -> int:
        """
        Retrieves the size of the square

        Returns:
            int: the size of the square
        """
        return self.__size

    def area(self) -> int:
        """
        Returns the area of the square

        Returns:
            int
        """
        return self.__size**2

    def my_print(self) -> None:
        """
        Prints the representation of the square using hashes '#'
        """
        if self.__size == 0:
            print()

        for _ in range(self.__size):
            print("#" * self.__size)
