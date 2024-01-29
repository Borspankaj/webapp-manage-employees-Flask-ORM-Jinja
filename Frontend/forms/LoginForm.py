from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LoginForm(FlaskForm):
    email = StringField('email')
    password = StringField('password')
    submit = SubmitField('Submit')
    