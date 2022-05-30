#!/usr/bin/python3
"""create a MyList"""


class MyList(list):
    """print a sorted list"""

    def print_sorted(self):
        """print sorted list"""

        print(sorted(self))
