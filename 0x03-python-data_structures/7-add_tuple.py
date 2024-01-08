#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    '''
    A function that adds 2 tuples

    Args:
        tuple_a : tuple
        tuple_b : tuple
    Returns:
        tuple
    '''
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
