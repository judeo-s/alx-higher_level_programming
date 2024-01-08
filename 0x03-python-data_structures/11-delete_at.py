#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    '''
    A function that deletes the item at a specific position in a list

    Args:
        my_list : list
        idx : int
    Returns:
        my_list : my_list
    '''
    length = len(my_list)
    if length > 0:
        if idx >= 0 and idx < length:
            del my_list[idx]
            return my_list
        else:
            return my_list
    else:
        return my_list
