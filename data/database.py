import os
from flask_sqlalchemy import SQLAlchemy
from app import flask_app

basedir = os.path.abspath(os.path.dirname(__file__))

# Could be env vars
db_username = 'postgres'
db_password = 'email_app'
db_host = 'localhost'
db_name = 'email_app'
db_port = '5432'

flask_app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flask_app)