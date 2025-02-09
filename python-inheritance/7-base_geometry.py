#!/usr/bin/python3
"""Define a class BaseGeometry with area and integer_validator methods."""


class BaseGeometry:
    """Class with methods area and integer_validator."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
