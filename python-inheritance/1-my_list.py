#!/usr/bin/python3
"""Module defining MyList class."""


class MyList(list):
    """Inherits from list and prints the sorted list."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
