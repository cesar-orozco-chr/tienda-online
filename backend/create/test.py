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

    def test_product_create(self):
        p = Product(11, 'Medias', 3000)
        db.session.add(p)
        db.session.commit()
        self.assertIsNotNone(Product.query.filter(Product.productid == 11).first())

    def test_client_create(self):
        c = Client(10, "Arturo Reyes")
        db.session.add(c)
        db.session.commit()
        self.assertIsNotNone(Client.query.filter(Client.clientid == 10).first())

    def test_purchase_create(self):
        pr = Purchase('en alistamiento', 11, 10)
        db.session.add(pr)
        db.session.commit()
        self.assertIsNotNone(Purchase.query.first())


if __name__ == '__main__':
    unittest.main()

