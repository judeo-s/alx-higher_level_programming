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
        num = ord(char)
        print("{:c}".format((num - 32) if num >= 97 and num <= 122 else num),
              end="")
    print()
