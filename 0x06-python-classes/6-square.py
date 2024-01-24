#!/usr/bin/python3

class Square:
    """
    A class for Square
    """

    def __init__(self, size: int = 0, position: "tuple[int, int]" = (0, 0)):
        """
        Initializes the Square clase

        Args:
            size: int
        """
        self.size = size
        self.position = position

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

    @property
    def position(self) -> "tuple[int, int]":
        """
        Retrieves the 2-tuple containing the coordinates of the square

        Returns:
            tuple[int, int]
        """
        return self.__position

    @position.setter
    def position(self, value: "tuple[int, int]") -> None:
        """
        Sets or updates the coordinate of the square

        Args:
            position (tuple[int, int]): a 2-tuple containing the
            coordinates of the square

        Raise:
            TypeError: when the argument received is not a 2-tuple or if any of
            the values in the 2-tuple is not an integer
        """
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if sum(1 for i in value if isinstance(i, int) and i >= 0) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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
