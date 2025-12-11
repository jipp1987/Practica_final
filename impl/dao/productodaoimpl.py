from core.dao.basedao import BaseDao
from impl.model.producto import Producto


class ProductoDAOImpl(BaseDao):
    """Implementación de DAO para productos."""

    def __init__(self):
        # Llamar al init de la clase padre
        super().__init__()
        # Inicializo los atributos propios del DAO de producto: nombre de la tabla en la BD
        # y clase principal del modelo
        self.table: str = 'producto'
        self.model_class: type = Producto

    def insert(self, nombre: str, descripcion: str) -> int:
        """
        Función para insertar un producto.
        :param nombre:
        :param descripcion:
        :return: Devuelve el id del producto recién creado.
        """
        sql = (f"INSERT INTO {self.table} (nombre, descripcion) VALUES ('{nombre}', "
               f"'{descripcion}')")
        return super()._execute_statement(sql_statement=sql,
                                          callback_function=self._get_last_rowid)
