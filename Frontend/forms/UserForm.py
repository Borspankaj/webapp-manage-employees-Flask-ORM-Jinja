from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField , SelectField

class UserForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email')
    phone_number = StringField('Phone Number')
    role = SelectField('Role', choices=[('ADMIN', 'ADMIN'), ('EMP', 'EMP')])
    password = StringField('Password')
    address = StringField('Address')
    submit = SubmitField('Submit')