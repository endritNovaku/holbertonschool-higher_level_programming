#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """__init__ - initialize the method
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """return as a string the width and height of the rectangle"""

        return f'[Rectangle] {self.__width}/{self.__height}'
