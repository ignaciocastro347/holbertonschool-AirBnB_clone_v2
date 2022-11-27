#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv
from sqlalchemy import Column, String

class State(BaseModel, Base):
    """ State class """
    
    # file ? for FileStorage or db for DBStorage
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        from sqlalchemy.orm import relationship
        cities = relationship("City", backref="state", cascade="all, delete")

    else:

        @property
        def cities(self):
            from models.__init__ import storage
            from models.city import City

            cities_list = []
            for key, val in storage.all(City).items():
                if val["state_id"] == self.id:
                    cities_list.append(val)
            return cities_list