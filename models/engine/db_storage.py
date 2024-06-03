#!/usr/bin/python3
"""File containing the definition of the DBStorage class"""

import os
import MySQLdb
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

user = os.getenv("HBNB_MYSQL_USER")
pwd = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")
db = os.getenv("HBNB_MYSQL_DB")


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of the DBStorage class"""
        url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(user, pwd, host, db)
        self.__engine = create_engine(url, pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of the instances"""
        obj_dict = {}
        if cls is None:
            cls_list = ["User", "State", "City", "Amenity", "Place", "Review"]
            for c in cls_list:
                cls_objs = self.__session.query(eval(c)).all()
                for instance in cls_objs:
                    key = c + '.' + instance.id
                    obj_dict[key] = instance
            return obj_dict
        else:
            cls_objs = self.__session.query(eval(cls.__name__)).all()
            for instance in cls_objs:
                name = type(cls).__name__
                key = name + '.' + instance.id
                obj_dict[key] = instance
            return obj_dict

    def new(self, obj):
        """Adds a new instance to the session"""
        self.__session.add(obj)

    def save(self):
        """Saves an instance"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Creates the tables and initializes the session"""
        Base.metadata.create_all(self.__engine)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session()

    def close(self):
        self.__session.close()
