#!/usr/bin/python3
"""compare 2 clasess"""


class Square:
    """initialize size"""
    def __init__(self, size=0):
        self.__size = int(size)

    """return size"""
    @property
    def size(self):
        return (self.__size)

    """find root sqr"""
    def area(self):
        return (self.__size * self.__size)

    """add a value"""
    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    """define the behavior for equal operator"""
    def __eq__(self, other):
        return (self.area() == other.area())

    """define the behavior for not equal operator"""
    def __ne__(self, other):
        return (self.area() != other.area())

    """define the behavior for less then operator"""
    def __lt__(self, other):
        return (self.area() < other.area())

    """define the behavior for greater than operator"""
    def __gt__(self, other):
        return (self.area() > other.area())

    """define the behavior for less or equal operator"""
    def __le__(self, other):
        return (self.area() <= other.area())

    """define the behavior for greater or equal operator"""
    def __ge__(self, other):
        return (self.area() >= other.area())
