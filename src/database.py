from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from settings import DB

ORMBase = declarative_base()

DB_URI = '{engine}://{username}:{password}@{host}/{database}'.format(**DB)


def get_db_session():

    engine = create_engine(DB_URI, echo=True)
    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)
    return session


def create_all():
    engine = create_engine(DB_URI, echo=True)
    ORMBase.metadata.create_all(engine)


def drop_all():

    engine = create_engine(DB_URI, echo=True)
    ORMBase.metadata.drop_all(engine)
