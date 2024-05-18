#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(60), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade="delete")

        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)
    else:
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
            """A getter attribute that returns a list of reviews
            related to a place"""
            from models.storage import FileStorage
            storage = FileStorage()
            rev_list = []
            instances = storage.all(Review)
            for key, obj in instances.items():
                if self.id == obj.id:
                    rev_list.append(instance)
            return rev_list

        @property
        def amenities(self):
            """Getter method for the amenity_ids"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """setter for amenity_ids"""
            if obj is None or obj.__class__.__name__ != "Amenity":
                return
            self.amenity_ids.append(obj.id)
