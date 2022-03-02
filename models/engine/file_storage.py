#!/usr/bin/env python3

import json
from models.base_model import BaseModel
from datetime import datetime

class FileStorage:
    """ Class that serializes instances to a JSON
    file and deserializes JSON files to instances"""
    
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {} # emptydict

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        # First, get the object's class name followed bi "." and
        # the id of the object. 
        # ex: to store a BaseModel object with id=12121212,
        #  the key will be BaseModel.12121212)

        key = obj.__class__.__name__ +"."+ obj.id
        self.__objects[key] = obj
        # Finally, it stores the object "obj" in self.__objects, at
        # key previously generated. 



    def save(self):
        """  serializes __objects to the JSON file (path: __file_path)"""
        
        
        #  For some reason this returns: 
        # TypeError: Object of type BaseModel is not JSON serializable


        #print(self.__objects)
        #for key in self.__objects:
        #    if key == "created_at" or key == "updated_at":
        #        self.__objects[key] = self.__objects[key].isoformat()
        #        print(f"{key} : {self.__objects[key]}")
        # json.dumps(self.__objects, indent=4, sort_keys=True, default=str)
        new_dict = {}
        with open(self.__file_path, "a", encoding='utf-8') as f: 
            for obj in self.__objects.values():
                key = obj.__class__.__name__ +"."+ obj.id
                new_dict[key] = obj.to_dict()

                json.dump(new_dict, f)
            # f.write(json.dumps(self.__objects))
            # The issue is that json.dump cant serialize a datetime object
            # that easily. It needs a way to represent it as a string. 
            # this solution almost works, but there is an extra pair of 
            # quotes at the end of the cat file.json ; echo ""
            
    def reload(self):
        """ deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists 
        otherwise, do nothing. If the file doesn
        t exist, no exception should be raised)"""

        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                return json.load(f)


          
        except:
            pass # If the file doesnt exist, no exception should be raised)



