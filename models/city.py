#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base


class City(BaseModel, Base):
  
    """ The city class, contains state ID and name """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        from sqlalchemy import Column, String, ForeignKey
        from sqlalchemy.orm import relationship

        __tablename__="cities"
        name = Column(String(128), nullable=False)

        state_id = Column(String(60),
                        ForeignKey("states.id", ondelete="CASCADE"),
                        nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")

    elif getenv("HBNB_TYPE_STORAGE") == "file":
        name = ""
