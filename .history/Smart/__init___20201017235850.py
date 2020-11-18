from flask import Flask
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

from Smart import routes