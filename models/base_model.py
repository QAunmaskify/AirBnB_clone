#!/usr/bin/python3
"""BaseModel Class"""


from datetime import datetime
from uuid import uuid4
from models import storage


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
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        if len(kwargs) > 0:
            for (key, value) in kwargs.items():
                if isinstance(key, datetime):

                    #: str: created_at or updated_at set to datetime str
                    self[key] = datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f'
                    )
                elif key != '__class__':
                    #: str: every other attributes set to str
                    setattr(self, key, value)

        else:
            #: str: id attribute set to str
            self.id = str(uuid4())

            #: datetime: updated_at set to datetime obj
            self.updated_at = datetime.now()

            #: datetime: created_at set to datetime obj
            self.created_at = datetime.now()
            storage.new(self)

    def save(self) -> None:
        """
        save updates the time on instance modification and save
        to storage.

        Args:
            No required parameter.    

        Returns:
            The return value. None
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """
        to_dict converts class instance to dictionary representation


        Args:
            No required parameter.

        Returns:
            dict if successful, None otherwise
        """
        new_dict = {}
        for (key, value) in self.__dict__.items():
            if type(value) is datetime:
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
            new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def __str__(self) -> str:
        """Return the string representation of the instance"""
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__
        )
