#!/usr/bin/python3
"""Square class inheriting from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that represents a square"""

    def __init__(self, size):
        """Initialize with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return square description"""
        return f"[Square] {self.__size}/{self.__size}"
