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

    def test_product_update(self):
        p = Product(11, 'Medias', 3000, 'activo')
        db.session.add(p)
        db.session.commit()
        d = Product.query.get(11)
        d.state = 'inactivo'
        db.session.add(d)
        db.session.commit()
        s = Product.query.first()
        self.assertEqual(s.state, 'inactivo')

    def test_client_update(self):
        c = Client(10, "Arturo Reyes")
        db.session.add(c)
        db.session.commit()
        d = Client.query.get(10)
        d.state = 'inactivo'
        db.session.add(d)
        db.session.commit()
        s = Client.query.first()
        self.assertEqual(s.state, 'inactivo')

    def test_purchase_update(self):
        pr = Purchase('en alistamiento', 11, 10)
        db.session.add(pr)
        db.session.commit()
        s = Purchase.query.first()
        s.shipping_state = 'Enviado'
        db.session.add(s)
        db.session.commit()
        self.assertEqual(s.shipping_state, 'Enviado')


if __name__ == '__main__':
    unittest.main()

