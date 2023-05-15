#!/usr/bin/python3
"""Place class"""
from models.base_model import BaseModel

class Place(BaseModel):
    """
    Attributes:
        amenity_ids (list)
        city_id (str) 
        latitude (float)
        user_id (str): User id
        max_guest (int)
        name
        description
        number_rooms
        number_bathrooms
        max_guest (int)
        price_by_night
        longitude     
    """

    amenity_ids = []
    number_bathrooms = 0
    city_id = ""
    latitude = 0.0
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    longitude = 0.0
