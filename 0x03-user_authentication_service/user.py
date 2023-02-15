#!/usr/bin/env python3
""" The user module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ A user class for the user table
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)


    def __repr__(self):
        """ String representation of the user instance
        """
        return "<User(email='%s', hashed_password='%s', session_id='%s', reset_token='%s') \
                >" % (self.email, self.hashed_password, self.session_id, self.reset_token)
