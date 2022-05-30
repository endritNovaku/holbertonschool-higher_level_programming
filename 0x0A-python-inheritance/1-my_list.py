#!/usr/bin/python3
"""Defines a list module"""


class MyList(list):
    """MyList class inheritance of list class"""

    def print_sorted(self):
        """Prints the list, but sorted(ascending sort)"""

        print(sorted(self))
