#!/usr/bin/python3
""" Module DBStorage """
from os import getenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ Class DBStorage that establishes a connection to a database """
    __engine = None
    __session = None

    def __init__(self):
        """Intanciate this Class"""
        args = ["mysql+mysqldb://{}:{}@{}/{}",
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")]
        self.__engine = create_engine(args[0].format(args[1],
                                                     args[2],
                                                     args[3],
                                                     args[4]),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            from models.base_model import Base
            Base.metadata.drop_all()

    def all(self, cls=None):
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = [User, State, City, Place, Review]
        result = []
        dict_of_instances = {}

        if cls:
            if cls not in classes:
                raise Exception("class is not valid")

            result = self.__session.query(cls).all()
        else:
            for c in classes:
                result.extend(self.__session.query(c).all())

        for instance in result:

            dict_aux = instance.to_dict()
            key = "{}.{}".format(dict_aux["__class__"], dict_aux["id"])

            dict_of_instances[key] = instance.to_dict()

        return dict_of_instances

    def new(self, obj):
        """Add new obj to session"""
        self.__session.add(obj)

    def save(self):
        """Save all pending changes in session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        from models.city import City
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
