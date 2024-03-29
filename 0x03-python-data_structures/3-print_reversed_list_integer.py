#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    '''
    A function that prints all integers of a list, in reverse order

    Args:
        my_list : list
    Returns:
        None
    '''
    if not my_list:
        return

    for i in my_list[::-1]:
        print("{:d}".format(i))
