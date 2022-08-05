#!/usr/bin/python3
"""FileStorage Class"""
import json


class FileStorage:
    """
    FileStorage uses file_path and objects attributes
    (abstracted data) as follow:

    file_path (private): keeps a reference to JSON file
    path.

    objects (dict): private class attribute to store all
    instance_obj.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns all the contents of objects (private class attribute)
        to any module that requests for it.

        Arg:
            requires no argument
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Stores a new BaseModel instance_obj in class attribute (objects)

        Arg:
            obj (BaseModel instance_obj): pass in BaseModel instance_obj
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes objects (class attribute) and writes the serialized
        data to JSON file accessible through file_path (class attribute)

        Arg:
            requires no argument
        """
        filename = FileStorage.__file_path
        tmp = FileStorage.__objects

        """Converts all instance_obj -> dict_representation of it"""
        for (key, value) in tmp.items():
            FileStorage.__objects[key] = value.to_dict()

        with open(filename, 'w', encoding='utf-8') as w_file:
            str_data = json.dumps(FileStorage.__objects, indent=2)
            w_file.write(str_data)
