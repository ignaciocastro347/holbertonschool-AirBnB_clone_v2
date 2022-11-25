#!/usr/bin/python3
""" Module DBStorage """
from os import getenv
from sqlalchemy import create_engine, text


class DBStorage:
    """ Class DBStorage that establishes a connection to a database """
    __engine = None
    __session = None

    def __init__(self):

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

            connection = create_engine("mysql+mysqldb://{}:{}@{}/information_schema".format(args[1],
                                                                                            args[2],
                                                                                            args[3]))

            command = "SELECT TABLE_NAME FROM `TABLES` WHERE TABLE_SCHEMA = '{}';".format(getenv("HBNB_MYSQL_DB"))
            result = connection.execute(text(command))

            connection.dispose()

            for row in result:
                print(row["TABLE_NAME"])
                self.__engine.execute("DROP TABLE {};".format(row["TABLE_NAME"]))

if __name__ == "__main__":
    conection = DBStorage()