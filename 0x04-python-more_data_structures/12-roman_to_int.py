#!/usr/bin/python3

def roman_to_int(roman_string):
    '''
    A function that converts a roman numeral to an integer

    Args:
        roman_string : str
    Returns:
        int
    '''
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    return sum(-roman_map[c] if i < len(roman_string) - 1 and
               roman_map[c] < roman_map[roman_string[i + 1]]
               else roman_map[c] for i, c in enumerate(roman_string))
