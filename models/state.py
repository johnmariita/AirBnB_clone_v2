#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")

    else:
        name = ""

        @property
        def cities(self):
            """Function to return the cities associates with a state"""
            from models import storage
            cities_list = []
            objs = storage.all(City)
            for key, obj in objs.items():
                if obj.state_id == self.id:
                    cities_list.append(obj)
            return cities_list
