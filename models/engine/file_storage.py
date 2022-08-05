#!/usr/bin/python3
"""FileStorage Class"""


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
            self (BaseModel object instance): pass in BaseModel instance
            obj
        """
        return FileStorage.__objects
        """
