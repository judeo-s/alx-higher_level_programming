#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    '''
    A function that prints the first x elements of a list and only integers.

    Args:
        my_list: list
        x: int
    Returns:
        count: int
    '''
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count = count + 1
        except (IndexError, ValueError, TypeError):
            pass
    print()
    return count
