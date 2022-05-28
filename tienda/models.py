from tienda import db
from datetime import datetime


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


class Client(db.Model):
    __tablename__ = "client"
    clientid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    created_at = db.Column(db.Date, default=datetime.now())

    def __init__(self, clientid, name):
        self.clientid = clientid
        self.name = name

    def __str__(self):
        return f"Client :" \
               f"{self.name}"

