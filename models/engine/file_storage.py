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
        tmp_store = {}

        """
        Converts all BaseModel instance_obj in objects attributes to
        its dictionary representation i.e:

        instance_obj -> dict_representation same as below

        <class 'BaseModel'> -> <class 'dict'>
        """
        for (key, value) in FileStorage.__objects.items():
            tmp_store[key] = value.to_dict()

        with open(filename, 'w', encoding='utf-8') as w_file:
            str_data = json.dumps(tmp_store, indent=2)
            w_file.write(str_data)

    def reload(self):
        """
        Deserializes the content of JSON file back to the structure of
        objects (dictionary). Then converts the contents of the dictionary
        to BaseModel instance_obj i.e:

        <class 'dict'> -> <class 'BaseModel'>

        Arg:
            requires no argument
        """
        from models.base_model import BaseModel
        filename = FileStorage.__file_path

        try:
            with open(filename, 'r', encoding='utf-8') as r_file:
                str_data = r_file.read()
                dict_data = json.loads(str_data)

                """<class 'dict'> -> <class 'BaseModel'>"""
                for (key, value) in dict_data.items():
                    FileStorage.__objects[key] = BaseModel(**value)
        except Exception:
            pass

    def update(self, obj_name, obj_id, attr, value):
        key = obj_name + '.' + obj_id
        setattr(FileStorage.__objects[key], attr, value)

    def destroy(self, obj_name, obj_id):
        key = obj_name + '.' + obj_id
        del (FileStorage.__objects[key])
