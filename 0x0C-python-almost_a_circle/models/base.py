#!/usr/bin/python3
"""define base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return dictionaries to json string"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""

        new_cvs = []
        new_file = cls.__name__ + ".csv"
        if new_file is not None:
            for i in list_objs:
                new_cvs.append(i.to_dictionary())
        with open(new_file, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(new_list_csv))

    @classmethod
    def load_from_file_csv(cls):
        """list of instances"""

        csv_file = cls.__name__ + ".csv"
        if path.exists(csv_file):
            with open(csv_file, "r", encoding="utf-8") as file:
                csv_dict = cls.from_json_string(file.read())
                csv_list = [cls.create(**csv_inst) for csv_inst in csv_dict]
                return csv_list
        else:
            return []
