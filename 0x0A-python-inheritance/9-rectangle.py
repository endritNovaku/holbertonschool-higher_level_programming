#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Rectangle class"""


class Rectangle(BaseGeometry):
    """init method"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """area method"""
    def area(self):
        return self.__width * self.__height

    """str method"""
    def __str__(self):
        return f'[Rectangle] {self.__width}/{self.__height}'
