#!/usr/bin/python3


'''A module that has function to read and print a content of a file'''


def read_file(filename=""):
    '''
    A function that reads a text file (utf8) and prints it to stdout

    Args:
        filename: str
    '''
    with open(filename, 'r') as file:
        print(file.read(), end="")
