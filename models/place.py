#!/usr/bin/python3
"""Place class"""


from models.base_model import BaseModel


class Place(BaseModel):
    '''
    Place class extends BaseModel (super class)


    Attributes:
        city_id (str): stores city unique number, FK.
        user_id (str): holds user unique number, FK.
        name (str): name of a place.
        description (str): information about a place.
        number_rooms (int): number of rooms in a place.
        number_bathrooms (int): no. of bathroom of a place.
        max_guest (int): place capacity.
        price_by_night (int): price for night services.
        latitude (float): latitude point.
        longitude (float): longitudinal point.
        amenity_ids (:obj: list of :obj: str): stores list of amenity ids
    '''
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
