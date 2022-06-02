#backend.delete.model
from datetime import datetime
from connection import db


class Client(db.Model):
    __tablename__ = "client"

    clientid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    state = db.Column(db.String(10), default="activo")
    created_at = db.Column(db.Date, default=datetime.now())

    def __init__(self, clientid, name):
        self.clientid = clientid
        self.name = name

    def __str__(self):
        return f"Client :" \
               f"{self.name}"
