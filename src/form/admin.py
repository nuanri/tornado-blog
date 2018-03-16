from wtforms import BooleanField, StringField, validators, TextField
# from wtforms.validators import DataRequired

from custon_form import Form


class UserinfoEditForm(Form):
    username = StringField('Username', [validators.Length(min=6, max=32)])
    nickname = StringField('Nickname', [validators.Length(min=0, max=32)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    is_admin = BooleanField('Is_Admin')
    is_lock = BooleanField('Is_Lock')
