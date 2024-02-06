#!/usr/bin/python3

''' A module that has a function that returns a json format of an object '''


import json


def to_json_string(my_obj):
    '''
    A function that returns the JSON representation of an object (string)

    Args:
        my_obj: class
    Returns:
        str
    '''
    return json.dumps(my_obj)
