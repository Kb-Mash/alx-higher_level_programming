#!/usr/bin/python3
"""a class named Base - will be our superclass"""
import json


class Base:
    """goal of class is to manage id attributes in all subclasses"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize Base instance

        Args:
            id(int, optional)
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            list_dict += [cls.to_dictionary(obj) for obj in list_objs]
        json_string = Base.to_json_string(list_dict)
        with open(filename, "w") as fp:
            fp.write(json_string)

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create an instance with attributes already set"""
        dummy = cls(1, 1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                instances = [cls.create(**data) for data in list_dicts]
                return instances
        except FileNotFoundError:
            return []
