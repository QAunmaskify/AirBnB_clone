#!/usr/bin/python3
"""
File Storage Module
"""
import os
import json


class FileStorage:
    """
    Class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns all objects as dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """ Set in the objects dictionary a new object with a given key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.__dict__

    def save(self):
        """Saves the serialized objects to file"""
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(FileStorage.__objects, indent=2, default=str))

    def reload(self):
        """ Retrieves and deserialize JSON file to object if path exists"""
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
            try:
                data = json.loads(f.read())
                for key, value in data.items():
                    FileStorage.__objects[key] = value
            except:
                pass
