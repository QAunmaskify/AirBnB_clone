#!/usr/bin/python3
"""Review Class"""


from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Review class extend BaseModel (super class)

    Attributes:
        place_id (str): Foreign Key for place id.
        user_id (str): Foreign Key for user.id
        text (str): comment about review
    '''
    place_id = ''
    user_id = ''
    text = ''
