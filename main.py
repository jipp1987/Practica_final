from impl.dao.productodaoimpl import ProductoDAOImpl

if __name__ == "__main__":
    producto_dao: ProductoDAOImpl = ProductoDAOImpl()
    producto_dao.insert("Patatas fritas", "Bolsa de patatas de 70 gramos.")