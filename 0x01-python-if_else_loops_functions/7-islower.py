#!/usr/bin/python3

def islower(c: str) -> bool:
    '''
    A function that checks for lowercase character (c).

    Args:
        c:str
    Returns:
        bool
    '''
    num = ord(c)
    if num >= 97 and num <= 122:
        return True
    else:
        return False
