#!/usr/bin/python3


'''A module that has function to write texts to a  file'''


def write_file(filename="", text=""):
    '''
    A function that wirtes a text to a file and returns the number
    characters written

    Args:
        filename: str
    '''
    if filename == "" or text == "":
        return 0

    with open(filename, 'w') as file:
        return file.write(text)
