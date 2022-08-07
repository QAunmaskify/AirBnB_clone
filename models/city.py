#!/usr/bin/python3
"""City class"""


from models.base_model import BaseModel


class City(BaseModel):
    '''
    City class extends BaseModel

    Arg:
        BaseModel - super class
    '''
    state_id = ''
    name = ''
