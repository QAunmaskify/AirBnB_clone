#!/usr/bin/python3
"""State Class"""


from models.base_model import BaseModel


class State(BaseModel):
    '''
    State class extends BaseModel (super class)


    Attributes:
        name (str): name of a state
    '''
    name = ''
