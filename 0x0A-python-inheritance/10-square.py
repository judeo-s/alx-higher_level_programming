#!/usr/bin/python3


'''
A module contains a class that models a square
'''


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''A class that models a square'''

    def __init__(self, size):
        '''
        A constructor of the Square class to initialize values of the class

        Args:
            size: int
        '''
        self.integer_validator(None, size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''
        A function that calculates the area of a square

        Returns:
            int
        '''
        return self.__size ** 2
