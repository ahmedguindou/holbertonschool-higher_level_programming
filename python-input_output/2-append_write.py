#!/usr/bin/python3
"""append file"""


def append_write(filename="", text=""):
    """append file"""
    with open(filename, 'a') as f:
        return f.write(text)
