""" This module exports the database engine.
Notes:
     Using the scoped_session contextmanager is
     best practice to ensure the session gets closed
     and reduces noise in code by not having to manually
     commit or rollback the db if a exception occurs.
Copied from: https://github.com/seanpar203/sanic-starter/blob/master/app/database.py
"""
import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

engine = create_engine(Config.DB_CONNECTION)
# Session to be used throughout app.
Session = sessionmaker(bind=engine)

@contextmanager
def scoped_session():
    session = Session()
    try:
        yield session
        session.expunge_all()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()