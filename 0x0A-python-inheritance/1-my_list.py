#!/usr/bin/python3
"""create a MyList"""

class MyList(list):
    """print a sorted list"""

    def print_sorted(self):
        """
        print_sorted - print sorted list
        Args:
            self: MyList
        """

        print(sorted(self))
