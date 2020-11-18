from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class RegisterForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm-Password', validators=[DataRequired()])
    submit = SubmitField('Sign')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign')
