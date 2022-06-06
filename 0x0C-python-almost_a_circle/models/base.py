#!/usr/bin/python3
"""define base class"""
import json
from os import path


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

        if list_dictionaries is None or list_dictionaries is []:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """from json string"""

        if json_string is None or json_string == []:
            return []

        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """load from file"""

        my_file = cls.__name__ + ".json"
        new_list = []
        if path.exists(my_file):
            with open(my_file, "r", encoding="utf-8") as f:
                new_dict = cls.from_json_string(f.read())
                for inst in new_dict:
                    new_list.append(cls.create(**inst))
                return new_list
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""

        filename = cls.__name__ + ".json"
        my_list = []
        if list_objs is not None:
            for el in list_objs:
                my_list.append(el.to_dictionary())
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(my_list))

    @classmethod
    def create(cls, **dictionary):
        """create instance"""

        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        f = cls.__name__ + ".json"
        lis = []
        if path.exists(f):
            with open(f, "r", encoding="utf-8") as fi:
                new_dict = cls.from_json_string(fi.read())
                for inst in new_dict:
                    lis.append(cls.create(**inst))
                return lis
        else:
            return []

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file"""

        filename = cls.__name__ + ".csv"
        my_list = []
        if list_objs is not None:
            for el in list_objs:
                my_list.append(el.to_dictionary())
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(my_list))
