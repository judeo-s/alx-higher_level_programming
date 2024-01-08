#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''
    A function that replaces an element of a list
    at a specific position without modifying the original list.

    Args:
        my_list : list
    Returns:
        new_list : list
    '''
    new_list = None
    length = len(my_list)
    if length > 0:
        if idx >= 0 and idx < length:
            new_list = [i for i in my_list]
            new_list[idx] = element
            return new_list
        else:
            return my_list
    else:
        return my_list
