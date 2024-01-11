#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''
    A function that returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary : dict
    Returns:
        dict
    '''
    new_dict = {
            key: value * 2
            for key, value in a_dictionary.items()
            if isinstance(value, int)
        }
    return new_dict
