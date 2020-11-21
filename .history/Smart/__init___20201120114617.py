from flask import Flask
from flask_sqlalchemy import  SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_FATABASE_URI'] = 'sqlite:///smart.db'
db = SQLAlchemy(app)

from Smart.admin import routes