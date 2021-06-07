from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms.fields.html5 import EmailField


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                        validators=[DataRequired(), 
                        Length(min=2, max=20)])
    email = EmailField('Email', 
            validators=[ validators.email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
        email = StringField('Email', 
                validators=[DataRequired(), validators.email()])
        password = PasswordField('Password', validators=[DataRequired()])
        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')
