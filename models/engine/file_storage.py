#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models
        currently in storage"""
        print_dict = {}
        if cls:
            className = cls.__name__
            for key, val in FileStorage.__objects.items():
                if key.split(".")[0] == className:
                    print_dict[key] = val
            return print_dict
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj:
            id = obj.to_dict()["id"]
            className = obj.to_dict()["__class__"]
            keyname = className + "." + id
            if keyname in FileStorage.__objects:
                del FileStorage.__objects[keyname]
                self.save()

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()



    def get(self, cls, id):
        """retrive class from db by its id"""
        if cls and id:
            targetObject = "{}.{}".format(cls, id)
            all_obj = self.all(cls)
            return all_obj.get(targetObject)
        return None

    def count(self, cls=None):
        """ count all objects in storage"""
        return (len(self.all(cls)))