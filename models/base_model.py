#!/usr/bin/python3
"""BaseModel Class"""


from datetime import datetime
from uuid import uuid4
from models import storage

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, DateTime


Base = declarative_base()


class BaseModel(Base):
    """
    Base class, BaseModel, defines all basic common public
    instance attributes: id, created_at, updated_at which
    are inherited by other class that extends this base class.
    """
    id = Column(String(60), nullable=False, primary_key=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

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
            self.name = 'No name'

            #: str: id attribute set to str
            self.id = str(uuid4())

            #: datetime: updated_at set to datetime obj
            self.updated_at = datetime.now()

            #: datetime: created_at set to datetime obj
            self.created_at = datetime.now()
            # storage.new(self)

    def save(self) -> None:
        """
        save updates the time on instance modification and save
        an instance object to storage.

        Args:
            Required no parameter.

        Returns:
            None either successful or not.
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self) -> dict:
        """
        to_dict converts class instance to dictionary representation


        Args:
            Required no parameter.

        Returns:
            dict if successful, like::

            {   'id': 'e792-3f34-232-000f',
                'created_at': '2022-08-07T21:05:54.119572',
                'updated_at': '2022-08-07T21:05:56.119241',
                '__class__': 'BaseModel'
            }

        Raises:
            KeyError: dict does not have to_dict.

        """
        new_dict = {}
        for (key, value) in self.__dict__.items():
            if type(value) is datetime:
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def delete(self) -> None:
        storage.delete(self)

    def __str__(self) -> str:
        """Return the string representation of the instance"""
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__
        )
