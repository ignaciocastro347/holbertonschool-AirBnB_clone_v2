#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import getenv

class Review(BaseModel, Base):
    """ Review classto store review information """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        from sqlalchemy import Column, String, ForeignKey

        __tablename__ = "reviews"
        description = Column(String(1024), nullable=False)
        place_id = Column(String(60),
                         ForeignKey("places.id", ondelete="CASCADE"),
                         nullable=False)
        user_id = Column(String(60),
                         ForeignKey("users.id", ondelete="CASCADE"),
                         nullable=False)

    elif getenv("HBNB_TYPE_STORAGE") == "file":
        place_id = ""
        user_id = ""
        text = ""
