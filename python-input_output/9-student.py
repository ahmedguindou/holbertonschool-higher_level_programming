#!/usr/bin/python3
"""student to json"""


class Student:
    """student to json"""
    def __init__(self, first_name, last_name, age):
        """student to json"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """student to json"""
        return self.__dict__
