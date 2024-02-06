#!/usr/bin/python3

'''A module that writes arguments to a file'''

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    '''
    A function that adds all arguments to a Python list, and then saves
    them to a file
    '''
    temp = []
    items = None
    temp = temp + sys.argv
    try:
        items = load_from_json_file("add_items.json")
    except Exception:
        pass

    if type(items) in [list]:
        for i in temp:
            items.append(i)
    else:
        items = []

    save_to_json_file(items, "add_items.json")


if __name__ == "__main__":
    add_items()
