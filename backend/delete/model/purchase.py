from datetime import datetime
from backend.create.connection.connection import get_sql_alchemy

db = get_sql_alchemy()


class Purchase(db.Model):
    __tablename__ = "purchase"

    purchaseid = db.Column(db.Integer, primary_key=True)
    shipping_state = db.Column(db.String(25))
    productid = db.Column(db.Integer, db.ForeignKey('product.productid'))
    product = db.relationship('Product', backref=db.backref('purchase', lazy=True))
    clientid = db.Column(db.Integer, db.ForeignKey('client.clientid'))
    client = db.relationship('Client', backref=db.backref('purchase', lazy=True))
    created_at = db.Column(db.Date, default=datetime.now())

    def __init__(self, purchaseid, shipping, productid, clientid):
        self.purchaseid = purchaseid
        self.shipping_state = shipping
        self.productid = productid
        self.clientid = clientid

    def __str__(self):
        pass
