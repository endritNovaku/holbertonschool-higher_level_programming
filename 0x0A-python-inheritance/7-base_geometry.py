#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """area function"""

    def area(self):
        """raise an Exception error"""
        raise Exception("area() is not initialized")
    """define integer_validator function"""

    def integer_validator(self, name, value):
        """check if a value is int or not"""
        self.name = name
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value
