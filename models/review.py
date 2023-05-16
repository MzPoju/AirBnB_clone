#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Attributes:
        user_id (str)
        place_id (str)
        text
    """
    user_id = ""
    place_id = ""
    text = ""
