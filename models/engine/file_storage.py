#!/usr/bin/python3
"""FileStorage class file."""
import json
import os
import models.base_model


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file."""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialize the instance of class."""
        super().__init__()

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def reset(self):
        """Clear data on __object (cache)."""
        self.__objects.clear()

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        if obj is not None:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        file = FileStorage.__file_path

        with open(file, mode='w', encoding="utf-8") as f:
            f.write(
                json.dumps(
                    FileStorage.__objects,
                    cls=models.base_model.BaseModelEncoder))

    def reload(self):
        """Deserialize the JSON file to __objects."""
        file = FileStorage.__file_path
        if not os.path.exists(file):
            return
        try:
            with open(file, mode="r+", encoding="utf-8") as f:
                file_string = f.read()
                data = json.loads(file_string)
                for object_key, model_data in data.items():
                    model_name, model_id = object_key.split('.')
                    model = models.classes[model_name](**model_data)
                    self.new(model)

        except Exception as e:
            print(e)
