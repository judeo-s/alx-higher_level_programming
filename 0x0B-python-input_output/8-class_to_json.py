#!/usr/bin/python3

'''A module for converting class to json'''


def class_to_json(obj):
    '''
    A function that returns the dictionary description with simple data
    structure for JSON serialization of an object

    Args:
        obj: class
    Returns:
        dict
    '''
    return obj.__dict__
