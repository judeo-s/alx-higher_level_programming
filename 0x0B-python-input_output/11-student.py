#!/usr/bin/python3

"""A module that models a Student object."""


class Student:
    """Models a Student object."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes and creates a new Student object.

        Args:
            first_name: str
            last_name: str
            age: int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        Returns the dictionary representation of the Student object.

        Args:
            attr: list
        Returns:
            JSON
        """
        if attr is not None and isinstance(attr, list):
            return (
                {
                    key: value for key, value in self.__dict__.items()
                    if key in attr
                }
            )
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of a `Student` instance with contents in a
        JSON file.

        Args:
            json: dict
        """
        for key, value in json.items():
            self.__dict__[key] = value
