#!/usr/bin/python3

def print_list_integer(my_list=[]):
    '''
    A function that prints all integers of a list

    Args:
        my_list : list
    Returns:
        None
    '''
    length = len(my_list)
    if length > 0:
        for i in my_list:
            try:
                print("{}".format(i))
            except ValueError:
                print("List must only include integers!")
                break
