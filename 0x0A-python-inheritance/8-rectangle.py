#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Define Retangle class"""


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """init function"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
