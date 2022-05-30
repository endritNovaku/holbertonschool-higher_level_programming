#!/usr/bin/python3
"""create a MyList"""

class MyList(list):
    def print_sorted(self):
        print(sorted(self))
