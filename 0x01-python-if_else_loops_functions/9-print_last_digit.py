#!/usr/bin/python3

def print_last_digit(number) -> int:
    '''
    A function that prints the last digit of a number

    Args:
        number:int
    Returns:
        int
    '''
    last_digit = (abs(number) % 10)
    print("{:d}".format(last_digit), end="")
    return last_digit
