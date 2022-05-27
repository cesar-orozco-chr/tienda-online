from datetime import datetime
from backend.create.connection.connection import get_sql_alchemy

db = get_sql_alchemy()


class Product(db.Model):
    __tablename__ = "product"

    productid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    price = db.Float()
    state = db.Column(db.String(10), default="activo")
    created_at = db.Column(db.Date, default=datetime.now())

    def __init__(self, productid, name, price, state):
        self.productid = productid
        self.name = name
        self.price = price
        self.state = state

    def __str__(self):
        return f"Product : " \
               f"{self.name}"
