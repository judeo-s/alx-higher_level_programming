#!/usr/bin/python3

"""A module that models a Rectangle"""


class Rectangle:
    """
    A class for Rectangles
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object

        Args:
            width (int, optional)
            height (int, optional)
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        Returns a string which represents the rectangle with the character #

        Return:
            string: str
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i != self.__height - 1:
                string += '\n'
        return string

    @property
    def width(self):
        """
        Returns the width of a Rectangle object.

        Returns:
            int
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of width of a Rectangle object.

        Args:
            value: int
        Raises:
            TypeError, ValueError
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of a Rectangle object.

        Returns:
            int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of the height of a Rectangle object.

        Args:
            value: int
        Raises:
            TypeError, ValueError
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of Rectangle object.

        Returns:
            int
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of a Rectangle object.

        Returns:
            int
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
