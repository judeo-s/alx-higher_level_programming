#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''
    A function that prints x elements of a list.

    Args:
        my_list: list
        x: int
    Returs:
        count: int
    '''
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count = count + 1
        except IndexError:
            pass
    print()
    return count
