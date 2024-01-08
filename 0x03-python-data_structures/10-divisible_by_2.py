#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    '''
    A function that finds all multiples of 2 in a list

    Args:
        my_list : list
    Returns:
        list
    '''
    length = len(my_list)
    if length > 0:
        new_list = []
        for i in my_list:
            new_list.append(True if i % 2 == 0 else False)
        return new_list
    else:
        return []
