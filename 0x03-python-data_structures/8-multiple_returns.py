#!/usr/bin/python3

def multiple_returns(sentence):
    '''
    a function that returns a tuple with the length of a string
    and its first character.

    Args:
        sentence : str
    Returns:
        length : int
        character : str
    '''
    if sentence:
        return len(sentence), sentence[0]
    else:
        return len(sentence), None
