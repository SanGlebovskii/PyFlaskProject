from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)

DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'test23'
DB_ECHO = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
db = SQLAlchemy(app)
if not database_exists(db.engine.url):
    create_database(db.engine.url)
db.init_app(app)
db.create_all()
