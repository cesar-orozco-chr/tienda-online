from flask_sqlalchemy import SQLAlchemy
from flask import Flask

import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://docker:docker@192.168.0.8:5439/docker"
    # os.getenv('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)
    return app
