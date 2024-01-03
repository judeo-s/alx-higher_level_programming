#!/usr/bin/python3

def remove_char_at(str: str, n: int) -> str:
    """
    a function that creates a copy of the string,
    removing the character at the position n

    Args:
        str: str
        n: int
    Returns:
        new_str: str
    """
    updated_str = ""

    for i in range(len(str)):
        if i == n:
            continue
        new_str += str[i]

    return new_str
