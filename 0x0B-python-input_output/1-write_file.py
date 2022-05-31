#!/usr/bin/python3
"""write in a file and return the num of char written"""


def write_file(filename="", text=""):
    """
    write in a file and return the num of char written
    Args:
        filename(str): name of the file
        text(str): text to be written to the file
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
