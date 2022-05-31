#!/usr/bin/python3
"""save a json object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """save a json object to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
