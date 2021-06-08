from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from wtforms.fields.html5 import EmailField

from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=2, max=20)])
    email = EmailField('Email',
                       validators=[validators.email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        # this is how we query data and raise validation error
        user = User.query.filter_by(username=username.data).first()
        if user :
            raise ValidationError('that user name is taken, please choose another name.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('that email is taken.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), validators.email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
