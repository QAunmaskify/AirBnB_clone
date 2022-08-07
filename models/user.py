#!/usr/bin/python3
"""User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class extends BaseModel (super class)

    Args:
        BaseModel: super class inherited
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
