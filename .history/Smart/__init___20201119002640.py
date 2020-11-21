from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from Smart import admin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_FATABASE_URI'] = 'sqlite:///smart.db'
db = SQLAlchemy(app)

from Smart.admin import routes