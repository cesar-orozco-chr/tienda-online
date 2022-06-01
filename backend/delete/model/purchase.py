#backend.delete.model
from datetime import datetime
from connection import db


class Purchase(db.Model):
    __tablename__ = "purchase"

    purchaseid = db.Column(db.Integer, primary_key=True)
    shipping_state = db.Column(db.String(25))
    productid = db.Column(db.Integer, db.ForeignKey('product.productid'))
    product = db.relationship('Product', backref=db.backref('purchase', lazy=True))
    clientid = db.Column(db.Integer, db.ForeignKey('client.clientid'))
    client = db.relationship('Client', backref=db.backref('purchase', lazy=True))
    created_at = db.Column(db.Date, default=datetime.now())

    def __init__(self, shipping, productid, clientid):
        self.shipping_state = shipping
        self.productid = productid
        self.clientid = clientid

    def __str__(self):
        pass
