#!/usr/bin/python3
"""
This module implements the Base class of other modules in
this AirBnB project
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class
    """

    def __init__(self, *args, **kwargs):
        """ Initializaton """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Returns the string representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Updates the modified datetime of the object"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all key/values of the object"""
        result = {}
        for key, value in self.__dict__.items():
            result[key] = value
            if isinstance(value, datetime):
                result[key] = value.isoformat()
        result["__class__"] = self.__class__.__name__
        return result
