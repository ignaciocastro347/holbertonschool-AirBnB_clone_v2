#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv

class State(BaseModel, Base):
    """ State class """
    
    # file ? for FileStorage or db for DBStorage
    if getenv("HBNB_TYPE_STORAGE") == "db":
        from sqlalchemy import Column, String
        from sqlalchemy.orm import relationship
        
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    elif getenv("HBNB_TYPE_STORAGE") == "file":
        # TODO: try it with FileStorage
        name = ""
        cities = []

        @property
        def cities(self):  # cities is a getter atribute
            from models.__init__ import storage
            from models.city import City

            cities_list = []
            for key, val in storage.all(City).items():
                if val["state_id"] == self.id:
                    cities_list.append(val)
            return cities_list