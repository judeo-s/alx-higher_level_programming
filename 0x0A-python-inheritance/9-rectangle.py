#!/usr/bin/python3

'''
A module that contains a template for the BaseGeometry class
'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''A class than models a rectangle.'''

    def __init__(self, width, height):
        '''
        A contructor function for the Rectangle class

        Args:
            width: int
            height: int
        '''
        self.integer_validator(None, width)
        self.integer_validator(None, height)
        self.__width = width
        self.__height = height

    def __str__(self):
        '''
        A function that returns a custom string

        Returns:
            str
        '''
        return f'[{type(self).__name__}] {self.__width}/{self.__height}'

    def area(self):
        '''
        A function that returns the area of a Rectangle

        Returns:
            int
        '''
        return self.__width * self.__height
