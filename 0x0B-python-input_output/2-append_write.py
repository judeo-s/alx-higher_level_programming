#!/usr/bin/python3


'''A module that has function to appends texts to a  file'''


def append_write(filename="", text=""):
    '''
    A function that appends a string at the end of a text file and returns
    the number of characters added.

    Args:
        filename: str
    '''
    if filename == "" or text == "":
        return 0

    with open(filename, 'a') as file:
        return file.write(text)
