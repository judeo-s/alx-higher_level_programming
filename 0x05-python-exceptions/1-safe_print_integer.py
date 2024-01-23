#!/usr/bin/python3

def safe_print_integer(value):
    '''
    A function that prints an integer with "{:d}".format().

    Args:
        value: int
    Returns:
        bool
    '''
    try:
        print("{:d}".format(int(value)))
    except ValueError:
        return False
    return True
