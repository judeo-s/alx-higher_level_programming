#!/usr/bin/python3

'''
A module that contains a function that checks if a specific
instance is of a particular class
'''


def is_kind_of_class(obj, a_class):
    '''
    A function that returns True if the object is an isntance of, or if
    the object is an instance of a class that inherited from, the specific
    class; otherwise False

    Args:
        obj: class
        a_class: class
    Returns:
        bool
    '''
    return isinstance(obj, a_class)
