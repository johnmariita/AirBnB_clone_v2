#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import os
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    class Base:
        pass


class BaseModel:
    """A base class for all hbnb models"""
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime,
                            default=datetime.utcnow(), nullable=False)
        updated_at = Column(DateTime,
                            default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            try:
                ut = datetime.strptime(kwargs['updated_at'],
                                       '%Y-%m-%dT%H:%M:%S.%f')
                ct = datetime.strptime(kwargs['created_at'],
                                       '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['updated_at'] = ut
                kwargs['created_at'] = ct
            except KeyError:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes the current instance"""
        from models import storage
        storage.delete(self)
