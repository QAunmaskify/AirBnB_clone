#!/usr/bin/python3
"""
This module implements the Base class of other modules in
this AirBnB project
"""
import uuid
from datetime import datetime
import json


class BaseModel:
    """
    Base class
    """

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """ Returns the string representation of the class"""
        ret = dict((k, v) for k, v in BaseModel.__dict__.items()\
                if not callable(v) and not k.startswith("__"))
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, ret)

    def save(self):
        """ Updates the modified datetime of the object"""
        self.updated_at = datetime.now()


    def to_dict(self):
        """ Returns a dictionary containing all key/values of the object"""
        result = {}
        for key, value in self.__dict__.items():
            result[key] = value
            if isinstance(value, datetime):
                result[key] = value.isoformat()
        result["__class__"] = self.__class__.__name__
        return result
