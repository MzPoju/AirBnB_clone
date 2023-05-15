#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Attributes:
        email : usermail
        password : userpasswd
        first_name : firstname
        last_name : lastname
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
