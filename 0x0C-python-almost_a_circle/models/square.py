#!/usr/bin/python3
"""Define square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """get size"""

        return self.width

    @size.setter
    def size(self, size):
        """Setter function"""

        self.width = size
        self.height = size

    def __str__(self):
        """str representation of square"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
