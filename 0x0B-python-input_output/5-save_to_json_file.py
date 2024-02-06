#!/usr/bin/python3

'''A module with a function to write objects to a file'''


import json


def save_to_json_file(my_obj, filename):
    '''
    A function that writes an object to a text file using JSON representation

    Args:
        my_obj: class
        filename: str
    '''
    if my_obj is None or filename is None or filename == '':
        return

    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
