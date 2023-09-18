#!/usr/bin/python3
"""base module"""
import json


class Base:
    """defines Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base class instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of "list_dictionaries"
        """
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of "list_objs" to a file
        """
        data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy_inst = cls(1, 1)
        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """loads dictionaries from a json file,
        creates class instances out of those dicts,
        returns the created instances
        """
        with open(f"{cls.__name__}.json", "r", encoding="utf-8") as f:
            dict_list = cls.from_json_string(f.read())
        return [cls.create(**entry) for entry in dict_list]
