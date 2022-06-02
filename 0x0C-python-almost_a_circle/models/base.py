#!/usr/bin/python3
"""define base class"""


class Base:
    """base class"""
    __nb_object = 0

    def __init__(self, id=None):
        """init"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
