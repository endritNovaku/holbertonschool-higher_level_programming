#!/usr/bin/python3
"""Define Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """
        __init - inicialize square class
        Args:
            size(int): size of the square
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the square"""

        return self.__size * self.__size
