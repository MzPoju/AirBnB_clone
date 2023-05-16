#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    Attributes:
        state_id : State id.
        name : Name of city
    """

    state_id = ""
    name = ""
