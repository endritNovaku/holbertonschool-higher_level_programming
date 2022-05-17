#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = int(size)

    @property
    def size(self):
        return (self.__size)

    def area(self):
        return (self.__size * self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
