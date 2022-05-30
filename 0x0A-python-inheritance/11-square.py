#!/usr/bin/python3
"""Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """
        __init__ - inicialize square class
        Args:
            size(int): size of the square
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the square of the area"""

        return self.__size * self.__size

    def __str__(self):
        """Return as a string the width and height of the square"""

        return f'[Square] {self.__size}/{self.__size}'
