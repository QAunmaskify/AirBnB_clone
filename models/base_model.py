#!/usr/bin/python3
"""BaseModel Class"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Base class, BaseModel, defines all common public
    instance attributes: id, created_at, updated_at.

    id: assign unique string value when an instance
    is created.

    created_at: assign datetime value on instance creation.

    updated_at: assign datetime value on instance creation
    and modify whenever an instance is updated.
    """
    def __init__(self, *args, **kwargs):
        """__init__ initializes BaseModel instance attributes
        Args:
            args (tuple): set positional parameter(s).
            kwargs (dict): set key/value pair parameter(s)
        """

        """Set the public instance if kwargs is not empty"""
        if len(kwargs) > 0:
            self.my_number = kwargs['my_number']
            self.name = kwargs['name']
            self.created_at = datetime.strptime(
                kwargs['created_at'],
                '%Y-%m-%dT%H:%M:%S.%f'
            )
            self.id = kwargs['id']
            self.updated_at = datetime.strptime(
                kwargs['updated_at'],
                '%Y-%m-%dT%H:%M:%S.%f'
            )
        else:
            """Otherwise, use this default setting"""
            self.id = str(uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()

    def save(self):
        """Update the time on instance modification"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert instance to dictionary"""
        new_dict = {}
        for (key, value) in self.__dict__.items():
            if type(value) is datetime:
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
            new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
