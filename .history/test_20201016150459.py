
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir= os.path.abspath(os.path.dirname(__file__))

print(basedir)