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
        if value not int:
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
        if value not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
