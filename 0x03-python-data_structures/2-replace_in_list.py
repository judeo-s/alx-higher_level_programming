#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    '''
    A function that replaces an element of a list
    at a specific position (like in C).

    Args:
        my_list : str
    Returns:
        None
    '''
    length = len(my_list)
    if length > 0:
        if idx >= 0 and idx < length:
            my_list[idx] = element
            return my_list
        else:
            return my_list
    else:
        return my_list
