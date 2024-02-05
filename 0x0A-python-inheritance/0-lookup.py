#!/usr/bin/python3


def lookup(obj):
    '''
    A function tat returns the list of attributes and methods
    of an object.

    Args:
        obj: class
    Returns:
        list
    '''
    return sorted(obj().__dir__())
