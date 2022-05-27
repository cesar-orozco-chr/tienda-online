from datetime import datetime
from backend.create.connection.connection import get_sql_alchemy

db = get_sql_alchemy()


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
