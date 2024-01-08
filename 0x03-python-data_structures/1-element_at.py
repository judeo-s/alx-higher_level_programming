#!/usr/bin/python3

def element_at(my_list, idx):
    '''
    A function that retrieves an element from a like in C

    Args:
        my_list : str
    Returns:
        None
    '''
    length = len(my_list)
    if length > 0:
        if idx >= 0 and idx < length:
            return my_list[idx]
        else:
            return None
    else:
        return None
