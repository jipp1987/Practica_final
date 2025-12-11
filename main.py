from impl.dao.productodaoimpl import ProductoDAOImpl

if __name__ == "__main__":
    producto_dao: ProductoDAOImpl = ProductoDAOImpl()
    last_id: int = producto_dao.insert("Cereales",
                                       "Cereales de avena.")
    print(last_id)