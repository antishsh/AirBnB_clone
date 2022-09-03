#!/usr/bin/python3
"""FileStorage class file."""
import os
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format( type(obj).__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        file = FileStorage.__file_path
        with open(file, mode='w', encoding="utf-8") as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """Deserialize the JSON file to __objects (only if the JSON file (__file_path)."""
        file = FileStorage.__file_path
        if os.path.exists(file):
            with open(file, mode="r", encoding="utf-8") as f:
                pass
