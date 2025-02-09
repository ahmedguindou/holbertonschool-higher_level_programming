#!/usr/bin/python3
"""Define a class BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Class with an unimplemented area method."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
