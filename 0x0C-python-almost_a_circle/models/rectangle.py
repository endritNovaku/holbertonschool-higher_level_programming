#!/usr/bin/python3
"""Define Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""

        return self.__width

    @property
    def height(self):
        """getter for height"""

        return self.__height

    @property
    def x(self):
        """getter for x"""

        return self.__x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """find the area"""

        return self.width * self.height

    def display(self):
        """display rectangle"""

        for i in range(self.y):
            print()
        for j in range(self.height):
            print(' ' * self.x, end="")
            print('#'*self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) \
{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """update Rectangle"""

        count = 0
        for arg in args:
            if count == 0:
                self.id = arg
            if count == 1:
                self.width = arg
            if count == 2:
                self.height = arg
            if count == 3:
                self.x = arg
            if count == 4:
                self.y = arg
            count += 1
