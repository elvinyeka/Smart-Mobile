from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email

class RegisterForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
