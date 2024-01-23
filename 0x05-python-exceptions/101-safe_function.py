#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    '''
    A function that executes a function safely

    Args:
        fct: def
        args: list

    Returns:
        any
    '''
    try:
        return fct(*args)
    except Exception as err:
        stderr.write(f"Exception: {err}\n")
        return None
