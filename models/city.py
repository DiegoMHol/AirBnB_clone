#!/usr/bin/python3
"""
A City definition that inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """ a class definition of City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ cit instantiation"""
        super().__init__(*args, **kwargs)
