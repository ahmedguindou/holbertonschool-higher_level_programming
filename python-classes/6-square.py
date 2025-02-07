#!/usr/bin/python3
"""
Defines a Square class with size and position attributes.
"""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square.

        Args:
            size (int): Size of the square (default is 0).
            position (tuple): Position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the size with validation.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Gets the position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        """
        Sets the position with validation.

        Raises:
            TypeError: If position is not a tuple of two positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Returns the area of the square."""
        return self._size ** 2

    def my_print(self):
        """Prints the square with `#`, considering position."""
        if self._size == 0:
            print()
            return

        print("\n" * self._position[1], end="")
        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)
