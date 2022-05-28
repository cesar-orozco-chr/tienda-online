from connection import db, create_app
from model.product import Product
from model.client import Client
from model.purchase import Purchase

import unittest
import os


class TestApp(unittest.TestCase):
    def setUp(self):
        os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app = create_app()
        self.app.app_context().push()
        db.create_all()

    def test_product_list(self):
        p = Product(11, 'Medias', 3000, 'activo')
        db.session.add(p)
        db.session.commit()
        self.assertIsNotNone(Product.query.all())

    def test_client_list(self):
        c = Client(10, "Arturo Reyes")
        db.session.add(c)
        db.session.commit()
        self.assertIsNotNone(Client.query.all())

    def test_purchase_list(self):
        pr = Purchase('en alistamiento', 11, 10)
        db.session.add(pr)
        db.session.commit()
        self.assertIsNotNone(Purchase.query.first())


if __name__ == '__main__':
    unittest.main()

