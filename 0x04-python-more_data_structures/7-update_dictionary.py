#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    '''
    A function that replaces or adds key/value in a dictionary

    Args:
        a_dictionary : dict
        key
        value
    Returns:
        new_dict : dict
    '''
    new_dict = a_dictionary
    new_dict[key] = value
    return new_dict
