#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv

class Place(BaseModel, Base):
    """ A place to stay """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        from sqlalchemy import Column, String, Integer, Float, ForeignKey
        from sqlalchemy.orm import relationship

        __tablename__ = "places"
        city_id = Column(String(60),
                         ForeignKey("cities.id", ondelete="CASCADE"),
                         nullable=False)
        user_id = Column(String(60),
                         ForeignKey("users.id", ondelete="CASCADE"),
                         nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)

        reviews = relationship("Review", backref="place", cascade="all, delete")

    elif getenv("HBNB_TYPE_STORAGE") == "file":
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            from models.__init__ import storage
            from models.review import Review

            reviews_list = []
            for key, val in storage.all(Review).items():
                if val["place_id"] == self.id:
                    reviews_list.append(val)
            return reviews_list
