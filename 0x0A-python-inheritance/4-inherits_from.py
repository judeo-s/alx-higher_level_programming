#!/usr/bin/python3

"""
A module with a function that returns True if an object is an
instance of a class that inherits from the specified class.
"""


def inherits_from(obj, a_class):
    '''
    A function that returs True if the object is an instance of a class
    that inherited (directly or indrectly) from the specifired class;
    otherwise False.

    Args:
        obj: class
        a_class: class
    Returns:
        bool
    '''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
