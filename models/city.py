#!/usr/bin/python3
"""City class"""


from models.base_model import BaseModel


class City(BaseModel):
    '''
    City class extends BaseModel (super class)


    Attributes:
        state_id (str): a chosen state.
        name: name of a state.
    '''
    state_id = ''
    name = ''
