#!/usr/bin/python3

"""
A Amenity definition that inherits from BaseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ a class definition of Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ amenity instantiation"""
        super().__init__(*args, **kwargs)
