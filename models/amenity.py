#!/usr/bin/python3
"""Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    Amenity class extend BaseModel

    Attributes:
        name (str): label for services enjoy
    '''
    name = ''
