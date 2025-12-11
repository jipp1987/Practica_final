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

    def insert(self, nombre: str, descripcion: str) -> None:
        """Función para insertar un producto."""
        sql = (f"INSERT INTO {self.table} (nombre, descripcion) VALUES ('{nombre}', "
               f"'{descripcion}')")

        # Conectar con la base de datos
        self.connect()
        # Crear cursor, SQL y hacer commit
        cursor = self.create_cursor()
        cursor.execute(sql)
        self.commit()
        # Desconectar de la BD
        self.disconnect()
