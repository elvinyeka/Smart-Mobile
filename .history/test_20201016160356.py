
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Name: {self.name} Age: {self.age}'