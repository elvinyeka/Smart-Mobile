from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkeydfgfdgdfgdfg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smart.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from Smart.admin import routes
from Smart.products import  routes