#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value) -> bool:
    '''
    A function that safely prints an integer

    Args:
        value: any
    Returns:
        bool
    '''
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        stderr.write(f"Exception: {err}\n")
        return False

    return True
