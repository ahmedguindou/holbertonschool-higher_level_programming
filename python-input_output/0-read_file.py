#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read file"""
    with open(filename, 'r') as f:
        print(f.read(), end="")
