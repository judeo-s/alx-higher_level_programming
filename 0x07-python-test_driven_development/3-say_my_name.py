#!/usr/bin/python3

"""A module with a function that prints the first and last name of a person"""


def say_my_name(first_name, last_name=""):
    """
    Prints the first and last name of a person.
    Args:
        first_name: str
        last_name: str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
