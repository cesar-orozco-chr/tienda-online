from datetime import datetime
from backend.create.connection.connection import get_sql_alchemy

db = get_sql_alchemy()


class Product(db.Model):
    __tablename__ = 'Products'

    productId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    price = db.Column(db.Integer)
    state = db.Column(db.String(25))
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, productId, name, price, state):
        self.productId = productId
        self.name = name
        self.price = price
        self.state = state

    def __str__(self) -> str:
        return "<Product %r>" % self.name
