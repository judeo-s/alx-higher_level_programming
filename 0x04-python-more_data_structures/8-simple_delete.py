#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    '''
    A function that delets a key in a dictionary

    Args:
        a_dictionary : dict
        key : str
    Returns:
        dict
    '''
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
