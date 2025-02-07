#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size):
        """Initialize the square with a private instance attribute size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
