#!/usr/bin/python3
"""Serialization and deserialization JSON types of file storage"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Custom class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):

        return self.__objects

    def new(self, object):
        
        self.__objects[object.__class__.__name__ + '.' + str(object)] = object

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """
        with open(self.__file_path, 'w+') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()
                       }, f)

    def reload(self):
        """Deserialization of the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
