from sqlalchemy import Column, Integer, String, Text, ForeignKey,\
    DateTime, Sequence, Boolean
from sqlalchemy.orm import relationship
from database import ORMBase


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

    def __init__(self, title, content):
        self.title = title
        self.content = content
