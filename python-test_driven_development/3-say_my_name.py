#!/usr/bin/python3
"""
This module provides a function to print name and lastname

Examples:
>>> say_my_name("John", "Smith")
My name is John Smith
>>> say_my_name("Walter", "White")
My name is Walter White
>>> say_my_name("Bob")
My name is Bob
>>> say_my_name(12, "White")
Traceback (most recent call last):
    ...
TypeError: first_name must be a string
>>> say_my_name("John", 123)
Traceback (most recent call last):
    ...
TypeError: last_name must be a string
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first name> <last name>".

    Args:
    first_name (str): The first name.
    last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
    TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
