from sqlalchemy import Column, Integer, String, Text, ForeignKey,\
    DateTime, Table, Sequence, Boolean
from database import ORMBase
from utils.enc import check_password


class User(ORMBase):

    __tablename__ = 'auth_user'

    id = Column(Integer, Sequence('auth_user_id_seq'), primary_key=True)
    username = Column(String(30), unique=True)
    nickname = Column(String(30))
    email = Column(String(64), unique=True)
    img = Column(String(1024))
    password = Column(String(512))
    is_admin = Column(Boolean, default=False)
    is_lock = Column(Boolean, default=False)
    date_joined = Column(DateTime())
    last_login = Column(DateTime())

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def validate_password(self, raw_password):
        return check_password(raw_password, self.password)
