#!/usr/bin/python3

'''A module with a function to read objects from a file'''


import json


def load_from_json_file(filename):
    '''
    A function that creates an object from a JSON file

    Args:
        filename: str
    '''
    if filename is None or filename == '':
        return None

    with open(filename, 'r') as file:
        return json.loads(file.read())
