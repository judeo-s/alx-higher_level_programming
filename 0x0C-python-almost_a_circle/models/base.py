#!/usr/bin/python3

'''A module used to act as a base for other modules'''


class Base:
    '''A base class for other classes'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        A constructor function for the Base class

        Args:
            id: int
        '''
        self.id = None

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
