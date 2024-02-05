#!/usr/bin/python3

'''
A module that contains a template for the BaseGeometry class
'''


class BaseGeometry:
    '''A base class for geometry shapes.'''

    def area(self):
        '''a function that raises an Exception with a message'''
        raise Exception("area() is not implemented")
