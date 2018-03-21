from wtforms import BooleanField, validators, TextField
from wtforms.validators import DataRequired

from custon_form import Form


class ArticleForm(Form):
    title = TextField('Title', validators=[
                DataRequired(message=u'标题不能为空')])
    content = TextField('Content', validators=[
                DataRequired(message=u'正文不能为空')])
    is_public = BooleanField('Is_Public')
