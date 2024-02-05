#!/usr/bin/python3

'''
A module that contains a template for the BaseGeometry class
'''


class BaseGeometry:
    '''A base class for geometry shapes.'''

    def area(self):
        '''a function that raises an Exception with a message'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        A function that validates the value argument.

        Args:
            name: str
            value: int
        Raises:
            TypeError & ValueError
        '''
        if type(value) not in [int]:
            raise TypeError("{} must be an integer".format(value))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
