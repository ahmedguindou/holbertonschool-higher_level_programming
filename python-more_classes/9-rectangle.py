#!/usr/bin/python3
"""
    A class to represent a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (str): The symbol used for string representation.
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (str): The symbol used for string representation.
"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle with width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter (2 * (width + height)).

        If width or height is 0, the perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of
        the rectangle using `print_symbol` characters.

        Returns:
            str: The rectangle as a string.

        If width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join([
            str(self.print_symbol) * self.width for _ in range(self.height)
        ])

    def __repr__(self):
        """
        Returns a string to recreate the rectangle.

        Returns:
            str: A string like 'Rectangle(width, height)'.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a message when the rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the areas of two rectangles
        and returns the one with the biggest area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the biggest area.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new square Rectangle instance where width == height.

        Args:
            size (int): The size of the square sides (default is 0).

        Returns:
            Rectangle: A new Rectangle with equal width and height (size).
        """
        return cls(size, size)
