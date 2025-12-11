from typing import Union


class Producto(object):
    """Modelo de producto."""

    def __init__(self, id_producto: int, nombre: str, descripcion: str) -> None:
        self.id_producto: Union[int, None] = id_producto
        self.nombre: str = nombre
        self.descripcion: str = descripcion

    def __str__(self) -> str:
        return (f"ID={str(self.id_producto) if self.id_producto is not None else ""}, Nombre={self.nombre}, "
                f"Descripcion={self.descripcion}")

    def __eq__(self, other):
        return self.id_producto == other.id_producto