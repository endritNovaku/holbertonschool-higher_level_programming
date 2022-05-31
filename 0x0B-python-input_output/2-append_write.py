#!/usr/bin/python3
"""append a text to the end of a file"""


def append_write(filename="", text=""):
    """
    append a text to then end of a file
    Args:
        filename(str): name of the file
        text(str):text to be appendet
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
