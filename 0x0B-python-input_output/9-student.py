#!/usr/bin/python3
"""Defina a Student class"""


class Student:
    """create a student class"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary of the class"""

        return vars(self)
