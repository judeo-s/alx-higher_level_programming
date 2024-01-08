#!/usr/bin/python3

def no_c(my_string):
    '''
    A function that removes all characters "c" and "C" from a string

    Args:
        my_string : str
    Return:
        new_string : str
    '''
    temp1 = ""
    new_string = ""

    for i in my_string.split("C"):
        temp1 = temp1 + i

    for i in temp1.split("c"):
        new_string = new_string + i
    return new_string
