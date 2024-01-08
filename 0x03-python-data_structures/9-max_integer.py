#!/usr/bin/python3

def max_integer(my_list=[]):
    '''
    A function that finds the biggest integer of a list

    Args:
        my_list : list
    Returns:
        max_int : int
            or
        None
    '''
    length = len(my_list)
    if length > 0:
        return sorted(my_list)[-1]
    else:
        return None
