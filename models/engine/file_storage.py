#!/usr/bin/python3
"""FileStorage Class"""


class FileStorage:
    """
    FileStorage uses file_path and objects attributes as follow:

    file_path (private): keeps a reference to JSON file path.

    objects (dict): private class attribute to store all instance_obj.
    """

    __file_path = 'file.json'
    __objects = {}

