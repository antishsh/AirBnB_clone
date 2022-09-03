#!/usr/bin/python3
"""Base class file."""

import uuid
from datetime import datetime
from json import JSONEncoder
import models


class BaseModel:
    """BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize the instance of class."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Save definition."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance."""
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')

        dict_repr[__class__] = type(self).__name__
        return dict_repr

    def __str__(self):
        """Str definition."""
        clName = self.__class__.__name__
        return "[{}] ({}) <{}>".format(clName, self.id, self.__dict__)


class BaseModelEncoder(JSONEncoder):
    """JSON Encoder for BaseModel."""

    def default(self, o):
        """Encode."""
        if isinstance(o, BaseModel):
            return o.to_dict()
        return super().default(o)
