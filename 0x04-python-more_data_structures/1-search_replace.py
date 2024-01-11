#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''
    A function that replaces all occurrences of an element by
    another in a new list

    Args:
        my_list : list
        search
        replace
    Returns:
        new_list : list
    '''
    new_list = [i for i in my_list]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
