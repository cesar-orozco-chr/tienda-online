from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

db = SQLAlchemy()


def create_app(template_folder):
    app = Flask(__name__, template_folder=template_folder)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)
    return app
