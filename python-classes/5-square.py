#!/usr/bin/python3
"""
This module defines a Square class.

The Square class represents a square with a given size. It includes
methods for setting and retrieving the size, calculating the area,
and printing the square using the `#` character.
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
        size (int): The size of the square. It must be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with a given size.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self._size ** 2

    def my_print(self):
        """
        Prints the square using the `#` character.

        If size is 0, it prints an empty line.
        """
        if self._size == 0:
            print()
        else:
            for _ in range(self._size):
                print("#" * self._size)
