#!/usr/bin/python3

"""
A module with a function that adds an attribute to an object much like
the built-in `setattr()` function
"""


def add_attribute(obj, attribute_name, attribute_value):
    '''
    A function that adds a new attribute to an object if it’s possible

    Args:
        obj: class
        attribute_name: str
        attribute_value: str
    Raises:
        TypeError
    '''
    if not (
        hasattr(obj, "__dict__")
        or (
            hasattr(type(obj), "__slots__")
            and attribute_name in type(obj).__slots__
        )
    ):
        raise TypeError("can't add new attribute")

    obj.__dict__[attribute_name] = attribute_value
