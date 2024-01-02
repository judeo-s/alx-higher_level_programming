#!/usr/bin/python3

def uppercase(str: str):
    '''
    A function that prints a string (str) in uppercase
    followed by a new line

    Args:
        str:str
    Returns:
        None
    '''
    for char in str:
        if "a" <= char <= "z":
            char = ord(char) - 32
        print("{}".format(char), end="")
    print()
