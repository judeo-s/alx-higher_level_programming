#!/usr/bin/python3

'''
A module with a function that returns the list of attributes
and methods of an object
'''


def lookup(obj):
    '''
    A function tat returns the list of attributes and methods
    of an object.

    Args:
        obj: class
    Returns:
        list
    '''
    return dir(obj)
