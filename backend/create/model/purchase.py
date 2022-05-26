from datetime import datetime
from backend.create.connection.connection import get_sql_alchemy

db = get_sql_alchemy()


class Purchase(db.Model):
    __tablename__ = 'Purchases'

    purchaseId = db.Column(db.Integer, primary_key=True)
    shippingState = db.Column(db.String(25))
    productId = db.Column(db.Integer)
    clientId = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, purchaseId, shippingState, productId, clientId):
        self.purchaseId = purchaseId
        self.shippingState = shippingState
        self.productId = productId
        self.clientId = clientId

    def __str__(self) -> str:
        return "<Purchase Id: %r State: %r>" % self.purchaseId % self.shippingState
