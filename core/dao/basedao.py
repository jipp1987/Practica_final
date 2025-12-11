from typing import Union, Callable

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
        self._connection: Union[PooledMySQLConnection, MySQLConnectionAbstract, None] = None
        self._cursor: Union[MySQLCursorAbstract, None] = None

    def connect(self):
        """Conexión con la DB."""
        self._connection = mysql.connector.connect(
            host=self.__host,
            port=self.__port,
            database=self.__database,
            user=self.__user,
            password=self.__password)

    def disconnect(self):
        """Función para desconectar de la DB."""
        self._connection.close()
        self._connection = None

    def commit(self):
        if self._connection is not None:
            self._connection.commit()
        else:
            raise Exception("No connection!!!")

    def rollback(self):
        if self._connection is not None:
            self._connection.rollback()
        else:
            raise Exception("No connection!!!")

    def create_cursor(self) -> None:
        """Devuelve un cursor de MySQL para hacer alguna operación."""
        if self._connection is not None:
            self._cursor = self._connection.cursor()
        else:
            raise Exception("No connection!!!")

    def _get_last_rowid(self) -> int:
        """Devuelve un cursor de MySQL para hacer alguna operación."""
        if self._connection is not None:
            return self._cursor.lastrowid
        else:
            raise Exception("No connection!!!")

    def _execute_statement(self, sql_statement: str,
                           callback_function: Union[Callable, None] = None):
        """
        Función para ejecutar sentencias SQL.
        :param sql_statement: SQL statement para insertar.
        :return: Devuelve el id del producto recién creado.
        """
        try:
            result = None
            # Conectar con la base de datos
            self.connect()
            # Crear cursor, SQL y hacer commit
            self.create_cursor()
            self._cursor.execute(sql_statement)
            self.commit()

            # Por si es necesaria alguna función de callback al terminar la acción.
            if callback_function is not None:
                result = callback_function()

            # Desconectar de la BD
            self._cursor.close()
            self.disconnect()

            return result
        except Exception as e:
            raise e

