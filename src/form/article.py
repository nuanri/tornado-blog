from wtforms import BooleanField,validators, TextField

from custon_form import Form


class ArticleForm(Form):
    title = TextField('Title')
    content = TextField('Content')
