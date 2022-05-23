#!/usr/bin/python3
"""create a Rectangle class with widht and height attribute"""


class Rectangle:
    """Rectangle class created with width and height
    Attributes:
        number_of_instances (int): shows the number of instances created
        and deleted

        print_symbo (str): characters to print
    """
    number_of_instances = 0
    print_symbol = "#"
    """create a functions for ractengle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """return the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """return perimeter of a rectangle"""
         perimeter = 0
            return perimeter
        perimeter = 2 * self.__width + 2 * self.__height
        return perimeter

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance"""

        return cls(size, size)

    def __str__(self):
        """print a rectangle"""
        pr = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                pr.append(str(self.print_symbol))
            if i < self.height - 1:
                pr.append("\n")
        return "".join(pr)

    def __repr__(self):
        """return the rectangle width and height"""
        return f"Rectangle ({self.__width}, {self.__height})"

    def __del__(self):
        """delete a instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
