from connection import db, create_app
from model.product import Product
from model.client import Client

import unittest
import os


class TestApp(unittest.TestCase):
    def setUp(self):
        os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app = create_app()
        self.app.app_context().push()
        db.create_all()

    def test_product_delete(self):
        p = Product(11, 'Medias', 3000, 'activo')
        db.session.add(p)
        db.session.commit()
        d = Product.query.get(11)
        d.state = 'inactivo'
        db.session.add(d)
        db.session.commit()
        self.assertIsNone(Product.query.filter(Product.state == 'activo').first())

    def test_client_delete(self):
        c = Client(10, "Arturo Reyes")
        db.session.add(c)
        db.session.commit()
        d = Client.query.get(10)
        d.state = 'inactivo'
        db.session.add(d)
        db.session.commit()
        self.assertIsNone(Client.query.filter(Client.state == 'activo').first())


if __name__ == '__main__':
    unittest.main()

