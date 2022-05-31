#!/usr/bin/python3
"""Defina a Student class"""
import json


class Student:
    """create a student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary of the class"""

        d = vars(self)
        newDict = {}
        if type(attrs) == list:
            for key in d:
                if key in attrs:
                    newDict[key] = d[key]
            return newDict
        return d

    def reload_from_json(self, json):
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
