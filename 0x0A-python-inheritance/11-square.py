#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Square class"""


class Square(Rectangle):
    """init method"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    """area method"""
    def area(self):
        return self.__size * self.__size

    """str method"""
    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
