#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''
    A function that prints a dictionary by ordered keys

    Args:
        a_dictionary : dict
    Returns:
        dict
    '''
    sort = dict([(i, a_dictionary[i]) for i in sorted(a_dictionary)])
    for key in sort.keys():
        print("{}: {}".format(key, sort.get(key)))
