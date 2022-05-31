#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """Read a file:
        Args:
            filename(str): name of the file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
