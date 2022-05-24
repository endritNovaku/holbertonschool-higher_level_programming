#!/usr/bin/python3
"""Print square based on length"""


def print_square(size):
    """Prints a square with the character #"""

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for rows in range(size):
        for cols in range(size):
            print("#", end="")
        print("")
