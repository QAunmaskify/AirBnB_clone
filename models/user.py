#!/usr/bin/python3
"""User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class extends BaseModel (super class)


    Attributes:
        email (str): user's contact email.
        password (str): user's login password.
        first_name (str): user's first name.
        last_name (str): user's last name.

    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
