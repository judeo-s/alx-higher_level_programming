#!/usr/bin/python3

def best_score(a_dictionary):
    '''
    A function that returns a key with the biggest integer value

    Args:
        a_dictionary : dict
    Returns:
        max_score : str
    '''
    if not a_dictionary:
        return None

    max_score = list(a_dictionary.keys())[0]

    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary[max_score]:
            max_score = key

    return max_score
