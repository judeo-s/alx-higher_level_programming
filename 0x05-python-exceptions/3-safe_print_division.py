#!/usr/bin/python3


def safe_print_division(a, b):
    '''
    A function that divides 2 integers and prints the result.

    Args:
        a: int
        b: int
    Returns:
        c: float
    '''
    c = None
    try:
        c = a / b
        return c
    except (ZeroDivisionError, TypeError, ValueError):
        return None
    finally:
        print("Inside result: {}".format(c))
