#!/usr/bin/python3

class BaseGeometry:
    def area(self):
        raise Exception("area() is not initialized")

    def integer_validator(self, name, value):
        self.name = name
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value
