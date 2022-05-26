from datetime import datetime
from backend.create.connection.connection import get_sql_alchemy

db = get_sql_alchemy()


class Client(db.Model):
    __tablename__ = 'Clients'

    clientId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, clientId, name):
        self.clientId = clientId
        self.name = name

    def __str__(self) -> str:
        return "<Client Id: %r Name: %r>" % self.clientId % self.name
