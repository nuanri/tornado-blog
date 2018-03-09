from wtforms import BooleanField, StringField, PasswordField, validators, TextField

from custon_form import Form

class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=6, max=32)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required()])
