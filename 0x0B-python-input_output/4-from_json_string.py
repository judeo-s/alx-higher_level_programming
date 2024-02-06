#!/usr/bin/python3
import json


''' A module that has a function that returns an object from JSON'''


def from_json_string(my_str):
    '''
    A function that returns an object from a JSON

    Args:
        my_obj: str
    Returns:
        class
    '''
    return json.loads(my_str)
