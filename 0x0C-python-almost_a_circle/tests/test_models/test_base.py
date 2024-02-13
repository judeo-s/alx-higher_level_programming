#!/usr/bin/python3

'''A model that is used to test the Base classo'''


import json
import inspect
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestDocumentation(unittest.TestCase):
    """Tests the documentation for modules, classes and methods."""

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up class method for the doc tests.
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring_exists(self):
        """
        Tests if module docstring documentation exists.
        """
        self.assertIsNotNone(Base.__doc__)

    def test_classes_docstring_exists(self):
        """
        Tests if class docstring documentation exists.
        """
        self.assertIsNotNone(Base.__doc__.__class__)

    def test_methods_docstring_exists(self):
        """
        Tests if methods docstring documentation exists
        """
        for _, method in self.setup:
            self.assertIsNotNone(method.__doc__)


class TestBase(unittest.TestCase):
    '''A class dedicated to testing the Base class'''

    def test_initialization(self):
        '''Tests the initialization of the Base class'''
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(12)
        self.b4 = Base()
        self.b5 = Base(42)

        self.assertEquals(self.b1.id, 1)
        self.assertEquals(self.b2.id, 2)
        self.assertEquals(self.b4.id, 3)

    def test_manual(self):
        '''Test the auto initialization of the Base class'''
        self.assertEquals(self.b3.id, 12)
        self.assertEquals(self.b5.id, 42)

    def test_json_string(self):
        '''A test to validate the json string of the Base class'''
        r1 = Rectangle(4, 5, 1, 2)
        dictionary = r1.to_dictionary()

        results = Base.to_json_string([dictionary])
        expected = json.dumps([dictionary])
        self.assertEquals(results, expected)

    def test_json_strings(self):
        r1 = Rectangle(4, 5, 1, 2)
        r2 = Rectangle(6, 7, 8, 9)

        dict1 = r1.to_dictionary()
        dict2 = r2.to_dictionary()

        results = Base.to_json_string([dict1, dict2])
        expected = json.dumps([dict1, dict2])
        self.assertEquals(results, expected)

    def test_empty_json_string(self):
        self.assertEquals(Base.to_json_string([]), '[]')
        self.assertEquals(Base.to_json_string(None), '[]')

    def test_invalid_json_string(self) -> None:
        """
        Tests the `to_json_string` static method using invalid arguments of
        pass a list.
        """
        with self.assertRaises(TypeError) as err:
            Base.to_json_string("not list")
            (Base.to_json_string(89))
            Base.to_json_string({"name": "Bob"})

        self.assertEqual(
            err.exception.__str__(),
            "argument should only contain list of dictionaries",
        )

    def test_no_args_json_string(self) -> None:
        exception_msg = (
            "missing 1 required positional argument: 'list_dictionaries'"
        )
        with self.assertRaisesRegex(TypeError, exception_msg):
            Base.to_json_string()

    def test_from_json_to_string_none_arg(self) -> None:
        """Tests for empty lists when None is passed as argument."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list(self) -> None:
        """Tests for when an empty list is passed as argument."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_to_string_non_json_string(self) -> None:
        """Tests encoding errors for non-JSON strings."""
        with self.assertRaises(json.JSONDecodeError):
            Base.from_json_string("Hello")

    def test_from_json_string_integer_arg(self) -> None:
        """Tests for TypeError raised when an integer is passed as argument."""
        with self.assertRaisesRegex(TypeError, "must be a string"):
            Base.from_json_string(87)

    def test_from_json_string_list_arg(self) -> None:
        """Tests for TypeError raised when a list is passed as argument."""
        with self.assertRaisesRegex(TypeError, "must be a string"):
            Base.from_json_string(["Hello"])

    def test_from_json_string_valid_data(self) -> None:
        """Tests for valid data passed to `from_json_string_method`."""
        self.assertEqual(Base.from_json_string('[{"id": 5}]'), [{"id": 5}])
