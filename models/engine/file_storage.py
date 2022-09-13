#!/usr/bin/python3
"""FileStorage Class"""
import json


class FileStorage:
    """
    FileStorage abstracts file_path and objects attributes
    for caching data and processing it.

    """

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None) -> dict:
        """
        Returns all stored objects (dictionary representation)
        of BaseModel instance_obj to any module that requests for
        it.

        Arg:
            requires no argument

        Returns:
            dict

        """
        f_list = {}
        if cls is not None:
            for (key, value) in FileStorage.__objects.items():
                if isinstance(value, cls):
                    f_list[key] = value

        return f_list

    def new(self, obj):
        """
        Stores a new BaseModel instance_obj in class attribute (objects)
        Arg:
            obj (instance_obj): pass in class instance_obj

        Returns:
            None
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self) -> None:
        """
        Serializes dictionary representation of a class and writes it as
        'string data' to JSON file accessible through file_path.

        However, it converts all class instance objects to its dictionary
        representation i.e: instance_obj -> dict_representation.

        Examples:
            <class 'BaseModel'>  ==>>  <class 'dict'>

        Arg:
            Requires no argument.

        Returns:
            None

        """

        filename = FileStorage.__file_path
        tmp_store = {}

        for (key, value) in FileStorage.__objects.items():
            tmp_store[key] = value.to_dict()

        with open(filename, 'w', encoding='utf-8') as w_file:
            str_data = json.dumps(tmp_store, indent=2)
            w_file.write(str_data)

    def reload(self) -> None:
        """
        Deserializes the content of JSON file back to the structure of
        objects (dictionary). Then converts the contents of the dictionary
        to supported class instance_obj based on each class type.

        Examples:
            <class 'dict'>  ==>  <class 'instance_obj'>

        Arg:
            Requires no argument.

        Returns:
            None

        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.state import State
        filename = FileStorage.__file_path

        try:
            with open(filename, 'r', encoding='utf-8') as r_file:
                str_data = r_file.read()
                dict_data = json.loads(str_data)

                tmp = {}

                for (key, value) in dict_data.items():
                    type_of_class = key.split('.')[0]

                    if type_of_class == 'BaseModel':
                        tmp[key] = BaseModel(**value)
                    elif type_of_class == 'User':
                        tmp[key] = User(**value)
                    elif type_of_class == 'State':
                        tmp[key] = State(**value)
                    elif type_of_class == 'City':
                        tmp[key] = City(**value)
                    elif type_of_class == 'Amenity':
                        tmp[key] = Amenity(**value)
                    elif type_of_class == 'Place':
                        tmp[key] = Place(**value)
                    elif type_of_class == 'Review':
                        tmp[key] = Review(**value)

                FileStorage.__objects = tmp
        except IOError:
            pass

    def update(self, obj_name, obj_id, attr, value):
        key = obj_name + '.' + obj_id
        setattr(FileStorage.__objects[key], attr, value)

    def destroy(self, obj_name, obj_id):
        key = obj_name + '.' + obj_id
        del (FileStorage.__objects[key])

    def delete(self, obj=None):
        if obj is not None:
            for (key, value) in FileStorage.__objects.items():
                if value is obj:
                    del (FileStorage.__objects[key])
                    break
