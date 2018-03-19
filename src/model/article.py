import re

from sqlalchemy import Column, Integer, String, Text, ForeignKey,\
    DateTime, Sequence, Boolean
from sqlalchemy.orm import relationship

from database import ORMBase
from utils.custom_markdown import convert_html
from utils.html_tags import strip_tags


class Article(ORMBase):

    __tablename__ = 'blog_article'

    id = Column(Integer, Sequence('blog_article_id_seq'), primary_key=True)
    title = Column(String(512))
    user_id = Column(Integer, ForeignKey('auth_user.id'))
    user = relationship("User", backref="aticles")
    content = Column(Text())
    created = Column(DateTime())
    updated = Column(DateTime())
    public = Column(Boolean, default=False)
    view_count = Column(Integer)

    def __init__(self, user, title, content):
        self.user_id = user.id
        self.title = title
        self.content = content

    @property
    def content_html(self):
        return convert_html(self.content)

    @property
    def abstract(self):
        try:
            txt = strip_tags(convert_html(self.content))
            # txt do something
            txt = txt[0:300]
            return txt
        except:
            txt = re.sub(r'</?\w+[^>]*>', '', convert_html(self.content))[0:300]
            return txt
            pass
