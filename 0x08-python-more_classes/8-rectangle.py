#!/usr/bin/python3

"""A module that models a Rectangle"""


class Rectangle:
    """
    A class for Rectangles
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object

        Args:
            width (int, optional)
            height (int, optional)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                string += str(Rectangle.print_symbol)
            if i != self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """
        Returns a string representing the rectangle

        Return:
            str
        """
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """Prints message after a Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(
        rect_1: "Rectangle", rect_2: "Rectangle"
    ) -> "Rectangle":
        """
        Returns the biggest rectangle based on the area.

        Args:
            rect_1
            rect_2

        Raises:
            TypeError

        Returns:
            Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1

        return max((rect_1, rect_2), key=lambda rect: rect.area())
