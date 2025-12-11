from typing import Union

import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract
from mysql.connector.pooling import PooledMySQLConnection

from utils.fileutils import read_section_in_ini_file


class BaseDao(object):
    """DAO principal."""

    def __init__(self):
        # Cargar credenciales desde fichero ini
        db_credentials: dict = read_section_in_ini_file("db", "MySQL")
        # Inicializar atributos
        self.__host: str = db_credentials["host"]
        self.__database: str = db_credentials["database"]
        self.__user: str = db_credentials["user"]
        self.__password: str = db_credentials["password"]
        self.__port: int = int(db_credentials["port"])
        # Dejo preparada la conexión
        self.__connection: Union[PooledMySQLConnection, MySQLConnectionAbstract, None] = None

    def connect(self):
        """Conexión con la DB."""
        self.__connection = mysql.connector.connect(
            host=self.__host,
            port=self.__port,
            database=self.__database,
            user=self.__user,
            password=self.__password)

    def disconnect(self):
        """Función para desconectar de la DB."""
        self.__connection.close()
        self.__connection = None

    def commit(self):
        if self.__connection is not None:
            self.__connection.commit()
        else:
            raise Exception("No connection!!!")

    def rollback(self):
        if self.__connection is not None:
            self.__connection.rollback()
        else:
            raise Exception("No connection!!!")

    def create_cursor(self) -> MySQLCursorAbstract:
        """Devuelve un cursor de MySQL para hacer alguna operación."""
        if self.__connection is not None:
            return self.__connection.cursor()
        else:
            raise Exception("No connection!!!")