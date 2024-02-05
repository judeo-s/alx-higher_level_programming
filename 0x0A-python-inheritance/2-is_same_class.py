#!/usr/bin/python3

'''
A module that contains a function that checks if a specific
instance is of a particular class
'''


def is_same_class(obj, a_class):
    '''
    A function that returns True if the object is exactly an instance
    of the specified

    Args:
        obj: class
        a_class: class
    Returns:
        bool
    '''
    return type(obj) is a_class
