#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        """Initialize the instance of class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str definition"""
        clsname = self.__class__.__name__
        return "[{}] ({}) <{}>".format(clsname, self.id, self.__dict__)

    def save(self):
        """save definition"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')

        dict_repr[__class__] = type(self).__name__
        return dict_repr
