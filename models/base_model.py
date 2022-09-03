#!/usr/bin/python3
"""Base class file."""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize the instance of class."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    self.__dict__[key] = value
                if "created_at" in kwargs.keys():
                    self.created_at = datetime.strptime(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
                if "updated_at" in kwargs.keys():
                    self.updated_at = datetime.strptime(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Str definition."""
        clsname = self.__class__.__name__
        return "[{}] ({}) <{}>".format(clsname, self.id, self.__dict__)

    def save(self):
        """Save definition."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance."""
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')

        dict_repr[__class__] = type(self).__name__
        return dict_repr
